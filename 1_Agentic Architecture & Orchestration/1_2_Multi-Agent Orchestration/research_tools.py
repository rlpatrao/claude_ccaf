"""Stub research tools for lab 1.2, served from an in-process MCP server.

Claude sees these tools as:
    mcp__research__search_sources
    mcp__research__get_document

The coordinator does not get these tools. Each subagent's AgentDefinition lists
only the one tool it needs.
"""

import json
import re

from claude_agent_sdk import create_sdk_mcp_server, tool

from corpus import DOCUMENTS

SERVER_NAME = "research"
SEARCH_TOOL = f"mcp__{SERVER_NAME}__search_sources"
GET_DOCUMENT_TOOL = f"mcp__{SERVER_NAME}__get_document"


def _text(payload, is_error=False):
    """Wrap a payload in the result shape the SDK expects from a tool."""
    text = payload if isinstance(payload, str) else json.dumps(payload)
    result = {"content": [{"type": "text", "text": text}]}
    if is_error:
        result["is_error"] = True
    return result


# Generic words that would otherwise match unrelated titles ("Tidal ... Energy").
STOPWORDS = {"and", "the", "for", "with", "energy", "power", "renewable",
             "technology", "technologies", "systems", "global", "market"}


def search(query: str) -> list[dict]:
    """Plain function, so the matching logic can be tested without the SDK.

    Matches any query word (3+ characters, excluding STOPWORDS) against a
    document's title and keywords. Document bodies are not searched, so results
    stay predictable.
    """
    words = {w for w in re.findall(r"[a-z0-9]+", query.lower())
             if len(w) >= 3 and w not in STOPWORDS}
    hits = []
    for doc_id, doc in DOCUMENTS.items():
        haystack = set(re.findall(r"[a-z0-9]+", doc["title"].lower()))
        haystack.update(k.lower() for k in doc["keywords"])
        if words & haystack:
            hits.append({"source_id": doc_id, "title": doc["title"], "date": doc["date"]})
    return hits


@tool(
    "search_sources",
    "Search the research corpus for sources on one subtopic. Returns a JSON list of "
    "{source_id, title, date}; it does not return document text. Use short, specific "
    "terms (for example 'tidal stream' or 'geothermal'). An empty list means no "
    "source matched; try a synonym before concluding that nothing exists.",
    {"query": str},
)
async def search_sources(args):
    hits = search(args["query"])
    return _text(hits)


@tool(
    "get_document",
    "Return the full record of one source by its source_id (for example 'SOL-01'): "
    "title, publisher, date and text. Returns an error for an unknown source_id.",
    {"source_id": str},
)
async def get_document(args):
    doc_id = args["source_id"].strip().upper()
    if doc_id not in DOCUMENTS:
        return _text(
            f"Unknown source_id '{args['source_id']}'. Use search_sources to find valid IDs.",
            is_error=True,
        )
    doc = DOCUMENTS[doc_id]
    return _text({"source_id": doc_id, **{k: doc[k] for k in ("title", "publisher", "date", "text")}})


research_server = create_sdk_mcp_server(
    name=SERVER_NAME, version="1.0.0", tools=[search_sources, get_document]
)

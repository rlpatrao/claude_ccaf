"""Stub document corpus for lab 1.2.

The documents are synthetic. Publishers are fictional and figures are
illustrative; do not cite them outside this lab.

Two properties are deliberate:
- Solar has two documents that give different global capacity figures from
  different years (SOL-01 and SOL-02). Lab 5.6 (information provenance) reuses
  this conflict.
- Fusion is reachable only by searching for fusion-specific terms. A coordinator
  that treats "renewable" narrowly and omits fusion will not find it by accident.
"""

DOCUMENTS = {
    "SOL-01": {
        "title": "Global Solar Photovoltaic Market Review",
        "publisher": "Helios Energy Observatory (fictional)",
        "date": "2022-06-15",
        "keywords": ["solar", "photovoltaic", "pv", "panels", "capacity"],
        "text": (
            "Installed global solar photovoltaic capacity reached approximately 940 GW "
            "at the end of 2021. Utility-scale plants accounted for about 60% of new "
            "additions. Module prices fell by roughly 85% between 2010 and 2021."
        ),
    },
    "SOL-02": {
        "title": "Solar Capacity Outlook",
        "publisher": "Northwind Analytics (fictional)",
        "date": "2024-03-02",
        "keywords": ["solar", "photovoltaic", "pv", "capacity", "perovskite"],
        "text": (
            "Global solar photovoltaic capacity passed 1,600 GW at the end of 2023. "
            "Perovskite-silicon tandem cells have exceeded 33% efficiency in laboratory "
            "conditions but are not yet commercially durable."
        ),
    },
    "WND-01": {
        "title": "Onshore and Offshore Wind: Cost and Deployment",
        "publisher": "Coastal Grid Institute (fictional)",
        "date": "2023-09-10",
        "keywords": ["wind", "turbine", "offshore", "onshore"],
        "text": (
            "Offshore wind turbines now exceed 15 MW per unit. Floating foundations allow "
            "deployment in water deeper than 60 m. Onshore wind remains one of the "
            "lowest-cost sources of new electricity in most markets."
        ),
    },
    "GEO-01": {
        "title": "Enhanced Geothermal Systems Field Trials",
        "publisher": "Deep Heat Research Council (fictional)",
        "date": "2023-11-20",
        "keywords": ["geothermal", "egs", "heat", "drilling"],
        "text": (
            "Enhanced geothermal systems create permeability in hot dry rock so that heat "
            "can be extracted where natural reservoirs do not exist. Field trials report "
            "sustained flow rates sufficient for multi-megawatt plants. Drilling cost is "
            "the main barrier to wider adoption."
        ),
    },
    "TID-01": {
        "title": "Tidal Stream and Tidal Range Energy",
        "publisher": "Marine Energy Forum (fictional)",
        "date": "2022-12-05",
        "keywords": ["tidal", "marine", "ocean", "tide", "stream"],
        "text": (
            "Tidal energy is highly predictable because it follows lunar cycles. Tidal "
            "stream turbines operate like underwater wind turbines; tidal range schemes "
            "use barrages or lagoons. Installed capacity worldwide remains below 1 GW."
        ),
    },
    "BIO-01": {
        "title": "Biomass and Bioenergy: Feedstocks and Emissions",
        "publisher": "Agricultural Energy Review (fictional)",
        "date": "2023-04-18",
        "keywords": ["biomass", "bioenergy", "biofuel", "biogas", "feedstock"],
        "text": (
            "Biomass energy uses organic feedstocks such as forestry residues, crops and "
            "waste. Its carbon benefit depends on feedstock sourcing and regrowth time. "
            "Anaerobic digestion produces biogas from agricultural and food waste."
        ),
    },
    "FUS-01": {
        "title": "Magnetic Confinement Fusion: Progress Report",
        "publisher": "Plasma Physics Consortium (fictional)",
        "date": "2024-01-25",
        "keywords": ["fusion", "tokamak", "plasma", "stellarator"],
        "text": (
            "Fusion is not yet a commercial energy source. Tokamak and stellarator "
            "experiments have extended plasma confinement times, and one inertial "
            "confinement experiment reported target gain above 1. Commercial plants are "
            "not expected before the late 2030s at the earliest."
        ),
    },
    "HYD-01": {
        "title": "Hydropower and Pumped Storage",
        "publisher": "River Systems Authority (fictional)",
        "date": "2023-07-30",
        "keywords": ["hydro", "hydropower", "dam", "pumped storage"],
        "text": (
            "Hydropower is the largest source of renewable electricity by generation. "
            "Pumped storage hydropower provides most of the world's grid-scale energy "
            "storage capacity."
        ),
    },
}

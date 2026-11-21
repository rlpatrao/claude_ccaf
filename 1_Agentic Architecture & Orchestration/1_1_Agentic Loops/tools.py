"""Stub tools for lab 1.1. No external API is called; all data is hard-coded."""

WEATHER_DATA = {
    "paris": {"city": "Paris", "temp_c": 18, "condition": "cloudy"},
    "tokyo": {"city": "Tokyo", "temp_c": 24, "condition": "sunny"},
    "london": {"city": "London", "temp_c": 12, "condition": "rain"},
    "new york": {"city": "New York", "temp_c": 21, "condition": "clear"},
}

# Units accepted by convert_units. Use this same list for the enum in your schema.
SUPPORTED_UNITS = ["C", "F", "km", "miles"]


def get_weather(city):
    """
    Returns stub weather data for a city from WEATHER_DATA.

    Args:
        city (str): City name, case-insensitive.

    Returns:
        dict: city, temp_c, condition.

    Raises:
        ValueError: if the city is not in WEATHER_DATA.
    """
    key = city.strip().lower()
    if key not in WEATHER_DATA:
        known = ", ".join(c["city"] for c in WEATHER_DATA.values())
        raise ValueError(f"No weather data for '{city}'. Known cities: {known}.")
    return WEATHER_DATA[key]


def convert_units(value, from_unit, to_unit):
    """
    Converts a value between C and F, or between km and miles.

    Args:
        value (float): The value to convert.
        from_unit (str): One of SUPPORTED_UNITS.
        to_unit (str): One of SUPPORTED_UNITS.

    Returns:
        dict: value, unit (the converted result, rounded to 2 decimals).

    Raises:
        ValueError: if the unit pair is not supported (for example C to km).
    """
    if from_unit == "F" and to_unit == "C":
        result = (value - 32) / 1.8
    elif from_unit == "C" and to_unit == "F":
        result = value * 1.8 + 32
    elif from_unit == "km" and to_unit == "miles":
        result = value / 1.609344
    elif from_unit == "miles" and to_unit == "km":
        result = value * 1.609344
    else:
        raise ValueError(
            f"Unsupported conversion: {from_unit} to {to_unit}. "
            "Supported pairs: C<->F, km<->miles."
        )
    return {"value": round(result, 2), "unit": to_unit}


# ---------------------------------------------------------------------------
# Tool schemas sent to Claude. Property names must match the Python parameter
# names above, because the agent loop calls each function with **block.input.
# ---------------------------------------------------------------------------

GET_WEATHER_SCHEMA = {
    "name": "get_weather",
    "description": (
        "Returns the current weather for one city: city name, temperature in "
        "degrees Celsius (temp_c), and a short condition such as 'sunny'. "
        "Use this whenever the user asks about weather or temperature in a city. "
        "Temperatures are always returned in Celsius; use convert_units if the "
        "user wants Fahrenheit. Returns an error if the city is not known."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "City name in plain English, for example 'Paris' or 'New York'.",
            },
        },
        "required": ["city"],
    },
}

CONVERT_UNITS_SCHEMA = {
    "name": "convert_units",
    "description": (
        "Converts a numeric value between temperature units (C and F) or "
        "between distance units (km and miles). Returns the converted value "
        "rounded to 2 decimals and its unit. Only C<->F and km<->miles are "
        "supported; mixing a temperature unit with a distance unit returns an error."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "value": {
                "type": "number",
                "description": "The numeric value to convert.",
            },
            "from_unit": {
                "type": "string",
                "enum": SUPPORTED_UNITS,
                "description": "Unit of the input value.",
            },
            "to_unit": {
                "type": "string",
                "enum": SUPPORTED_UNITS,
                "description": "Unit to convert to.",
            },
        },
        "required": ["value", "from_unit", "to_unit"],
    },
}

# Pass this list to client.messages.create(tools=TOOLS).
TOOLS = [GET_WEATHER_SCHEMA, CONVERT_UNITS_SCHEMA]

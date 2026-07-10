"""
Mock Maritime Analytics Engine
Hackathon Demo Version

This module simulates maritime traffic around the Strait of Hormuz.
No SQLite, AIS Stream, or external APIs are required.
"""

import asyncio
import random
from datetime import datetime, timezone

# ==========================================================
# GATE DEFINITIONS
# ==========================================================

GATE_A = (26.05, 56.50)
GATE_B = (26.65, 56.10)

GATES = {
    "Strait of Hormuz": {
        "a": GATE_A,
        "b": GATE_B,
        "description": "Primary global oil shipping chokepoint",
    },
    "Fujairah Approach": {
        "a": (25.00, 56.50),
        "b": (25.30, 56.50),
        "description": "Fujairah Port",
    },
    "Dubai Approach": {
        "a": (25.00, 55.20),
        "b": (25.35, 55.20),
        "description": "Dubai / Jebel Ali",
    },
}

# ==========================================================
# ANCHORAGE ZONES
# ==========================================================

ANCHORAGE_ZONES = {
    "Fujairah Anchorage": {
        "lat": 25.15,
        "lon": 56.40,
    },
    "Dubai / Jebel Ali": {
        "lat": 25.05,
        "lon": 55.05,
    },
    "Bandar Abbas": {
        "lat": 27.15,
        "lon": 56.30,
    },
}

# ==========================================================
# CRISIS TIMELINE
# ==========================================================

CRISIS_TIMELINE = [
    {
        "date": "2026-03-01",
        "event": "Regional military escalation",
        "severity": "high",
    },
    {
        "date": "2026-03-03",
        "event": "Shipping advisory issued",
        "severity": "medium",
    },
    {
        "date": "2026-03-06",
        "event": "Commercial vessels rerouted",
        "severity": "critical",
    },
]

# ==========================================================
# STRAIT POLYGON
# ==========================================================

STRAIT_DANGER_ZONE = [
    (26.85, 55.80),
    (26.85, 56.70),
    (26.10, 56.70),
    (26.10, 56.15),
]

# ==========================================================
# SCENARIO DATA
# ==========================================================

SCENARIOS = {
    "normal": {
        "risk": "LOW",
        "inbound": 188,
        "outbound": 181,
        "anchored": 28,
        "waiting": 9,
        "active": 352,
    },

    "limited": {
        "risk": "MEDIUM",
        "inbound": 118,
        "outbound": 112,
        "anchored": 54,
        "waiting": 31,
        "active": 301,
    },

    "conflict": {
        "risk": "HIGH",
        "inbound": 54,
        "outbound": 47,
        "anchored": 103,
        "waiting": 76,
        "active": 228,
    },

    "closed": {
        "risk": "CRITICAL",
        "inbound": 0,
        "outbound": 0,
        "anchored": 171,
        "waiting": 138,
        "active": 191,
    },
}

# ==========================================================
# CURRENT DEMO STATE
# ==========================================================

CURRENT_SCENARIO = "normal"

# ==========================================================
# SHIP TYPES
# ==========================================================

SHIP_TYPES = [
    "Tanker",
    "Cargo",
    "Container",
    "LNG Carrier",
    "Bulk Carrier",
]

FLAGS = [
    "Panama",
    "Liberia",
    "India",
    "Singapore",
    "Marshall Islands",
]

DESTINATIONS = [
    "Dubai",
    "Jebel Ali",
    "Fujairah",
    "Bandar Abbas",
    "Doha",
    "Mumbai",
]

# ==========================================================
# HELPERS
# ==========================================================

def set_demo_scenario(name: str):
    """
    Change the active demo scenario.
    """

    global CURRENT_SCENARIO

    if name in SCENARIOS:
        CURRENT_SCENARIO = name


def current():
    return SCENARIOS[CURRENT_SCENARIO]


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def random_ship():
    return {
        "mmsi": random.randint(100000000, 999999999),
        "ship_name": random.choice([
            "MT Horizon",
            "MV Ocean Star",
            "Pacific Trader",
            "Sea Falcon",
            "Arabian Pearl",
            "Blue Neptune",
            "Eastern Spirit",
        ]),
        "flag": random.choice(FLAGS),
        "destination": random.choice(DESTINATIONS),
        "ship_type": random.choice(SHIP_TYPES),
        "speed": round(random.uniform(8, 18), 1),
        "crossed_at": utc_now(),
    }


def get_ship_type_label(ship_type):
    """
    Compatibility function used by api.py.
    """

    return str(ship_type)

# ==========================================================
# MOCK ANALYTICS FUNCTIONS
# ==========================================================

async def get_transit_summary(hours: int = 24, gate: str | None = None):
    """
    Mock transit summary.
    """

    data = current()

    recent = []

    for _ in range(10):
        ship = random_ship()

        ship["direction"] = random.choice([
            "INBOUND",
            "OUTBOUND",
        ])

        ship["gate"] = "Strait of Hormuz"

        recent.append(ship)

    return {
        "hours": hours,
        "gate_filter": gate,
        "inbound": data["inbound"],
        "outbound": data["outbound"],
        "by_gate": {
            "Strait of Hormuz": {
                "inbound": data["inbound"],
                "outbound": data["outbound"],
            }
        },
        "recent_events": recent,
    }


async def get_hourly_transits(hours=48, gate=None):
    """
    Mock hourly chart.
    """

    base = current()

    chart = []

    for h in range(hours):
        chart.append(
            {
                "hour": f"{h:02d}:00",
                "inbound": max(
                    0,
                    int(base["inbound"] / hours)
                    + random.randint(-3, 3),
                ),
                "outbound": max(
                    0,
                    int(base["outbound"] / hours)
                    + random.randint(-3, 3),
                ),
            }
        )

    return chart


async def get_vessel_states():
    """
    Mock vessel state distribution.
    """

    data = current()

    anchored = data["anchored"]

    transiting = max(0, data["active"] - anchored - 42)

    return {
        "states": {
            "transiting": transiting,
            "anchored": anchored,
            "maneuvering": 26,
            "slow": 16,
            "unknown": 0,
        },
        "total": data["active"],
        "zone_counts": {
            "Fujairah Anchorage": anchored // 2,
            "Dubai / Jebel Ali": anchored // 3,
            "Bandar Abbas": anchored // 4,
        },
        "vessels_by_state": {},
    }


async def get_flag_distribution(hours: int = 24):
    """
    Mock vessel flags.
    """

    return [
        {"flag": "Panama", "vessels": 63},
        {"flag": "Liberia", "vessels": 51},
        {"flag": "India", "vessels": 39},
        {"flag": "Singapore", "vessels": 27},
        {"flag": "Marshall Islands", "vessels": 21},
    ]


async def get_destination_distribution(hours: int = 24):
    """
    Mock destinations.
    """

    return [
        {"destination": "Dubai", "vessels": 48},
        {"destination": "Jebel Ali", "vessels": 41},
        {"destination": "Fujairah", "vessels": 29},
        {"destination": "Bandar Abbas", "vessels": 19},
        {"destination": "Mumbai", "vessels": 14},
    ]


async def get_daily_summary():
    """
    Mock daily dashboard summary.
    """

    data = current()

    return {
        "generated_at": utc_now(),
        "total_records": 18420,
        "records_24h": 3418,
        "unique_vessels_24h": data["active"],
        "transits_24h": {
            "inbound": data["inbound"],
            "outbound": data["outbound"],
            "total": data["inbound"] + data["outbound"],
        },
        "vessel_states": {
            "transiting": data["active"] - data["anchored"],
            "anchored": data["anchored"],
            "maneuvering": 26,
            "slow": 16,
        },
        "anchorage_zones": {
            "Fujairah Anchorage": data["anchored"] // 2,
            "Dubai / Jebel Ali": data["anchored"] // 3,
            "Bandar Abbas": data["anchored"] // 4,
        },
    }

# ==========================================================
# DEMO UTILITIES
# ==========================================================

def randomize_demo():
    """
    Slightly randomize the current scenario values
    to make the dashboard look live.
    """

    data = SCENARIOS[CURRENT_SCENARIO]

    data["inbound"] = max(0, data["inbound"] + random.randint(-5, 5))
    data["outbound"] = max(0, data["outbound"] + random.randint(-5, 5))
    data["anchored"] = max(0, data["anchored"] + random.randint(-2, 2))
    data["waiting"] = max(0, data["waiting"] + random.randint(-2, 2))


async def heartbeat():
    """
    Background task that keeps changing the demo values.
    """

    while True:
        randomize_demo()
        await asyncio.sleep(30)


# ==========================================================
# MODULE TEST
# ==========================================================

if __name__ == "__main__":

    async def run_demo():

        print("\n========== MOCK MARITIME ANALYTICS ==========\n")

        print(await get_transit_summary())

        print(await get_hourly_transits())

        print(await get_vessel_states())

        print(await get_flag_distribution())

        print(await get_destination_distribution())

        print(await get_daily_summary())

        print(await get_blockade_indicators())

        print("\n=============================================\n")

    asyncio.run(run_demo())

async def get_blockade_indicators():
    data = current()

    ratio = round((data["anchored"] / data["active"]) * 100, 1)

    return {
        "active_vessels": data["active"],
        "anchored_vessels": data["anchored"],
        "anchored_ratio_pct": ratio,
        "waiting_fleet_6h": data["waiting"],
        "waiting_fleet_24h": max(0, data["waiting"] - 10),
        "strait_transits_24h": data["inbound"] + data["outbound"],
        "strait_status": CURRENT_SCENARIO.upper(),
        "situation": {
            "level": data["risk"],
            "title": f"{data['risk']} Risk",
            "text": "Demo maritime analytics generated from simulated data."
        },
        "fleet_by_type": [
            {"type": "Tanker", "count": 84},
            {"type": "Cargo", "count": 102},
            {"type": "Container", "count": 61},
        ],
        "fleet_by_flag": [
            {"flag": "Panama", "count": 58},
            {"flag": "Liberia", "count": 41},
            {"flag": "India", "count": 36},
        ],
    }

# ==========================================================
# SCENARIO HELPERS
# ==========================================================

def available_scenarios():
    """Return all available demo scenarios."""
    return list(SCENARIOS.keys())


def get_current_scenario():
    """Return the active demo scenario."""
    return CURRENT_SCENARIO


def set_demo_scenario(name: str):
    """Change the active demo scenario."""
    global CURRENT_SCENARIO

    if name in SCENARIOS:
        CURRENT_SCENARIO = name
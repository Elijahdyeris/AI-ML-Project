import json
import uuid
import random
from datetime import datetime, timedelta
import os

# Output file
output_path = "data/workflow_scenarios.json"
os.makedirs("data", exist_ok=True)

# Role and period options
roles = ["undergraduate", "graduate", "faculty", "admin", "research"]
periods = ["regular_term", "exam", "holiday", "registration"]
scenario_types = ["normal_transition", "role_specific", "attack"]
services = ["lms", "email", "sis", "research_db"]

def rand_time(start):
    return (start + timedelta(minutes=random.randint(0, 120))).isoformat()

def create_scenario(scenario_type):
    base_time = datetime(2023, 12, 1, 9, 0)
    user_id = f"user_{uuid.uuid4().hex[:12]}"
    role = random.choice(roles)
    period = random.choice(periods)

    if scenario_type == "normal_transition":
        subtype = "semester_end"
        description = f"{role} accessing services at end of term"
        outcome = "accept"
    elif scenario_type == "role_specific":
        subtype = "grading"
        description = f"{role} performing workload-intensive tasks"
        outcome = "accept"
    else:
        subtype = "credential_theft"
        description = f"Simulated unauthorized access for {role}"
        outcome = "reject"

    scenario = {
        "scenario_id": f"scen_{uuid.uuid4().hex[:12]}",
        "scenario_type": scenario_type,
        "scenario_subtype": subtype,
        "role_category": role,
        "description": description,
        "authentication_events": [
            {
                "event_id": f"auth_{uuid.uuid4().hex[:12]}",
                "timestamp": rand_time(base_time),
                "device_type": random.choice(["laptop", "mobile"]),
                "location_type": random.choice(["on_campus", "off_campus"]),
                "service_accessed": random.choice(services),
                "success": outcome == "accept"
            }
        ],
        "behavioral_data": [
            {
                "session_id": f"sess_{uuid.uuid4().hex[:12]}",
                "keystroke_features": {
                    "avg_key_dwell_time": round(random.uniform(85, 125), 1),
                    "typing_speed": round(random.uniform(60, 90), 1)
                },
                "app_transition_sequence": [
                    {"from": "email", "to": "lms", "timestamp": int(datetime.now().timestamp())},
                    {"from": "lms", "to": "sis", "timestamp": int(datetime.now().timestamp()) + 60}
                ]
            }
        ],
        "expected_outcome": outcome,
        "context_factors": {
            "academic_calendar_period": period,
            "time_pressure_level": random.choice(["low", "medium", "high"])
        }
    }

    return scenario

# Generate 150 scenarios
scenarios = (
    [create_scenario("normal_transition") for _ in range(60)] +
    [create_scenario("role_specific") for _ in range(60)] +
    [create_scenario("attack") for _ in range(30)]
)

# Save to file
with open(output_path, "w") as f:
    json.dump(scenarios, f, indent=2)

print(f"✅ Generated 150 academic workflow scenarios → {output_path}")

import json, random, uuid
from datetime import datetime, timedelta

with open("data/uald.json") as f:
    uald = json.load(f)

# Select a subset of user IDs and academic periods from uald.json
user_periods = [(entry["anonymous_user_id"], entry["academic_period"]) for entry in uald]
user_periods = random.sample(user_periods, min(1000, len(user_periods)))  # Sample 1,000 pairs

roles = ["undergraduate", "graduate", "faculty", "admin", "research"]
devices = ["laptop", "desktop", "tablet", "mobile"]

def generate_behavior(user_id, academic_period):
    return {
        "session_id": f"sess_{uuid.uuid4().hex[:12]}",
        "anonymous_user_id": user_id,
        "start_time": datetime.now().isoformat(),
        "end_time": (datetime.now() + timedelta(minutes=random.randint(30, 90))).isoformat(),
        "role_category": random.choice(roles),
        "device_type": random.choice(devices),
        "keystroke_features": {
            "avg_key_dwell_time": round(random.uniform(80, 120), 2),
            "avg_digraph_time": round(random.uniform(150, 250), 2),
            "keystroke_rhythm_variance": round(random.uniform(20, 60), 2),
            "typing_speed": round(random.uniform(40, 90), 2),
            "pause_frequency": round(random.uniform(0.05, 0.3), 3),
            "flight_time_consistency": round(random.uniform(0.7, 0.95), 3)
        },
        "mouse_features": {
            "avg_movement_speed": round(random.uniform(300, 600), 2),
            "avg_click_duration": round(random.uniform(100, 180), 2),
            "direction_change_frequency": round(random.uniform(0.1, 0.4), 3),
            "curvature_metric": round(random.uniform(0.2, 0.6), 3)
        },
        "app_transition_sequence": [
            {"from": "browser", "to": "email", "timestamp": int(datetime.now().timestamp())},
            {"from": "email", "to": "lms", "timestamp": int(datetime.now().timestamp()) + 100},
        ],
        "academic_period": academic_period,
        "primary_activity": random.choice(["coursework", "grading", "research"])
    }

data = [generate_behavior(user_id, period) for user_id, period in user_periods]

with open("data/abbd.json", "w") as f:
    json.dump(data, f, indent=2)
print("✅ Generated abbd.json with user IDs from uald.json")
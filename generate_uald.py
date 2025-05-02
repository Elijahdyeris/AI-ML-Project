import json, random
from datetime import datetime, timedelta
import uuid

roles = ["undergraduate", "graduate", "faculty", "admin", "research"]
locations = ["library", "lab", "dorm", "admin_office", "classroom"]
devices = ["laptop", "desktop", "tablet", "mobile"]
methods = ["password", "otp", "fingerprint", "faceid"]
services = ["lms", "email", "sis", "research_db"]
browsers = ["Chrome", "Firefox", "Edge"]
oses = ["Windows 10", "macOS 12.6.1", "Linux"]

def random_time():
    start = datetime(2022, 9, 1)
    return (start + timedelta(seconds=random.randint(0, 365*24*3600))).isoformat()

def generate_entry():
    return {
        "event_id": f"auth_{uuid.uuid4().hex[:12]}",
        "timestamp": random_time(),
        "anonymous_user_id": f"user_{uuid.uuid4().hex[:12]}",
        "role_category": random.choice(roles),
        "device_type": random.choice(devices),
        "device_id": f"dev_{uuid.uuid4().hex[:12]}",
        "auth_method": random.choice(methods),
        "location_type": random.choice(["on_campus", "off_campus"]),
        "campus_zone": random.choice(locations),
        "network_type": random.choice(["campus_wifi", "public_wifi", "vpn"]),
        "ip_hash": f"ip_{uuid.uuid4().hex[:8]}",
        "service_accessed": random.choice(services),
        "success": random.choice([True]*9 + [False]),
        "failure_reason": None,
        "session_duration": random.randint(5, 120),
        "academic_period": random.choice(["regular_term", "exam", "holiday"]),
        "client_browser": random.choice(browsers),
        "client_os": random.choice(oses)
    }

data = [generate_entry() for _ in range(10000)]

with open("data/uald.json", "w") as f:
    json.dump(data, f, indent=2)

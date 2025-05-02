# save_shared_users.py
import json
import uuid
import os

os.makedirs("data", exist_ok=True)

user_ids = [f"user_{uuid.uuid4().hex[:12]}" for _ in range(1000)]
with open("data/shared_users.json", "w") as f:
    json.dump(user_ids, f)

print("✅ Shared user IDs saved to data/shared_users.json")

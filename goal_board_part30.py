# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GoalBoard
import json, os


def load_profiles():
    with open("profiles.json", "r") as f:
        return json.load(f)


def save_profiles(profiles):
    os.makedirs("data", exist_ok=True)
    with open("data/profiles.json", "w") as f:
        json.dump(profiles, f, indent=2)


class UserProfile:
    def __init__(self, username, role="member"):
        self.username = username
        self.role = role

    def to_dict(self):
        return {"username": self.username, "role": self.role}

    @classmethod
    def from_dict(cls, d):
        return cls(d["username"], d.get("role", "member"))


def add_user(username="guest", role="viewer"):
    profiles = load_profiles()
    if username not in [p["username"] for p in profiles]:
        profiles.append(UserProfile(username, role).to_dict())
        save_profiles(profiles)
        print(f"User '{username}' added with role: {role}")


def list_users():
    profiles = load_profiles()
    return "\n".join([f"{p['username']} ({p['role']})" for p in profiles])


def switch_user(username="guest"):
    if username == "guest":
        print("Switching to guest mode.")
    else:
        users = load_profiles()
        user = next((u for u in users if u["username"] == username), None)
        if not user:
            add_user(username, "member")


def run():
    while True:
        print("\n--- GoalBoard User Management ---")
        cmd = input("(1) Add user  (2) List users  (3) Switch user  (4) Exit ").strip()
        if cmd == "1":
            u = input("Username: ").strip() or "guest"
            r = input("Role (viewer/member/owner): ").strip() or "viewer"
            add_user(u, r)
        elif cmd == "2":
            print(list_users())
        elif cmd == "3":
            switch_user(input("Username: ").strip() or "guest")
        elif cmd == "4":
            break

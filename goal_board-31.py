# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GoalBoard
class ActiveProfileManager:
    def __init__(self, profiles_db):
        self.profiles_db = profiles_db
    
    def get_active_profile(self):
        return self.profiles_db.get("active_profile", None)
    
    def set_active_profile(self, profile_name):
        if profile_name not in self.profiles_db["profiles"]:
            raise ValueError(f"Профиль '{profile_name}' не найден")
        self.profiles_db["active_profile"] = profile_name
    
    def list_profiles(self):
        return [p for p in self.profiles_db["profiles"].values() if p.get("active", False) is False]

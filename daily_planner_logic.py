class UserProfile:
    def __init__(self):
        self.name = ""
        self.goals = []
        self.preferences = {
            "theme": "default",
            "font_size": 12,
            "color_scheme": "light"
        }
        self.tasks = [{"name": "", "due_date": ""}]
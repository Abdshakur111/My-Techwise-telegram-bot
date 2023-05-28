# database.py
import json

class Database:
    def __init__(self, users_file, issues_file):
        self.users_file = users_file
        self.issues_file = issues_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users_data = json.load(file)
        except FileNotFoundError:
            self.users_data = {'users': []}

        try:
            with open(self.issues_file, 'r') as file:
                self.issues_data = json.load(file)
        except FileNotFoundError:
            self.issues_data = {'issues': []}

    def save_data(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users_data, file, indent=4)

        with open(self.issues_file, 'w') as file:
            json.dump(self.issues_data, file, indent=4)

    def user_exists(self, user_id):
        return any(user['id'] == user_id for user in self.users_data['users'])

    def register_user(self, user_id):
        self.users_data['users'].append({'id': user_id, 'tracking_id': None})
        self.save_data()

    def set_tracking_id(self, user_id, tracking_id):
        for user in self.users_data['users']:
            if user['id'] == user_id:
                user['tracking_id'] = tracking_id
                break
        self.save_data()

    def get_tracking_id(self, user_id):
        for user in self.users_data['users']:
            if user['id'] == user_id:
                return user['tracking_id']
        return None

    def report_issue(self, user_id, issue_text):
        self.issues_data['issues'].append({'user_id': user_id, 'issue_text': issue_text})
        self.save_data()

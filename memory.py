class InterviewMemory:
    def __init__(self):
        self.sessions = {}  # Dictionary to hold interview sessions

    def get(self, session_id):
        return self.sessions.get(session_id)
    
    def save(self, session_id, session_data):
        self.sessions[session_id] = session_data
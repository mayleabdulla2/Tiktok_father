from config import SESSION_FILE

def load_sessions():
    with open(SESSION_FILE, 'r') as f:
        return [line.strip() for line in f]
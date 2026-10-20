from config import PROXY_FILE

def load_proxies():
    with open(PROXY_FILE, 'r') as f:
        return [line.strip() for line in f]
import requests

def send_fake_report(target, proxy, session):
    url = f'https://example.com/report/{target}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Session': session,
        'Tags': 'system software, education'
    }
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    data = {
        'reason': 'spam',
        'details': 'This user is spamming the group.'
    }
    response = requests.post(url, headers=headers, proxies=proxies, data=data)
    if response.status_code == 200:
        print(f'Report sent to {target} using proxy {proxy}')
    else:
        print(f'Failed to send report to {target} using proxy {proxy}')
import requests 

repo = 'venky0712/python'
branch = 'master'
access_token = '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'

r = requests.put(
    'https://api.github.com/repos/{0}/branches/{1}/protection'.format(repo, branch),
    headers = {
        'Accept': 'application/vnd.github.luke-cage-preview+json',
        'Authorization': 'Token {0}'.format(access_token)
    },
    json = {
        "restrictions": {
            "users": [
              "venky0712"
            ]
        },
        "required_status_checks": None,
        "enforce_admins": None,
        "required_pull_request_reviews": None
    }
)
print(r.status_code)
print(r.json())
import requests
from bs4 import BeautifulSoup

def get_readme_info(name : str):
    url = f"https://raw.githubusercontent.com/{name}/{name}/refs/heads/master/README.md"
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
    elif res.status_code == 404:
        url = f"https://raw.githubusercontent.com/{name}/{name}/refs/heads/main/README.md"
        res = requests.get(url)
        if res.status_code == 404:
            url = f"https://raw.githubusercontent.com/{name}/{name}/refs/heads/master/readme.md"
            res = requests.get(url)
            if res.status_code == 404:
                url = f"https://raw.githubusercontent.com/{name}/{name}/refs/heads/main/readme.md"
                res = requests.get(url)

    else:
        return None
    print(res.text.strip())
    return res.text.strip()

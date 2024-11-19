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

#https://github.com/pdh0128?tab=repositories
#https://github.com/leegunwoooo?tab=repositories
def get_reponame(name : str):
    url = f"https://github.com/{name}?tab=repositories"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    res = soup.find_all("h3", class_="wb-break-all")
    repo_names = []
    for item in res:
        item = item.find('a')
        item_text = item.text.strip()
        if item_text != name:
            repo_names.append(item_text)
    print(repo_names)
    return repo_names

def get_repo_content(name :str, repo_name : str):
    url = f"https://raw.githubusercontent.com/{name}/{repo_name}/refs/heads/master/README.md"
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
    elif res.status_code == 404:
        url = f"https://raw.githubusercontent.com/{name}/{repo_name}/refs/heads/main/README.md"
        res = requests.get(url)
        if res.status_code == 404:
            url = f"https://raw.githubusercontent.com/{name}/{repo_name}/refs/heads/master/readme.md"
            res = requests.get(url)
            if res.status_code == 404:
                url = f"https://raw.githubusercontent.com/{name}/{repo_name}/refs/heads/main/reademe.md"
                res = requests.get(url)
    else:
        return None

    if res.text.strip() == "404: Not Found":
        return None

    print(res.text.strip())
    return res.text.strip()

if __name__ == '__main__':
    name = "pdh0128"
    repo_name = get_reponame(name)
    for repo_name in repo_name:
        repo = get_repo_content(name, repo_name)
        print(repo)

#https://raw.githubusercontent.com/BitByte08/rhythm/refs/heads/master/readme.md
#https://github.com/BitByte08/rhythm
import requests


OWNER = "sefineh-ai"
REPO = "Neo4j"
BRANCH = "main"
FOLDER_PATH = "data"

def get_file_urls(owner, repo, branch, folder_path):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}?ref={branch}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        files = response.json()
        raw_urls = [
            f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file['path']}"
            for file in files if file['type'] == 'file'
        ]
        return raw_urls
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
        return []

urls = get_file_urls(OWNER, REPO, BRANCH, FOLDER_PATH)
print(urls)
with open("urls.txt", "w") as file:
    for url in urls:
        file.write(url+"\n")

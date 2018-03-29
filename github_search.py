import requests

def get_name():
    print("请输入你所需要查询的信息用\" \"分割开:")
    names = input().split(" ")
    return names

def check_name(names):
    repo_api = 'https://api.github.com/search/repositories?q='
    topic_api = 'https://api.github.com/search/repositories?q=topic:'
    data = []
    for name in names:
        repo_info = requests.get(repo_api+name).json()['items'][0]
        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']
        topic = requests.get(topic_api+name).json()['total_count']
        temp = {'name':name,'stars':stars,'forks':forks,'topic':topic}
        data.append(temp)
    return data
name = get_name()
info = check_name(name)
print(info)
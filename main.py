import requests
import pprint

print('GET google.com')
response = requests.get('https://www.google.com')
print(response.status_code)
# print(response.text)
print('*******')

print('GET api.github.com')
params = {
    'q' : 'python'
}
response=requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()
print(f"Статус код запроса по Python: {response.status_code}")
print(f"Репозиториев Python: {response_json['total_count']}")
#pprint.pprint(response_json)

params = {
    'q' : 'html'
}
response=requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()
# pprint.pprint(response_json)
print(f"Статус код запроса по HTML: {response.status_code}")
print(f"Репозиториев HTML: {response_json['total_count']}")
pprint.pprint(response_json)
print('*******')

print('GET jsonplaceholder.typicode.com')
params = {
    'userId' : '1'
}
response=requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
response_json = response.json()
print(f"Статус код запроса: {response.status_code}")
pprint.pprint(response_json)
print('*******')

print('POST jsonplaceholder.typicode.com')
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title" : "foo",
    "body" : "bar",
    "userId" : 1
}
response = requests.post(url, data=data)
print(response.status_code)
print (f"ответ - {response.json()}")

print('*******')
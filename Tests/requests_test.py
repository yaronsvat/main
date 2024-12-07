import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.status_code)
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
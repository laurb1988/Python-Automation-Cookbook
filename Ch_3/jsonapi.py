import requests

results = requests.get('http://jsonplaceholder.typicode.com/posts/')
print(results)
print(len(results.json()))
new_post = {'userId':10, 'title':'a title', 'body':'something something'}
results = requests.post('http://jsonplaceholder.typicode.com/posts/', json=new_post)
print(results)
print(results.json())
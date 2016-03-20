import requests

url = 'http://img13.360buyimg.com/n0/jfs/t1156/242/321554758/55334/6c899912/5518ad98Nce49110e.jpg'
r = requests.get(url).content
print r
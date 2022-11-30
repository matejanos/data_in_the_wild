import pandas as pd
# import requests
import os
import urllib.request


posts = pd.read_csv('test.csv')
links = posts.url
#print(links)

dir = 'images'

path = os.getcwd()
path = os.path.join(path, dir)
os.mkdir(path)

for index, row in posts.iterrows():
    #print(row['url'], row['user_id'])
    filename = f"{row['user_id']}.jpg"
    urllib.request.urlretrieve(row['url'], f"{path}/{filename}")
    print(filename)

# f = open('test2.jpg','wb')
# f.write(requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Neymar_PSG.jpg/1200px-Neymar_PSG.jpg').content)
# f.close()
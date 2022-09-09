from proxy_rotator import *

urls = open("urls.txt").read().split()
proxies = open("list_proxy.txt").read().split()

items = {}

for url in urls:
    items[url] = 'none'

fetch_items(items, proxies)

with open("resulting_output.txt", "w") as file:
    for item in items:
        file.write('url: ' + str(item) + '\n'
         + 'output: ' + str(items[item]) + "\n\n")
import requests
import threading

def send_request(session, url, proxy):
    try:
        response = session.get(url,proxies={"http": proxy, "https": proxy})
        json = response.json()

        if not json:
            return 'none'

        return response.json()
    except:
        return 'none'

def count_items(items):
    cnt = 0

    for item in items:
        if items[item] == 'none' or items[item] == 'pending':
            cnt += 1

    return cnt

def fetch(session, url, proxy, items):
    items[url] = 'pending'
    result = send_request(session, url, proxy)
    items[url] = result

def fetch_items(items, proxies):
    while count_items(items) > 0:
        with requests.Session() as session:
            for proxy in proxies:
                cnt = 0

                for url in items:
                    if items[url] != 'none':
                        continue

                    request = threading.Thread(target=fetch, args=(session, url, proxy, items))
                    request.start()

                    cnt += 1
                    if cnt > 9:
                        break
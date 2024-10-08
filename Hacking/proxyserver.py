import requests

proxies = {
    "http": "206.233.166.71:58394",
    "https": "46.227.37.49:1088",
}

response = requests.get("http://google.com", proxies=proxies)
print(response.text)
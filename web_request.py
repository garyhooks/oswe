import requests
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}

r = requests.get("https://manageengine:8443/", verify=False, proxies=proxies)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.text)

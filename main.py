import json
import requests

# URL запрос
url = "https://storerocket.io/api/user/Yw8lg6ZJvo/locations?radius=250&units=miles"

# Заголовки запрос
headers = {
    "Authority": "storerocket.io",
    "Method": "GET",
    "Path": "/api/user/Yw8lg6ZJvo/locations?radius=250&units=miles",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "cookie" : 'XSRF-TOKEN=eyJpdiI6IkJESWUwQS96VkNEZVV0VGJzckFQQWc9PSIsInZhbHVlIjoiVHN4cjJLTlZLOW45dmtma0ZPQ0xOaEZLSGwwUGdKWGFIZmFpdm96NjNLUUxEMEtXTFhQVU1UVHo2L1JHeGE0RlpNSTlQeHpUUEMzQWNCc0FYTnBZZzZ0aGtNK1N1SGtFekEyNWFZSEZFWUg0REVRRWRuTHRyVEt6OVNzb3REWlIiLCJtYWMiOiI4OTEwM2QzMjA2MGZmOTk4Y2NkYWRiYzBlMmY1ZmNkNGVhMDU4N2MyYzU1ZDIzZjRlMTVjZWNjYTQxMzhmYjBlIiwidGFnIjoiIn0%3D; storerocket_session=eyJpdiI6IjlRTk5aV0VqdGVEbDUxa0pIR1lPc1E9PSIsInZhbHVlIjoiN0xHSVl1NUMzK044Tm5qUHhUaVJZc3VuWTVsMFRPaG5HdEVQbncwYXZybGpKSTc3VTFRbEVaVmZSZFRTdTcwTXRTd2dYcVAzRzM4QWFYWkVwSDZ2b0VTV3p6YjducVY3dDBPdWtod1Ftd00wSlVMOW1uekFiUVE1eHF6QXA3RFciLCJtYWMiOiI2MzQyNzJmN2VmNjU5ZDc5OGYxM2ZjNWZiNDA2M2EyNjQxNjY5YTYyZTA4NjViM2MzNGZiMDQ3NDM3NGU1OGEzIiwidGFnIjoiIn0%3D',
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}



response = requests.get(url, headers=headers)


if response.status_code == 200:
    # проверка формати чавоб
    if 'application/json' in response.headers.get('Content-Type'):
        # сохранит к\р чаво бо намуди json
        json_data = response.json()
        with open('dealer.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        print("JSon сохранит шуд")
    elif 'text/html' in response.headers.get('Content-Type'):
        # сохранит к\р чаво бо намуди html
        with open('dealer.html', 'w', encoding='utf-8') as html_file:
            html_file.write(response.text)
        print("Чаввоб бо формати html сохранит шуд.")
    else:
        print("формати файл муян карда нашуд:", response.headers.get('Content-Type'))
else:
    print(f"Error: status code  {response.status_code}")
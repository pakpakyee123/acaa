import requests

url = "https://arca.live/u/@하루/86785959"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print(r.text[:5000])

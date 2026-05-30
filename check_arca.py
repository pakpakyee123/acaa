import requests

url = "https://arca.live/b/commission"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print(r.status_code)
print(r.text[:3000])

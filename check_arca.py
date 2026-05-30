import os
import requests

webhook = os.environ["DISCORD_WEBHOOK"]

requests.post(
    webhook,
    json={"content": "GitHub Actions 테스트 성공"}
)

print("done")

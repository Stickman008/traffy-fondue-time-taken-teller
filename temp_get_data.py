import requests

url = "https://publicapi.traffy.in.th/dump-csv-chadchart/bangkok_traffy.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("data/bangkok_traffy.csv", "wb") as f:
        f.write(response.content)
    print("Data downloaded successfully.")
else:
    print(f"Failed to download data. Status code: {response.status_code}")

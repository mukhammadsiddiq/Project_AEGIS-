import requests


def detect_intrusion():
    url = input("Enter the URL to monitor: ")
    response = requests.get(url)
    if response.status_code == 200:
        print("No intrusion detected.")
    else:
        print("Intrusion detected!")

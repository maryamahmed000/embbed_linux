import requests

def suggest_activity():
    try:
        response = requests.get("https://www.boredapi.com/api/activity")
        if response.status_code == 200:
            data = response.json()
            activity = data.get("activity")
            if activity:
                print(f"Suggested Activity: {activity}")
            else:
                print("No activity suggestion available.")
        else:
            print("Failed to retrieve activity suggestion.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org/?format=json")
        if response.status_code == 200:
            data = response.json()
            public_ip = data.get("ip")
            if public_ip:
                print(f"Your Public IP Address: {public_ip}")
            else:
                print("Unable to retrieve public IP.")
        else:
            print("Failed to retrieve public IP.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def get_location():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            location = data.get("city")
            if location:
                print(f"Your Location: {location}")
            else:
                print("Unable to retrieve location.")
        else:
            print("Failed to retrieve location.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    suggest_activity()
    get_public_ip()
    get_location()

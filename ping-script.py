import requests
import time

def ping_web_app(url, max_retries=5, delay=5):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Success: Received 200 OK on attempt {attempt}")
                return True
            else:
                print(f"Attempt {attempt}: Received status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Attempt {attempt}: Error - {e}")
        
        if attempt < max_retries:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

    print("Failed to receive 200 OK after multiple attempts.")
    return False


web_app_url =  input("Enter the web app URL: ")
if not web_app_url.startswith("http://"):
    web_app_url = "http://" + web_app_url
ping_web_app(web_app_url)
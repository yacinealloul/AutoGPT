import requests
import time
import json

def get_discussion():
    url = 'http://127.0.0.1:8000/getDiscussion'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des discussions : {e}")
        return None
    
    return json.loads(response.text)

def main():
    url = 'http://127.0.0.1:8000'
    last_discussion = None
    polling_interval = 30.0

    while True:
        current_discussion = get_discussion()
        
        if current_discussion is not None and current_discussion != last_discussion:
            print(current_discussion)
            last_discussion = current_discussion
        
        time.sleep(polling_interval)

if __name__ == "__main__":
    main()

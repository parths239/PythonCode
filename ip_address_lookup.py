import urllib.request
import json

while True:
    ip = input("What is your target IP: ")
    
    if not ip:  # Exit if input is empty
        print("Exiting...")
        break
    
    url = f"http://ip-api.com/json/{ip}"
    
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        values = json.loads(data)
        
        if values["status"] == "fail":
            print("Invalid IP or request failed.")
        else:
            print(f"IP: {values['query']}")
            print(f"City: {values['city']}")
            print(f"ISP: {values['isp']}")
            print(f"Country: {values['country']}")
            print(f"Region: {values['region']}")
            print(f"Timezone: {values['timezone']}")
    
    except Exception as e:
        print(f"Error: {e}")

    break  # Exit after one iteration

import requests
import os


def fetch(key, apiKey):
    return requests.get(f"http://api.weatherapi.com/v1/current.json?key={apiKey}&q={key}&aqi=no")


def main():
    # Retrive APi key from APIKEY.env
    apiKey = os.getenv('APIKEY')

    while True:
        key = input("Enter a valid name of a city or airport code or 0 to exit: ")
        print()

        if key == "0":
            break

        try:
            response = fetch(key, apiKey)
            
            if response.status_code == 200:
                data = response.json()
                print(f"Current temperature in {data['location']['name']}, {data['location']['region']}, {data['location']['country']} is {data['current']['temp_c']}°C")
                print(f"Feels like: {data['current']['feelslike_c']}°C")
                print(f"Current weather condition: {data['current']['condition']['text']}\n")

            else:
                print("Invalid city or data not found.\n")

        except requests.RequestException as e:
            print(f"Request error: {e}")


if __name__ == "__main__":
    main()

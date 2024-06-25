from typing import Any
import requests


def Fetch_Weather(place: str) -> dict[Any, Any]:
    try:
        # Making the user input usable to the API or url
        place = str(place.lower().replace(" ", "%20", -1))
        API_KEY = "YOUR API KEY"
        # Getting the response from the API
        response = requests.request("GET",
                                    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{place}/today?unitGroup=metric&key={API_KEY}&contentType=json")
        if response.status_code != 200:
            # If the API failed to fetch the data show the user an error
            return dict({
                "DateAndTime": "API ERROR, TRY LATER",
                "Temperature": "API ERROR, TRY LATER",
                "Humidity": "API ERROR, TRY LATER",
                "Sunrise": "API ERROR, TRY LATER",
                "Sunset": "API ERROR, TRY LATER",
                "Conditions": "API ERROR , TRY LATER"
            })

        # Parse the results as JSON
        jsonData = response.json()
        # Getting the latest data
        DATASET = jsonData["days"][0]
        # Returning as a dictionary for easier access
        return dict({
            "DateAndTime": DATASET["datetime"],
            "Temperature": DATASET["temp"],
            "Humidity": DATASET["humidity"],
            "Sunrise": DATASET["sunrise"],
            "Sunset": DATASET["sunset"],
            "Conditions": DATASET["conditions"]
        })
    # If the user doesn't have WI-FI connection then show an error
    except requests.ConnectionError:
        return dict({
            "DateAndTime": "CONNECTION LOST",
            "Temperature": "CONNECTION LOST",
            "Humidity": "CONNECTION LOST",
            "Sunrise": "CONNECTION LOST",
            "Sunset": "CONNECTION LOST",
            "Conditions": "CONNECTION LOST"
        })

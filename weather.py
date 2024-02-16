# importing requests library
import requests as rq

# API key
api_key = '30d4741c779ba94c470ca1f63045390a'

#Taking the City from user and storing it in a variable user_input_city
user_input_city = input("Please enter the city \n")

# Fetch weather data from OpenWeatherMap API  
weather_data = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input_city}&units=imperial&APPID={api_key}")

# Print new lines for better formatting
print("\n\n")

# Print HTTP status code
print(weather_data.status_code)

# Condition checking 
if weather_data.status_code==404:

     print(f"City :{user_input_city} not found")

else:
     # Print raw JSON response
     print(weather_data.json())

     # Extract weather information from JSON response
     weather = weather_data.json()["weather"][0]["main"]
     temperature = round(weather_data.json()["main"]["temp"])
     sunrise = weather_data.json()["sys"]["sunrise"]
     sunset = weather_data.json()["sys"]["sunset"]

     # Display weather details
     print(f"Weather at {user_input_city} is : {weather}")
     print(f"Temperature in {user_input_city} is : {temperature}")
     print(f"Sunrise : {sunrise}")
     print(f"Sunset : {sunset}")
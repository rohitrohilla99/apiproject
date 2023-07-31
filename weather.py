import requests,json
apikey="07d7fbb973b1b48f10b7ff42dc3d30bc"
city_name=input("Enter the city name:")
temperature_data=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={apikey}")
b=temperature_data.json()["main"]["temp"]
temp=b-273.15
temp = round(temp,2);
if(temperature_data.json()['cod']=='404'):
    print("invalid data")
else:
    print(f"the temperature in {city_name} is:{temp}°C")


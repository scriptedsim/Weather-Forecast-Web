import requests

APIkey = "5d45c1cdebf7f04b2204285c20094ca3"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json() 
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data
    
if __name__=="__main__":
    print(get_data("Tokyo", forecast_days=5))
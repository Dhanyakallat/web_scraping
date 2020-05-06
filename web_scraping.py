import requests
import pandas as pd
from bs4 import BeautifulSoup

def read_web_page():
    page = requests.get('https://www.knmi.nl/nederland-nu/weer/verwachtingen')
    soup = BeautifulSoup(page.content,'html.parser')
    week = soup.find(id = 'weather')
    element = week.find(class_ = 'weather-map__table is-fullwidth')
    return(element)

def extract_web_value(element):
    accu_container = element.find_all(['li'])
    days_content      = []
    date_content      = []
    max_temp_content  = []
    min_temp_content  = []
    for i in range(6):
        extract_data = accu_container[i].get_text()
        data_split = extract_data.split()
        days_content.append(data_split[0])
        date_content.append(data_split[1])
        max_temp_content.append(data_split[3])
        min_temp_content.append(data_split[5])
    return days_content,date_content,max_temp_content,min_temp_content

def create_df(days_content,date_content,max_temp_content,min_temp_content):
    weather_forecast_df = pd.DataFrame(
         {'days': days_content,
         'date': date_content,
         'max_temp': max_temp_content,
         'min_temp': min_temp_content})
    return(weather_forecast_df)

def write_output(weather_forecast_df):
   print(weather_forecast_df)
   # weather_forecast_df.to_csv('weather_data')


 
element = read_web_page()
days_content,date_content,max_temp_content,min_temp_content = extract_web_value(element)
weather_forecast_df = create_df(days_content,date_content,max_temp_content,min_temp_content)
write_output(weather_forecast_df)


from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time

#get date info
now = datetime.now()
date = now.strftime("%d-%m-%Y")
dmy = date
ttime = now.strftime("%H:%M:%S")
date = date + " " + ttime

def newCity(city):
    try:
        cityWebSite = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
        driver = webdriver.Chrome()
        print(f'{city} weather forecast website is opening...\n')
        driver.get(cityWebSite)
        cityWeatherElement = driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[2]/div/table/thead/tr[1]/td[1]")
        cityWeather = cityWeatherElement.text
        print(f'{city} weather forecast:\n {cityWeather} \n')
        desktop_path = '/Users/eneskaragoz/Desktop/python/weatherForecast/'
        file_path = f'{desktop_path}/' + dmy + '_' +  city + 'Weather.txt'

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f'{city}Weather Forecast Info: ({date}):\n')
            file.write(cityWeather)
            file.write('\n')

    except NoSuchElementException:
        print(f'\nError: Invalid city name {city}, please try again...\n')

driver = webdriver.Chrome()
#weather forecast website for new york
print("new york weather forecast website is opening...")
driver.get("https://weather.com/weather/today/l/a496cfcba367ffae60ccfdc94e31bcf3d0a12ac6515336dbd274f381a932abbc")

#get weather forecast by class name
newYorkWeatherElement = driver.find_element(By.CLASS_NAME, "CurrentConditions--tempValue--MHmYY")
newYorkWeather = newYorkWeatherElement.text
degreeElement = driver.find_element(By.CLASS_NAME, "LanguageSelector--unitDisplay--mr3Rx")
degree = degreeElement.text
if "F" in degree:
    newYorkWeather = newYorkWeather + " Fahrenheit"
elif "C" in degree:
    newYorkWeather = newYorkWeather + "Celcius"

print(f'\nNew York weather forecast: {newYorkWeather} \n')
    #close chrome driver
driver.quit()       

time.sleep(3)

driver = webdriver.Chrome()
#weather forecast website for istanbul
print("istanbul weather forecast website is opening...")
driver.get("https://weather.com/weather/today/l/7912d03017522301f5c89f4f1d661d18ad10926c15063cf520ee5ec7ce7c787c")

#get weather forecast by xpath
istanbulWeatherElement = driver.find_element(By.XPATH, "//*[@id=\"WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a\"]/div/section/div/div/div[2]/div[1]/div[1]/span")
istanbulWeather = istanbulWeatherElement.text
degreeElement = driver.find_element(By.CLASS_NAME, "LanguageSelector--unitDisplay--mr3Rx")
degree = degreeElement.text
if "F" in degree:
    istanbulWeather = istanbulWeather + " Fahrenheit"
elif "C" in degree:
    istanbulWeather = istanbulWeather + "Celcius"
print(f'Istanbul weather forecast: {istanbulWeather} \n')
# close chrome driver
driver.quit()

# save info to the text file
#destination path
desktop_path = '/Users/eneskaragoz/Desktop/python/weatherForecast/'
file_path = f'{desktop_path}/weatherForecastInfo.txt'

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(f'New York Weather Forecast Info: ({date}):\n')
    file.write(newYorkWeather)
    file.write('\n')
    file.write(f'İstanbul Weather Forecast Info: ({date}):\n')
    file.write(istanbulWeather)

print(f'saved file path: {file_path}')

j = True

while j == True:
    answer = input("\ndo you want to search for another city? y/n \n")
    if answer == "y":
        city = input("which city do you want to search?\n")
        newCity(city)
    elif answer == "n":
        i = 0
        j = False
        print("\nok then, see you soon :)")
    else:
        print("\nwrong choice, please try again...\n")

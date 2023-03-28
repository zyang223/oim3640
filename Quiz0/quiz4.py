"""
-------------------------------------------------------------------------------
Q1. Please complete the following function to use your APIKEY to retrieve the current wind speed from OpenWeatherMap.

If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below, but you will lose 10 points.
MyAPIKEY = '756b1938810423b43e6ac1212d9d40fc'
-------------------------------------------------------------------------------
"""
import urllib.request
import json
import pprint


def get_wind_speed(city: str, country: str) -> float:
    """
    Returns the current wind speed in meters per second for the given city from OpenWeatherMap.

    Parameters:
    city -- the name of the city (str)
    country -- the two-letter country code for the city (str)
    """
    APIKEY="756b1938810423b43e6ac1212d9d40fc"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={APIKEY}"
    f=urllib.request.urlopen(url)
    response_text= f.read().decode("utf-8")
    response_data=json.loads(response_text)
    pprint.pprint(response_data)    
    wind_speed=(response_data["wind"]["speed"])
    print(f"The wind speed of {city} is {wind_speed}")
    
get_wind_speed("new+york","us")

# When you've completed your function, uncomment the following lines and run this file to test.

# print(get_wind_speed('wellesley', 'us')) # you can replace the arguments with your hometown city and country code. If there are two (or more) words in the city name, you need to add '+' or '%20' between words, i.e. if you are from New York, the first arugment should be converted to "new+york" or "new%20york".

## Expected output - of course the wind speed in your hometown might be different:
# 12.0


"""
-------------------------------------------------------------------------------
Q2. There are 351 towns/cities in Massachusetts according to 2020 Census. An API (http://107.173.19.148:81/mass) returns JSON data of all town names (and other information). Please complete the function that returns the town name list. This list should be sorted alphabetically.

Notice: for the following questions, you may create additional helper function(s) if needed. If you create additional function(s), you are allowed to change the given function(s) by adding necessary parameter(s).
-------------------------------------------------------------------------------
"""


def get_town_names() -> list:
    town_names=[]
    """
    Returns a sorted list of town names
    """
    url="http://107.173.19.148:81/mass"
    f=urllib.request.urlopen(url)
    response_text= f.read().decode("utf-8")
    response_data=json.loads(response_text)
    pprint.pprint(response_data)
    for town in response_data["data"]:
        town_names.append(town["name"])
        town_names.sort()
    return town_names
print(get_town_names())


## When you've completed your function, uncomment the following lines and run this file to test!
# names = get_town_names()
# print(type(names), len(names))
# print(names)

## Expected output:
## <class 'list'> 351
## ['Abington', 'Acton', 'Acushnet', 'Adams', 'Agawam', 'Alford', 'Amesbury', 'Amherst', ..., 'Yarmouth']


"""
-------------------------------------------------------------------------------
Q3. Which town/city is the largest by population in Massachusetts? Of course it is Boston. But do you know which town is the smallest? Please complete the function that returns the town's name that has the smallest population in Massachusetts.
-------------------------------------------------------------------------------
"""


def get_smallest_town() -> str:
    """
    Returns the town's name that has the smallest population
    """
    smallaest_town=[]
    url="http://107.173.19.148:81/mass"
    f=urllib.request.urlopen(url)
    response_text= f.read().decode("utf-8")
    response_data=json.loads(response_text)
    smallaest_town=response_data["data"][0]
    for town in response_data["data"]:
       if town["population"]<smallaest_town["population"]:
        smallaest_town=town
    return smallaest_town["name"]
print(get_smallest_town())


## When you've completed your function, uncomment the following lines and run this file to test!
# smallest = get_smallest_town()
# print(smallest)

## Expected output:
## Gosnold # There are only 70 people in that town based on 2020 Census.

"""
-------------------------------------------------------------------------------
Q4. You may have noticed you are the mayor of one or several towns in Massachusetts. Please complete the function that returns a dictionary - in this dictionary, key is mayor's name and value is a list of town names that the mayor is managing. You can find example from the expected output below.
-------------------------------------------------------------------------------
"""


def get_mayor_dict() -> dict:
    """
    Returns a dictionary that maps mayors to their towns, {str: list}
    """


## When you've completed your function, uncomment the following lines and run this file to test!
# mayor_dict = get_mayor_dict()
# print(mayor_dict['Naomi']) # You can replace Naomi with your own name, but the output would be different.

## Expected output - it is ok if the order is different:
## ['Dunstable', 'East Longmeadow', 'Erving', 'Lexington', 'Southwick', 'Walpole', 'Wareham', 'Wellesley'] # The towns that Mayor Naomi is managing.


"""
-------------------------------------------------------------------------------
Q5. Have you wondered how many people you are managing? Please complete the function that returns a list of all the mayor names sorted by the total population they are managing from most to least. You can find example from the expected output below.
-------------------------------------------------------------------------------
"""


def sort_mayors() -> list:
    """
    Returns a list that shows the mayor names sorted by the total population
    they are managing from most to least.
    """


## When you've completed your function, uncomment the following lines and run this file to test!
# sorted_mayor_list = sort_mayors()
# print(sorted_mayor_list) # Keydell is the busiest mayor because he manages almost 880K people.

## Expected output:
## ['Keydell', 'Eva', 'Caitlin', 'Alexander', 'Xiaolun', 'Abir', 'Rich', 'Pengru', 'Alice', 'Lilly', 'Matthew', 'Luke', 'Xue-Zhen', 'Sergio', 'Jacob', 'Lindsey', 'John', 'Siyuan', 'Matteo', 'Gina', 'Angela', 'Naomi', 'Harveen', 'Jai', 'Abby', 'Anika', 'Kimberly', 'Charlotte', 'Jason', 'Max', 'Katarina', 'Lily', 'XiuJie', 'Zide', 'Lillian', 'Michael', 'Choying', 'Bidhi', 'James']
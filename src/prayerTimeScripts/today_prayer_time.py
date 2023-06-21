import requests
import pyfiglet
import datetime
from tabulate import tabulate


class Location:
    country_code = 'BH'
    country_city = 'Sanad'
    latitude = 26.1501874
    longitude = 50.5841248


def prayer_call_request(today_date,
                        latitude,
                        longitude):
    parameters = {
        'latitude': latitude,
        'longitude': longitude,
        'method': 0
    }

    api_call = requests.get(f"http://api.aladhan.com/v1/timings/{today_date}", params=parameters)

    response_object = dict(api_call.json())
    timing_data = response_object.get("data")
    timing_list = timing_data.get("timings")

    return timing_list


def today_date():
    current_date_time = datetime.datetime.today()
    current_date = current_date_time.strftime("%d-%m-%Y")
    print(f"Today's Date: {current_date}")
    return current_date


def terminal_art():
    script_title = pyfiglet.figlet_format("Today's Prayer Times", font="slant")
    print(script_title)


def timing_parse_function(time_data):
    parsed_time_data = list(zip(time_data.keys(), time_data.values()))
    return parsed_time_data


def prayer_time_table(parsed_prayer_time):
    tabulated_list = tabulate(parsed_prayer_time,
                              showindex="always",
                              tablefmt="heavy_outline",
                              headers=["Prayer", "Time"])
    print(tabulated_list)


def main():
    terminal_art()
    today_prayer_time = prayer_call_request(today_date(), Location.latitude, Location.longitude)
    prayer_time_table(timing_parse_function(today_prayer_time))


if __name__ == "__main__":
    main()

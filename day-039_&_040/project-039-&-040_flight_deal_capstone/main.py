# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
import data_manager
import flight_search
import flight_data
import notification_manager


def get_config_line(line_num):  # Get contents of a given line in .config
    try:
        with open('day-039_&_040/project-039-&-040_flight_deal_capstone/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    os.environ["SHEET_ENDPOINT"] = get_config_line(0)

    data_manager_obj = data_manager.DataManager()
    flight_search_obj = flight_search.FlightSearch()

    sheet_data = data_manager_obj.sheety_get().json()
    for row in sheet_data["prices"]:
        if row["iataCode"] == "":
            row["iataCode"] = flight_search_obj.get_iata_code(row["city"])
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            data_manager_obj.sheety_put(row["id"], new_data)


if __name__ == "__main__":
    main()

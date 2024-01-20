import csv
import pandas


def main():
    data = pandas.read_csv("day-025/day-025_lesson_code_&_notes/weather_data.csv")
    print(data)

    # Find out the type of data
    print(type(data))
    # A 'Series' is a column of data
    # A 'DataFrame' is the table

    # You can convert the data into different types/formats
    temp_list = data["temp"].to_list()
    print(temp_list)

    # Get the average
    print(data["temp"].mean())

    # Get the maximum value
    print(data["temp"].max())

    # The column headings in the cvs file are made into attributes
    print(data.temp)

    # Get data in row
    print(data[data.day == "Monday"])

    # Get the row with the highest temp
    print(data[data.temp == data.temp.max()])

    # Get part of a row
    monday = data[data.day == "Monday"]
    print(monday.condition)

    # Create a dataframe
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("day-025/day-025_lesson_code_&_notes/new_data.csv")


def csv_example():
    with open("day-025/day-025_lesson_code_&_notes/weather_data.csv") as file:
        data = csv.reader(file)
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        print(temperatures)


if __name__ == "__main__":
    main()

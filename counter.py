def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    day_count = {}
    
    with open(file_name) as file:
        for line in file:
            if line.startswith("From "):
                day = grab_day(line)
                day_count[day] = day_count.get(day, 0) + 1

    print(day_count)


def grab_day(line: str) -> str:
    line = line.strip()
    line_list = line.split()
    day = line_list[2]

    return day



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()

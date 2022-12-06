import pytz
from pytz import timezone
from datetime import datetime

def main():
    format = "%Z %I:%M %p %a, %d/%m/%Y"
    zones = ["CET",
             "UTC",
             "Pacific/Auckland",
             "US/Pacific", 
             "US/Central",
             "US/Eastern",
            ]
    for zone in zones:
        time = datetime.now(timezone(zone)).strftime(format)
        print(f"{time}")

    while True:
        question = input("Do you want to print out all timezones? ")
        if question == "yes":
            pytz_zones()
            break
        elif question == "y":
            pytz_zones()
            break
        else:
            break
        
def pytz_zones():
    for timezone in pytz.all_timezones:
        print(timezone)

if __name__ == "__main__":
    main()

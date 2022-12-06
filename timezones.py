import pytz
from pytz import timezone
from datetime import datetime

def main():
    format = "%Z %I:%M %p %a, %d/%m/%Y"
    timezones = ["CET", "UTC", "Pacific/Auckland", "US/Pacific","US/Central", "US/Eastern"]
    for zone in timezones:
        time = datetime.now(timezone(zone)).strftime(format)
        if zone == "Pacific/Auckland":
            print(f"{time} - PoE")
        print(f"{time}")

if __name__ == "__main__":
    main()

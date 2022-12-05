import pytz
from pytz import timezone
from datetime import datetime

format = "%Z %I:%M %p %a, %d/%m/%Y"

time = datetime.now

CET = time(timezone("CET")).strftime(format) 
UTC = time(timezone("UTC")).strftime(format) 
PT = time(timezone("Pacific/Auckland")).strftime(format)
PST = time(timezone("US/Pacific")).strftime(format)
CST = time(timezone("US/Central")).strftime(format)
EST = time(timezone("US/Eastern")).strftime(format)

print("\n", CET, "\n",
            UTC, "\n",
            PT, "PoE", "\n", 
            PST, "\n",
            CST, "Lobos", "\n", 
            EST, "\n",)

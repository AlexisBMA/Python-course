import pytz
import datetime

available_zones = {"1": "Cuba",
      "2": "Egypt",
      "3": "America/Mexico_City",
      "4": "America/New_York",
      "5": "Europe/London",
      "6": "US/Hawaii",
      "7": "Japan",
      "8": "Australia/Melbourne",
      "9": "Europe/Madrid"}

print("Please choose a time zone (or 0 to quit)")
for place in sorted(available_zones):
    print("\t{}. {}".format(place,available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
from dateutil import relativedelta
import datetime


def upcoming_birthdays(people_list, days):
    # 90 is passed in as a parameter from menus.py

    for person in people_list:
        format_string = "%Y-%m-%d"
        birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)

        now = datetime.datetime.now()

        birthday_this_year = birthday_dt.replace(year=now.year)

        difference = birthday_this_year - now

        turning_age = relativedelta.relativedelta(now, birthday_dt).years + 1

        if 0 < difference.days < days: # difference less than 90 days and greater than 0            
            print(f"{person["name"]} turns {turning_age} in {difference.days} days on {birthday_dt.strftime("%B %d")}")


# format string {"name": "x", "birthday": "yyyy-mm-dd"} with string parse time
def display_age(person):
# 1- already now person name in dictionary
# 2- relativedelta to calculate dates. using a string a string {"yyyy-mm-dd"}
    format_string = "%Y-%m-%d"
    birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)
    today = datetime.date.today() # get today to subtract birthday from todays/nows date
    difference = relativedelta.relativedelta(today, birthday_dt) # today as earliest date
# the name is a key from the csv file
    print(f"{person['name']} is {difference.years} years, {difference.months} months, and {difference.days} days old")


def display_age_difference(people):
    format_string = "%Y-%m-%d"
    p0_dt = datetime.datetime.strptime(people[0]["birthday"], format_string)
    p1_dt = datetime.datetime.strptime(people[1]["birthday"], format_string)
    if p0_dt < p1_dt:
        difference = relativedelta.relativedelta(p1_dt, p0_dt)
        print(f"{people[0]["name"]} is older")
    else:
        difference = relativedelta.relativedelta(p0_dt, p1_dt)
        print(f"{people[1]["name"]} is older")

    print(f"{people[0]["name"]} and {people[1]["name"]}'s age difference is: {difference.years} years, {difference.months} months, and {difference.days} days")

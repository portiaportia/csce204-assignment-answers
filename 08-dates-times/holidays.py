from datetime  import date, time, datetime

holidays = {"Valentines Day": date(2021, 2, 14), 
             "St. Patricks Day": date(2021, 3, 17), 
             "Easter": date(2021, 4, 4), 
             "Memorial Day": date(2021, 5, 31), 
             "July 4th": date(2021, 7, 4), 
             "Labor Day": date(2021, 9, 6), 
             "Thanksgiving": date(2021, 11, 25),
             "Christmas": date(2021, 12, 25)}

for holiday in holidays:
    hDate = holidays[holiday]
    daysTillHoliday = (hDate - date.today()).days
    
    if daysTillHoliday < 0 :
        print(f"  {holiday} - " + hDate.strftime("%m/%d/%y") + f" Passed")
    elif daysTillHoliday == 0:
        print(f"* {holiday} - " + hDate.strftime("%m/%d/%y") + f" TODAY!")
    elif daysTillHoliday < 30 :
        print(f"* {holiday} - " + hDate.strftime("%m/%d/%y") + f" only {daysTillHoliday} days left")
    else:
        print(f"  {holiday} - " + hDate.strftime("%m/%d/%y"))
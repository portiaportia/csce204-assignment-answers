from datetime  import date, time, datetime

reminders = {"Drop kids off at school": time(7, 50), 
             "Pick up dry cleaning": time(8,30), 
             "Bake cookies for bake sale": time(10,0), 
             "Lunch with friends": time(12,30),
             "Yoga": time(13,15),
             "Pick up kids from school": time(14,30),
             "Soccer practice": time(15,15),
             "Dinner": time(17,00),
             "Piano Practice": time(18,30),
             "Read books": time(19,0),
             "Bed Time": time(20,0)
             }

# Loop through and display list of reminders
counter = 1

for reminder in reminders:
    rTime = reminders[reminder]
    print(f"{counter}. {reminder} - " + rTime.strftime("%I:%M %p"))
    counter += 1
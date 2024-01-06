from datetime import datetime
from plyer import notification
from time import sleep


while True:

    file = open("reminders.csv")

    reminders_data = file.readlines()

    current_datetime = str(datetime.now()).split(" ")

    current_date = current_datetime[0].split("-")

    current_time = current_datetime[1].split(":")
    
    for index,reminder in enumerate(reminders_data):

        if index == 0:
            continue

        reminder_details = reminder.split(",")
        reminder_date = reminder_details[1].split("-")
        reminder_time = reminder_details[2].split("-")

        if current_date[1] == reminder_date[1]:

            if current_date[2] == reminder_date[0]:

                
                if current_time[0] == reminder_time[0]:


                    if current_time[1] == reminder_time[1]:

                        print("matched")

                        sleep(20)
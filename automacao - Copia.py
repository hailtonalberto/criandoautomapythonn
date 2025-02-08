import webbrowser

import schedule
import time

@schedule.repeat(schedule.every().day.at("19:34"))
def tarefa():
    webbrowser.open("email payautogui.py")

    #schedule.every().second.until().do(tarefa)


while  True :
    schedule.run_pending()
    time.sleep(1)


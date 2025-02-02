import datetime

def return_current_time():
    now = datetime.datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return(formatted_date_time)
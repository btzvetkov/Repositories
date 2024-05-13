from datetime import datetime, time

start_time = datetime.combine(datetime.today(), time(3,0))
end_time = datetime.combine(datetime.today(), time(12,59))

try:
    time_str = input()
    time_obj = datetime.strptime(time_str, "%I:%M %p").time()
    if start_time.time() <= time_obj <= end_time.time():
        print("non-beer time")
    else:
        print("beer time")
except:
    print("invalid time")

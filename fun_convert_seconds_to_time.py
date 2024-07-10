# fun_convert_seconds_to_time.py
def fun_convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

print(fun_convert_seconds_to_time(3661))

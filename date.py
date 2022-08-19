import datetime as dt
while True:
    today = input('Enter start date. For example, 03/10/2021.\n')
    r = today.replace('/', ' ')
    l_t = r.split()
    day_today, month_today,  year_today = l_t[0],  l_t[1], l_t[2]

    thexday = input('Enter future date. For example, 15/11/2024.\n')
    c = thexday.replace('/', ' ')
    l_d = c.split()
    day_then, month_then, year_then = l_d[0], l_d[1], l_d[2]

    today_date = dt.datetime(int(year_today), int(month_today), int(day_today))
    future_date = dt.datetime(int(year_then), int(month_then), int(day_then))
    result = future_date - today_date
    print(f'There are {result} left.')

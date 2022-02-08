# https://www.codewars.com/kata/52742f58faf5485cae000b9a


def min_from_sec(sec):
    return sec // 60


def hours_from_min(min):
    return min // 60


def days_from_hours(h):
    return h // 24


def years_from_days(d):
    return d // 365


def sort_time(name):
    if name[0] == "second":
        return 0
    if name[0] == "minute":
        return 1
    if name[0] == "hour":
        return 2
    if name[0] == "day":
        return 3
    if name[0] == "year":
        return 4


def format_duration(seconds):
    if seconds == 0 or "" or None:
        return "now"
    # seconds, minutes, hours, days, years
    s, m, h, d, y = 0, 0, 0, 0, 0
    s = seconds % 60
    m = min_from_sec(seconds)
    h = hours_from_min(m)
    m = m % 60
    d = days_from_hours(h)
    h = h % 24
    y = years_from_days(d)
    d = d % 365

    time = {"second": s, "minute": m, "hour": h, "day": d, "year": y}
    # print(f'y: {y}  d:{d} h:{h} m:{m} s{s}')
    ans = ""
    for k, v in time.copy().items():
        if v == 0:
            time.pop(k)

    time = [[k, v] for k, v in time.items()]
    time.sort(reverse=True, key=sort_time)

    if len(time) == 1:
        ans = str(time[0][1]) + " " + time[0][0]
        if time[0][1] > 1:
            return ans + "s"
        else:
            return ans
    elif len(time) == 2:
        ans = str(time[0][1]) + " " + time[0][0]
        if time[0][1] > 1:
            ans = ans + "s" + " and "
        else:
            ans = ans + " and "

        ans = ans + str(time[1][1]) + " " + time[1][0]
        if time[1][1] > 1:
            ans = ans + "s"
        return ans
    elif len(time) > 2:
        time_str = []
        time.reverse()

        for idx, i in enumerate(time):
            if idx == 0:
                time_str.append("and " + str(i[1]) + " " + i[0])
                if i[1] > 1:
                    time_str[-1] += "s"

            if idx == 1:
                time_str.insert(0, str(i[1]) + " " + i[0])
                if i[1] > 1:
                    time_str[0] += "s"
            if idx > 1:
                time_str.insert(0, str(i[1]) + " " + i[0])
                if i[1] > 1:
                    time_str[0] += "s"
                time_str[0] += ","

        return " ".join(time_str)

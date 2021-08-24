def sum(x, y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + y['s']

    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1

    if result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1

    if result['h'] > 23:
        result['h'] -= 24
    return result


def minus(x, y):
    result = {}
    result['h'] = x['h'] - y['h']
    result['m'] = x['m'] - y['m']
    result['s'] = x['s'] - y['s']

    if result['m'] <= 0:
        result['h'] -= 1
        result['m'] += 60

    if result['s'] <= 0:
        result['m'] -= 1
        result['s'] += 60
    return result


def timetosec(x):
    x = ((x['h']*3600)+(x['m']*60)+x['s'])
    print('Total second is: ',x)


def sectotime(y):
    result = {'h': 0, 'm': 0, 's': 0}
    while True:
        if y >= 3600:
            y -= 3600
            result['h'] = result['h']+1
        elif y >= 60:
            y -= 60
            result['m'] = result['m']+1
        else:
            result['s'] = y
            break
    print('The total time is: ',result['h'], ":", result['m'], ":", result['s'])


def showtime(x):
    print(x['h'], ':', x['m'], ':', x['s'])


time1 = {'h': 12, 'm': 9, 's': 8}
time2 = {'h': 6, 'm': 12, 's': 14}

tsum = sum(time1, time2)
tminus = minus(time1, time2)
timetosecond = timetosec(time1)
secondtotime = sectotime(2000)

print('The sum and subtraction of these two numbers are: ')
showtime(tsum)
showtime(tminus)
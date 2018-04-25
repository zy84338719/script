import pandas as pd
import datetime as t

start = '2018-4-9'
end = '2019-4-7'
time = pd.bdate_range(start,end)

# print(type(time))
#
# print(type(now))
def restrict(day):
    a=['0,5','1,6','2,7','3,8','4,9']
    rest = pd.to_datetime(['2018-4-30',
                           '2018-5-1',
                           '2018-6-18',
                           '2018-9-24',
                           '2018-10-1',
                           '2018-10-2',
                           '2018-10-3',
                           '2018-10-4',
                           '2018-10-5',
                           '2018-12-31',
                           '2019-1-1',
                           '2019-2-4',
                           '2019-2-5',
                           '2019-2-6',
                           '2019-2-7',
                           '2019-2-8',
                           '2019-4-5'
                           ])
    print(rest)
    if day in rest:
        return None
    r = ruler(now)

    if day.weekday()== 0:
        n = r+0
        if n>4:
            n=n-5
        num = a[n]
    elif day.weekday() == 1:
        n = r+1
        if n>4:
            n=n-5
        num = a[n]
    elif day.weekday() == 2:
        n = r +2
        if n>4:
            n=n-5
        num = a[n]
    elif day.weekday() == 3:
        n = r + 3
        if n>4:
            n=n-5
        num = a[n]
    elif day.weekday() == 4:
        n = r + 4
        if n>4:
            n=n-5
        num = a[n]
    else:
        num = None

    return num


def ruler(now):
    if now < pd.to_datetime(['2018-7-9']):
        print("规则一")
        return 4
    elif now > pd.to_datetime(['2018-7-8']) and now < pd.to_datetime(['2018-10-8']):

        print('规则二')
        return 3
    elif now > pd.to_datetime(['2018-10-7']) and now < pd.to_datetime(['2019-1-7']):
        print('规则三')
        return 2
    elif now > pd.to_datetime(['2019-1-6']) and now < pd.to_datetime(['2019-4-8']):
        print('规则四')
        return 1
    elif now > pd.to_datetime(['2019-4-7']) and now < pd.to_datetime(['2019-7-6']):
        print('规则五')
        return 0
    else:
        print("None")
        return None


if __name__ == '__main__':
    now = pd.Timestamp(t.datetime(2018, 10, 1))
    # now = pd.datetime.now()
    res = restrict(now)
    print(res)
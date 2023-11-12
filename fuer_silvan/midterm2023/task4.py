import datetime


def weekday_of(date_string):
    x = datetime.datetime.fromisoformat(date_string)
    return x.weekday() + 1


print( weekday_of("1998-10-25") )
print( weekday_of("2001-01-01") )
print( weekday_of("1995-12-12") )
print( weekday_of("2023-11-06"))
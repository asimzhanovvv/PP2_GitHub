import datetime

x = datetime.datetime.now() - datetime.timedelta(days=5)
print(x.strftime("%d.%m.%Y"))
import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
z = x + datetime.timedelta(days=1)

print(x.strftime("Today: %d.%m.%Y"))
print(y.strftime("Yesterday: %d.%m.%Y"))
print(z.strftime("Tomorrow: %d.%m.%Y"))
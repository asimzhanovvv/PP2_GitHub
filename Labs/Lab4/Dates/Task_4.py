import datetime

date1_str = input("Enter first date (YYYY MM DD): ")
date2_str = input("Enter second date (YYYY MM DD): ")

date1 = datetime.datetime.strptime(date1_str, "%Y %m %d")
date2 = datetime.datetime.strptime(date2_str, "%Y %m %d")

difference = abs((date2 - date1).total_seconds())

print(f"Difference in seconds: {int(difference)}")

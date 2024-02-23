from datetime import date, datetime, timedelta

t = datetime.now()
print(t - timedelta(days=5))

y = t - timedelta(days=1)
tmrw = t + timedelta(days=1)
print("Yesterday:", y)
print("Today:", t)
print("Tomorrow:", tmrw)
print("Mithout ms:", t.replace(microsecond=0))
date1 = datetime(2024, 2, 20)
date2 = datetime(2024, 2, 23)
print("Difference in seconds:", (date2 - date1).total_seconds())

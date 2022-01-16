from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %w(sun:0 sat:5) %H:%M:%S %p")
weekday=datetime.today().weekday()

print(now)
print('weekday(mon:0 sun:6): ',weekday)

from datetime import datetime,date,timedelta
todays=datetime.now()
print(date.today())
birthday='25.11.2020'
data_birthday=datetime.strptime (birthday, '%Y.%m.%d').date()
print(data_birthday)
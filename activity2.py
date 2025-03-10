import random
import datetime
#define the start and end dates
start_date = datetime.date(2020,1,1)
end_date=datetime.date(2025,12,31)
random_days=random.randint(0 , (end_date - start_date).days)
random_date = start_date +datetime.timedelta(days=random_days)
print("random date: " , random_date)
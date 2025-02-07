from datetime import datetime, timedelta

current_date = datetime.today() #текущий

new_date = current_date - timedelta(days=5) #интервал 5 дней

print("Current Date:", current_date.date())
print("Date 5 days ago:", new_date.date())



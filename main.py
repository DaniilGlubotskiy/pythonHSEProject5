from datetime import datetime

# Для The Moscow Times
moscow_times_date_str = "Wednesday, October 2, 2002"
moscow_times_date = datetime.strptime(moscow_times_date_str, "%A, %B %d, %Y")
print("The Moscow Times:", moscow_times_date)

# Для The Guardian
guardian_date_str = "Friday, 11.10.13"
guardian_date = datetime.strptime(guardian_date_str, "%A, %d.%m.%y")
print("The Guardian:", guardian_date)

# Для Daily News
daily_news_date_str = "Thursday, 18 August 1977"
daily_news_date = datetime.strptime(daily_news_date_str, "%A, %d %B %Y")
print("Daily News:", daily_news_date)


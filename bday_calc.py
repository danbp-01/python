import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_1st = current_date.split('-')

b_date = input('Enter your birthday in yyyy-mm-dd format: ')
name = input('What is the name of the birthday legend? ')
b_date = b_date.split('-')

if current_date_1st[1] == b_date[1] and current_date_1st[2] == b_date[2]:
    age = int(current_date_1st[0])
    ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
    print(f" It's {name}'s {age}{ordinal_suffix} Birthday")
else:
    print("Sorry, today is not your birthday")
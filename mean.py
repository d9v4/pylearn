date = ('04.05.17')
team = 1
master_name = ('Петров Н.Н.')
kontrol_name = ('Иванова И.И.')
number_party = ('148')
ranks = 7
disign_name = ('Чистая линия Лак для волос 45*178')
speed = 320

count_welding = int(input('Счетчик сварки - '))
count_cf = input('Счетчик CF - ')
count_pallet = input('Счетчик паллет - ')

spent_time = count_welding / speed

print(date, disign_name, spent_time)

input()
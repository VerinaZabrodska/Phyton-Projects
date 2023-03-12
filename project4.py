from random import randint
list = [randint(1,10) for i in range(10)]
print(list)

x = int(input('Назвіть число:'))
s = 0
for i in list:
    if i==x:
        s=s+1
if s>=1:
    print(f'Скільки співпадає число {x} = {s}')
elif s<=x:
    print('Вибачте, даного числа немає')








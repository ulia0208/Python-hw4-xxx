from random import randint

n = int(input('Введите число '))

my_li = []
my_li2 = []

my_str = ()

for i in range(n + 1):
  my_li.append(randint(-100, 100))

print(my_li)

for i in range(n + 1):
  if my_li[i] == 0:
    if i != 0:
      my_li2.append('')
    else:
      my_li2.append('=0')

  elif my_li[i] == 1:
    if i != 0:
      my_li2.append(f'x^{i}')
    else:
      my_li2.append('1')
  elif my_li[i] == -1:
    if i != 0:
      my_li2.append(f'-x^{i}')
    else:
      my_li2.append('-1')
  else:
    my_li2.append(f'{my_li[i]}*x^{i}')

list.reverse(my_li2)

my_str = ('+'.join(my_li2))

for i in range(n + 1):
  my_str = my_str.replace('+-', '-')
  my_str = my_str.replace('++', '+')
  my_str = my_str.replace('--', '-')
  my_str = my_str.replace('-+', '+')
  my_str = my_str.replace('+=', '=')
  my_str = my_str.replace('-=', '=')

my_str = my_str.replace('*x^0', '=0')
my_str = my_str.replace('*x^1', 'x')
print(my_str)

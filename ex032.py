from datetime import date
ano = int(input('digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')
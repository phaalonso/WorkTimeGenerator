from prettytable import PrettyTable
import calendar
import json

dias_semana = {
    0 : 'Segunda',
    1 : 'Terca',
    2 : 'Quarta',
    3 : 'Quinta',
    4 : 'Sexta',
    5 : 'Sabado',
    6 : 'Domingo'
}

x = PrettyTable()
x.field_names = ['Dia da Semana', 'Data', 'Entrada', 'Saida']
c = calendar.TextCalendar(calendar.SUNDAY)
with open('arq.json', 'r') as f:
    horario = json.load(f)

ano = int(input('Insira o ano: '))
mes = int(input('Insira o mês: '))

for week in c.monthdays2calendar(ano, mes):
    for day, weekday in week:
        if day != 0:
            # print(day, dias_semana.get(weekday))
            if weekday < 5:
                for espediente in horario[dias_semana.get(weekday)]:
                    inicio, fim = espediente.values()
                    # print(inicio, fim)
                    # print(dias_semana.get(weekday), f'{day}/{mes}/{ano}', inicio, fim, sep = '\t\t')
                    x.add_row([dias_semana.get(weekday), f'{day}/{mes}/{ano}', inicio, fim])

print(x)
from datetime import date
data = date.today().year
maiores = menores = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    if data - ano < 21:
        menores += 1
    else:
        maiores += 1
print(f'Ao todo {maiores} pessoas atingiram a maioridade e {menores} pessoas ainda não são maiores ')

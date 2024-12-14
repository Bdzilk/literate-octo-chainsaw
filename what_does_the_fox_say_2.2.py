first = int(input("Дай целое число: "))
second= int(input("Дай другое целое число: "))
third = int(input("Дай еще целое число: "))
if first == second and first == third:
    print("Все, 3, равыны достаточно умно)")
elif first == second or first == third or second == third:
    print("Тут только, 2, равыны, попробуем еще?)")
else:
    print("Тут нет равыных, 0, пусто, ты совсем потерялся)")


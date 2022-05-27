# Task-1
print("Вычисление периметра и площади фигуры ".upper())
print("------------------------------------------------")
side_len_square = int(input("Enter side length of a square: "))
perim_square = side_len_square * 4
print("___________________________________________")
square_area = side_len_square ** 2
print(f"Периметр квадрата равен: {perim_square}")
print("Площадь квадрата равна: ", square_area, end="\n\n" )

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
length_rectangle = int(input("Enter side length of a rectangle: "))
width_rectangle = int(input("Enter side width of a rectangle: "))
perim_rectangle = 2 * (length_rectangle + width_rectangle)
area_rectangle = length_rectangle * width_rectangle
print("_________________________________________________")
print(f"Периметр прямоугольника равен: {perim_rectangle}")
print("Площадь квадрата равна: ", area_rectangle, end="\n\n" )


# Task-3

separ = input("Enter any symbol: ")
print()
print(separ * (perim_square + area_rectangle), end="\n\n")

# Task-2
print("приложение для финансового планирования".upper())
print("---------------------------------------", end="\n\n")
salary_month = int(input("Enter your monthly salary: "))
percent_mortgage = int(input("Enter percent mortgage: "))
percent_life = int(input("Enter percentage of living from salary: "))

mortgage_cash = (salary_month * percent_mortgage) / 100 
life_cash = (salary_month * percent_life) / 100
free_cash = salary_month - (mortgage_cash + life_cash)

if (percent_mortgage + percent_life) > 100:
  print("У тебя перерасход!! Надо жить экономнее.")
else:
  print("___________________________________________")
  print(f"На ипотеку было потрачено в м-ц: {mortgage_cash} рублей, за год: {mortgage_cash * 12} рублей".upper())
  print(f"На жизнь было потрачено в м-ц: {life_cash} рублей, за год: {life_cash * 12} рублей".upper())
  print(f"Свободные средства за м-ц: {free_cash} рублей, за год: {free_cash * 12} рублей".upper())

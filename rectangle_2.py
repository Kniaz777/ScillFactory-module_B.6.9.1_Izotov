from rectangle import Rectangle, Square, Circle
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print("Площадь первого прямоугольника = ", rect_1.get_area())
print("Площадь второго прямоугольника = ",rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("Площадь первого квадрата = ", square_1.get_area_square(),
      "Площадь второго квадрата = ", square_2.get_area_square())

radius_1 = Circle(8)
radius_2 = Circle(15)
print("Площадь первого круга = ", radius_1.get_area_circle(),
      "Площадь второго круга = ", radius_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, radius_1, radius_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())


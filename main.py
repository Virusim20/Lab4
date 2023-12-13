import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    print("Практична робота №4 Маріанна Забрянська 312ст\n\n")  
    task1()  

def distance(point1, point2):
    """Обчислити відстань між двома точками."""
    return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

def task1():
    """Виконати обчислення та вивести результати."""
    # Ручний ввід координат для чотирьох точок
    points = []
    for i in range(4):
        x = int(input(f"Введіть координату x для точки {i+1}: "))
        y = int(input(f"Введіть координату y для точки {i+1}: "))
        points.append(Point(x, y))

    # Обчислити відстань між другою та четвертою точками
    distance_2_to_4 = distance(points[1], points[3])
    print("Відстань між другою та четвертою точками:", distance_2_to_4)

    # Пересунути третю точку на 47 вгору
    points[2].y += 47

    # Вивести нові координати третьої точки
    print("Координати третьої точки після пересування:", points[2].x, points[2].y)

main()
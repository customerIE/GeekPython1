# 5. Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

import math
A_x = float(input('Введите координату точки А по оси Х: '))
A_y = float(input('Введите координату точки А по оси Y: '))
B_x = float(input('Введите координату точки B по оси Х: '))
B_y = float(input('Введите координату точки B по оси Y: '))
dist = math.sqrt((B_x - A_x)**2 + (B_y - A_y)**2)
print(dist)
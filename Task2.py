# 2. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def is_true(x,y,z):
    a = not(x or y or z)
    b = (not x) and (not y) and (not z)
    if a==b:
        print(F'При X={x}, Y={y}, Z={z} условие истинно.')
    else:
        print(F'При X={x}, Y={y}, Z={z} условие ложное.')
is_true(0,0,0)
is_true(0,0,1)
is_true(0,1,0)
is_true(0,1,1)
is_true(1,0,0)
is_true(1,0,1)
is_true(1,1,0)
is_true(1,1,1)
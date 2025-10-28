import random
def f(x):
    return -(x - 3)**2 + 9   
x = random.uniform(-10, 10)
y = f(x)


for i in range(100):
    new_x = x + random.uniform(-0.1, 0.1) 
    new_y = f(new_x)


    if new_y > y:
        x, y = new_x, new_y

print("Best x found:", round(x, 3))
print("Maximum value:", round(y, 3))

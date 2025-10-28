def f(x):
 # Example function: f(x) = -x^2 + 4x + 6
 return -x**2 + 4*x + 6
def hill_climbing(start, step=0.1, max_iter=1000):
 current = start
 for i in range(max_iter):
 left = current - step
 right = current + step
 current_val = f(current)
 left_val = f(left)
 right_val = f(right)
 if left_val > current_val and left_val >= right_val:
 current = left
 elif right_val > current_val and right_val >= left_val:
 current = right
 else:
 break
 return current, f(current)
def hill_descending(start, step=0.1, max_iter=1000):
 current = start
 for i in range(max_iter):
 left = current - step
 right = current + step
 current_val = f(current)
 left_val = f(left)
 right_val = f(right)
 if left_val < current_val and left_val <= right_val:
 current = left
 elif right_val < current_val and right_val <= left_val:
 current = right
 else:
 break
 return current, f(current)
start_point = 0
maxima, max_val = hill_climbing(start_point)
minima, min_val = hill_descending(start_point)
print(f"Local maxima at x = {maxima:.3f} with value = {max_val:.3f}")
print(f"Local minima at x = {minima:.3f} with value = {min_val:.3f}")
# def safety(meters):
#     return meters ** 3 * meters ** 2 - 12 * meters + 10

# D = float(input('Введите максимально допустимый уровень опасности: '))
# l = 0
# r = 4
# x_min = 4
# d_min = D

# while True:
#     x = (l + r) / 2
#     if safety(x) < abs(D):
#         r = x
#     elif safety(x) > D:
#         l = x
#     elif r - l < 1e-8:
#         break
#     else:
#         l = x
#         if abs(safety(x)) < abs(d_min):
#             x_min = x
#             d_min = safety(x)

# print('Приблизительная глубина безопасной кладки:', x_min, 'м')

# import sympy as sp

# def find_safe_depth(max_deviation):
#     # Define the function D(x) = x^3 - 3x^2 - 12x + 10
#     x = sp.Symbol('x')
#     D = x**3 - 3*x**2 - 12*x + 10

#     # Find the critical points (where D'(x) = 0)
#     critical_points = sp.solve(sp.diff(D, x), x)

#     # Choose the positive critical point (since depth cannot be negative)
#     safe_depth = max([point for point in critical_points if point > 0])

#     # Calculate the value of D at the safe depth
#     D_at_safe_depth = D.subs(x, safe_depth)

#     # Check if the deviation from zero is within the specified tolerance
#     if abs(D_at_safe_depth) <= max_deviation:
#         return safe_depth
#     else:
#         return None

# # Input: maximum deviation from zero
# max_deviation = float(input("Введите максимально допустимый уровень опасности: "))

# # Find the safe depth
# safe_depth_value = find_safe_depth(max_deviation)

# if safe_depth_value is not None:
#     print(f"Приблизительная глубина безопасной кладки: {safe_depth_value:.6f} м")
# else:
#     print("Не удалось найти подходящую глубину. Попробуйте другое значение допустимого отклонения.")

min = 0
max = 4

d_need = float(input('Введите максимально допустимый уровень опасности: '))

while True:
    depth = (max + min) / 2
    d_fact = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    
    if abs(d_fact - d_need) < 0.1e-9:
        print('Приблизительная глубина безопасной кладки:', round(depth, 9))
        break
    elif d_fact > d_need:
        min = depth
    else:
        max = depth

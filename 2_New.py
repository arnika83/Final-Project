import math

k = 1 / (4 * math.pi * 8.854 * (10**-12))

def huristics(x: int, y: int) -> float:
    return x**2 + y**2

def point_diff(x1, y1, x2, y2):
    return math.sqrt(huristics(x1 - x2, y1 - y2))

def find_bigO(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                return [i, j]
    raise ValueError("Grid does not contain an 'O'")

def calculate_electric_field(grid):
    Ex = 0
    Ey = 0   
    bigO_position = find_bigO(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 'O':                  
                charge = int(grid[i][j])             
                x_diff = j - bigO_position[1]
                y_diff = i - bigO_position[0]
                distance = point_diff(j, i, bigO_position[1], bigO_position[0])
                if distance != 0:
                    Ex += (k * x_diff * charge) / distance ** 3
                    Ey += (k * y_diff * charge) / distance ** 3

    return [Ex, Ey]

def calculate_line_electric_field(charge_density):
    L = 50  
    d = 1  
    Ex = 0
    Ey = 0

    num_segments = 1000
    segment_length = L / num_segments
    for i in range(num_segments + 1):
        x = -L / 2 + i * segment_length
        r = math.sqrt(x**2 + d**2)
        dE = (k * charge_density * segment_length) / r**2
        Ex_component = dE * (x / r)
        Ey_component = dE * (d / r)
        Ex += Ex_component
        Ey += Ey_component

    return [Ex, Ey]

# گرفتن ورودی از کاربر برای گرید
grid = []
n = int(input("Enter the size of the grid: "))
print(f"Enter the grid values (use 'O' for the target point):")
for i in range(n):
    l = input().split()
    grid.append(l)

# محاسبه میدان الکتریکی در گرید
Ex, Ey = calculate_electric_field(grid)

# نوشتن نتیجه در فایل
with open("electric_field_grid.txt", "w") as file:
    file.write(f"Electric field in grid: Ex = {Ex}, Ey = {Ey}\n")

# گرفتن ورودی از کاربر برای تراکم شارژ خط
charge_density = float(input("Enter the charge density (C/m) on the line: "))

# محاسبه میدان الکتریکی ایجاد شده توسط خط شارژ
Ex_line, Ey_line = calculate_line_electric_field(charge_density)

# نوشتن نتیجه در فایل
with open("electric_field_line.txt", "w") as file:
    file.write(f"Electric field at 1 meter of a 50 meter line: Ex = {Ex_line}, Ey = {Ey_line}\n")

print("Results have been written to electric_field_grid.txt and electric_field_line.txt files.")

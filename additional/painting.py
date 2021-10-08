x = float(input())
y = float(input())
h = float(input())
#pravougulna vrata sus strana 1.2m i vis. 2m
#kvadrated prozorec sus strana 1.5m
#stranichna stena
side_wall = x * y
window = 1.5 * 1.5
both = (2 * side_wall) - (2 * window)
back_wall = x * x
enter = 1.2 * 2
back_and_front = 2 * back_wall - enter
total_walls = both + back_and_front
green_paint = total_walls / 3.4

cell_rectangles = 2 * (x*y)
cell_triangles = 2 * (x * h / 2)
total_celling = cell_triangles + cell_rectangles
red_paint = total_celling / 4.3
print("%.2f" % green_paint)
print("%.2f" % red_paint)


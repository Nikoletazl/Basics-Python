v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())


p1_volume = p1 * h
p2_volume = p2 * h
pool_volume = p1_volume + p2_volume
pool_volume_percent = (pool_volume / v) * 100
p1_volume_percent = (p1_volume / pool_volume) * 100
p2_volume_percent = (p2_volume / pool_volume) * 100
if pool_volume <= v:
    print(f"The pool is {pool_volume_percent:.2f}% full. Pipe 1: {p1_volume_percent:.2f}%. Pipe 2: {p2_volume_percent:.2f}%.")
elif pool_volume > v:
    over = pool_volume - v
    print(f"For {h:.2f} hours the pool overflows with {over:.2f} liters.")
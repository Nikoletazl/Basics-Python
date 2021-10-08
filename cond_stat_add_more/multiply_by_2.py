n = int(input())
for i in range(0, n, n + 1):
   current_number = float(input())
if current_number > 0:
    positive = current_number * 2
    print(f"Result: {positive:2f}")
if current_number < 0:
    print("Negative number!")

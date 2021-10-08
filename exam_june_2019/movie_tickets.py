a1 = int(input())
a2 = int(input())
n = int(input())
symbol4 = 0
for first in range(a1, a2 + 1):
    symbol = chr(a2 - 1)
    for second in range(1, n + 1):
        symbol2 = n - 1
        for third in range(1, n + 1):
            symbol3 =int((n / 2) - 1)
            sum = symbol2 + symbol3 + symbol4
    symbol4 = ord(symbol)
if symbol4 % 2 != 0:
    if sum % 2 != 0:
        print(f"{symbol}-{symbol2}{symbol3}{symbol4}")
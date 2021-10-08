#1 rab mqsto 70*120
#koridor 100
#gubim 3 mesta
#zala 890
# zala - koridor = 790
#biura na red = 790/70
import math
h = float(input()) * 100
w = float(input()) * 100
w_space = math.floor((w-100)/ 70)
h_space = math.floor(h/120)
seats = w_space * h_space - 3
print(seats)
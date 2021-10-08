kg_vegetables = float(input())
kg_fruits = float(input())
total_vegetables = int(input())
total_fruits = int(input())
everything = kg_vegetables * total_vegetables + kg_fruits * total_fruits
euro = everything / 1.94
print("%.2f" % euro)
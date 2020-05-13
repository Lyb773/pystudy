a = int(input("base demand = "))
b = int(input("price sensitivity = "))
c = int(input("unit cost = "))

maxprofit = 0
bestprice = 0
for p in range(c + 1, a // b):  # c+1=至少要比成本多，a//b=a少于b就没有可能获利
    profit = (a - b * p) * (p - c)
    print(p, profit)

    if profit > maxprofit:
        maxprofit = profit
        bestprice = p
    else:
        break #(a - b * p) * (p - c)是一个曲线，只要最高点就够了

print("bestprice =", bestprice)
print("maximized profit =", maxprofit)

#这是以个关与商品定价的小程序
a = int(input("base demand = "))
b = int(input("price sensitivity = "))
c = int(input("unit cost = "))

maxprofit = 0
bestprice = 0
for p in range(c + 1, a // b):  # c+1是因为定价至少要比成本多，a//b中a代表免钱，少于b就是免费都没人要，没有可能获利
    profit = (a - b * p) * (p - c) # 商品定价（a-bp)(p-c)
    print(p, profit)

    if profit > maxprofit:
        maxprofit = profit
        bestprice = p
    else:
        break #(a - b * p) * (p - c)是一个曲线，只要最高点就够了

print("bestprice =", bestprice)
print("maximized profit =", maxprofit)

#存货策略(periodic Q.R policy，Find the best R in single product)
salestr = input("Sales data: ")
sale = salestr.split(',')
for i in range(len(sale)):
    sale[i] = int(sale[i])
# stgcost = shortage cost , invcost = inventory cost per day(/365)
stgcost = int(input("stgcost: "))
inv = float(input("annuel invcost(in decimal): "))
Q = int(input("Order quantity Q: "))
I = int(input("Inital inventory I: "))
invcost = 1000 * inv / 365

# finding the best R (number of reorder)
bestR = 0
costofbestR = 1000000
for R in range(Q):
    totalstgcost = 0
    totalinvcost = 0
    for s in sale:
        I -= s
        if I < 0:
            totalstgcost += -I * stgcost
            I += Q
        elif I < R: #这里假设每一天需求量没有大过Q，没有供不应求
            I += Q
            totalinvcost += I * invcost
    #update bestR
    totalCost = totalstgcost + totalinvcost
    if totalCost < costofbestR:
        bestR = R
        costofbestR = totalCost
    print(R, totalstgcost, totalinvcost, totalCost)
print(bestR)

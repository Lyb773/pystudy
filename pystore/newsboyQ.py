#这是一个单层的报童问题,但这次是找出最佳订货量
#需求量是有数据的，因此没有作离散分布

import math

c = int(input()) #进货成本
r = int(input()) #单位零售价
N = int(input()) #需求的个数
plist = []
for i in range(9):
    plist.append(float(input()))

exp = 0
sum = 0.0 #预期利润
D = 0.0
maxP = 0.0 #最佳收益
maxq = 0 #最佳订货量
for q in range(N + 1):
    sum = 0
    D = 0.0
    for p in range(q + 1):
        exp = r*p - c*q
        if p != q:
            sum += plist[p]*exp
            D += plist[p]
        else:
            sum += (1 - D)*exp
            break
    if sum > maxP:
        maxP = sum
        maxq = q

print(str(maxq),str(int(maxP))) #输出整数，不必要

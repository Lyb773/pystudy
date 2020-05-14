#这是一个单层的报童问题
#需求量是有数据的，因此没有作离散分布

import math

c = int(input()) #进货成本
r = int(input()) #单位零售价
N = int(input()) #需求的个数
q = int(input()) #订货量
plist = []
for i in range(9):
    plist.append(float(input()))

exp = 0
sum = 0.0 #预期利润
D = 0.0

for p in range(N + 1):
    exp = r*p - c*q
    if p != q:
        sum += plist[p]*exp
        D += plist[p]
    else:
        sum += (1 - D)*exp
        break

print(int(sum))

#LPT 演算法(without sorting )
n = int(input("Number of jobs: "))
m = int(input("Number of machines: "))
pstr = input("Processing times: ")

p = pstr.split(' ')
for i in range(n):
    p[i] = int(p[i])

loads = [0] * m
assignment = [0] * n

#assign job j to the least load machine
for j in range(n):
    #find the lease loaded machine
    leastloadmach = 0
    leastload = loads[0]
    for i in range(1, m):  #0..1..2..m-1
        if loads[i] < leastload:
            leastloadmach = i
            leastload = loads[i]

    #schedule a job
    loads[leastloadmach] += p[j]
    assignment[j] = leastloadmach + 1 #index 是 0，1，2，3，4，5这样派，加一就是1号2号3号。。。

    #check the Process
    print(str(p[j]) + ": " + str(loads))

print("Job assignment: " + str(assignment))
print("Machine loads: " + str(loads))

#Travelling salesperson problem(TSP)
#greedy algorithm,but 每次只能看一步
#locnum = 5 #location number
#dst = [[0, 9, 6, 7, 4], #2-dim
#       [9, 0, 5, 9, 6], #dst[i][j] = distance between locations i and j
#       [6, 5 ,0, 3, 1],
#       [7, 9, 3, 0, 4],
#       [4, 6, 1, 4, 0]]
locnum = int(input())
dst = []
for i in range(locnum):  #input 等同numlo数的数字，用空格隔开
    dst.append(input().split())
    for j in range(locnum):
        dst[i][j] = int(dst[i][j])

origin = 0

#tour:solution
#tourlen:total distance of solution
#unvisited:unvisited locations
tour = [origin]
tourlen = 0
unvisited = []
for i in range(locnum):
    unvisited.append(i)
unvisited.remove(origin) #start point is visited

print(tour, tourlen)

#the algorithm
cur = origin
for i in range(locnum - 1): #每次出发的第一个点已经决定了，接下来要选numlog-1次就好了
    #find the next location to visit
    next = -1
    mindst = 999
    for j in unvisited:
        if dst[cur][j] < mindst: #update next
            next = j
            mindst = dst[cur][j]
    unvisited.remove(next)
    tour.append(next)
    tourlen += mindst
    #run the next iteration from the next locations
    print(tour, tourlen) #take a look
    cur = next

tour.append(origin)
tourlen += dst[cur][origin]
print(tour,tourlen)

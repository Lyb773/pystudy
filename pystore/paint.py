#今天有一群人在為n面牆壁漆油漆，一開始都是顏色1，經過著色後會被覆蓋，變成其他顏色。
#第一行輸入牆壁n面和m次油漆，接下來的m行每行依順序輸入漆的牆壁的起點號碼、漆的牆壁的終點號碼，以及顏色代碼，都是合理的整數。
#輸出共有m段，於第 i 段輸出在全部油漆動作都完成後，第 i 次油漆之顏色的牆壁面數、一個空格，與該顏色代碼。段與段之間用一個分號隔開。
#所有牆壁在最初都是顏色 1。

n, m = map(int,input().split()) 
wcolour = [1 for x in range(n)]  
stls, endls, codels = [], [], []
for i in range(m):
  s, e, cc = map(int,input().split()) 
  #s = starting wall
  #e = ending wall
  #cc = colour code (eg.1,2,3....)
  stls.append(s)
  endls.append(e)
  codels.append(cc)
for i in range(m):
  for j in range(stls[i]-1, endls[i]):
    wcolour[j] = codels[i]

dwcolour = dict() #ch to a dict
for element in wcolour:
  if element not in dwcolour:
    dwcolour[element] = 1
  else:
    dwcolour[element] += 1

print(dwcolour)

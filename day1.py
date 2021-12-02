data = open('input_day1.txt', 'r').read().split()
intData = []
for i in range(len(data)):
        intData.append(int(data[i]))

#PART 1
more=0
for i in range(0, len(intData)):
    if i>=1:
        if intData[i]>intData[i-1]:
            more += 1
            
print(more) #Answer: 1791

#PART 2
more=0
sumList=[]
for i in range(len(intData)):
    try:
        sum=intData[i]+intData[i+1]+intData[i+2]
        sumList.append(sum)
    except:
        pass

for i in range(0, len(sumList)):
    if i>=1:
        if sumList[i]>sumList[i-1]:
            more=more+1

print(more) #Answer: 1822

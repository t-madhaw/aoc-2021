data = open('input_day2.txt', 'r').readlines()
stripped_data = [s.rstrip() for s in data]  #to get rid of \n
final_data = []

#stripping each string into a list of string and integer
for i in stripped_data:
    loc = i.split()
    loc[1] = int(loc[1])
    final_data.append(loc)

#Part 1

hor=0
depth = 0

for i in final_data:
    if i[0]=='forward':
        hor += i[1]
    elif i[0] == 'up':
        depth -= i[1]
    elif i[0] == 'down':
        depth += i[1]
        
print(hor*depth) #Answer: 1714950

#Part 2

aim=0
hor=0
depth = 0

for i in final_data:
    if i[0]=='forward':
        hor += i[1]
        depth += aim*i[1]
    elif i[0] == 'up':
        aim -= i[1]
    elif i[0] == 'down':
        aim += i[1]

print(hor*depth)  #Answer: 1281977850

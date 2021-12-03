file = open("input_day3.txt", "r").readlines()
rawdata = list(map(str.strip, file))
data = []
for i in range(len(rawdata)):
    data.append(list(rawdata[i]))
    
#PART 1

#creating dictionary to track occurence for each place-value
dic={}
keys= ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii']
for val in keys:
    dic[val]=0
    
#counting occurences
for num in data:
    for i in range(len(num)):
        if num[i]=='0':
            #print(num[i], keys[i])
            dic[keys[i]]+=1
            
#calculuating gamma, epsilon
gamma, epsilon = '',''
for i in keys:
    if dic.get(i)>500:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
gamma, epsilon = int(gamma, 2), int(epsilon, 2)
print("power consumption rating =", gamma*epsilon)  #Answer: power consumption rating = 3009600

#PART 2


    

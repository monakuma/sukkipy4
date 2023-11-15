numbers=[1,1]

data=sum(numbers)
count=2

# while  data<=1000:
#         numbers.append(data)
#         data=data+numbers[count-1]
#         count +=1
# print(numbers)
while True:
    next=numbers[-1]+numbers[-2]
    if next>1000:
        break
    numbers.append(next)
print(numbers)

rations=list()
for count in range(len(numbers)):
        if count==len(numbers)-1:
                break
        rations.append(numbers[count+1]/numbers[count])
print(rations)
        
for n in range(len(rations)):
    rations[n]=int(rations[n]*1000)/1000
print(rations)


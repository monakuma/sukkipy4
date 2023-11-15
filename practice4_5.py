# time=['8時','9時','10時','11時','12時','13時','14時','15時','16時','17時']
# temp={time[0]:7.8,time[1]:9.1,time[2]:10.2,time[3]:11.0,time[4]:12.5,time[5]:12.4,time[6]:14.3,\
#       time[7]:13.8,time[8]:12.9,time[9]:12.4}
tempA=[7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
temp_new=[7.8,9.1,10.2,11.0,12.5,'N/A',14.3,13.8,12.9,12.4]

sampleA=list()
sampleB=list()
total=0
Time=0

for temperature in tempA:
        print(f"{Time+8}時,{temperature}℃",end=" ")
        Time +=1
print()
for tempB in temp_new:
        if  isinstance(tempB ,str):
            continue
        sampleB.append(float(tempB) )
        total=total+tempB
print(f"{sampleB}℃")
print(total)

print(f"temp_newの平均気温は{total/(len(temp_new)-1):.2f}℃")


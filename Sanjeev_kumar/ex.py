list=[18,20,8,16,4,10,12,3]
list.sort()
print(list)
count=0
num=list[-2]
print("second max number is::",num)
while(num!=0):
    if num%2==0:
        num=num/2
        count+=1
    else:
        num=num-1
        count+=1  
print("no of step::",count)
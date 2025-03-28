def listsum (mylist):
    mysum = 0
    for i in mylist:
        mysum += i
    return mysum

def listavg (mylist):
    myavg = listsum(mylist)/len(mylist)
    return myavg


mynums= []
newlist = []
for i in range(1,21):
    mynums.append(i)
print (mynums)
for i in mynums:
    if i % 2 != 0:
        mynums.remove(i)
print (mynums)
for i in mynums:
    newlist.append(i*2)
print(newlist)
print("sum of the list is :" ,listsum(newlist))
print("average of the list is:" ,listavg(newlist))




listcomprehension = [i*i for i in range(1,21) if i %2 == 0]
print (listcomprehension)
    

        

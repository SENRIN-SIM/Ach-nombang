count=1
while (count < 5):
    print ("yes")
    print ("count =", count)
    count+=1

count=int(input("Enter number here:"))
while (count>=1 and count <= 100):
    count *=2
    print(count)
    if count<=-1:
        count=int(input("Enter again:"))




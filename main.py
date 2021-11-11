print("{}Hi this is a test python project!!!{}".format("\n\n\n\n","\n\n\n\n"))

def SelectionSort(l):
    for i in range(len(l)):
        temp=l[i];
        for j in range(i,len(l)):
            if l[j]<temp:
                l[i]=l[j]
                l[j]=temp;


l=[2,4,1,7,6,10,0]

SelectionSort(l);

print(l);



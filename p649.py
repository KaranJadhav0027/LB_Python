def ReverseList(Brr):
    start=0
    end=len(Brr)-1
    temp=0
    while(start<end):
        temp=Brr[start]
        Brr[start]=Brr[end]
        Brr[end]=temp

        start+=1
        end-=1
         
def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    ReverseList(Arr)
    print(Arr)
    
if __name__=="__main__":
    main()
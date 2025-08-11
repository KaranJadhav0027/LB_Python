def Update(Brr):

    i=0
    for i in range(len(Brr)-1,-1,-1):
        if(Brr[i]%2==0):
           Brr[i]=Brr[i]+1

def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    Update(Arr)
    print(Arr)
    
if __name__=="__main__":
    main()
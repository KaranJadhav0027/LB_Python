       
def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    print(Arr)
if __name__=="__main__":
    main()
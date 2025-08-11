def CheckMax(No1,No2,No3):
    if (No1>No2 and No1>No3):
         return No1
    elif(No2>No1 and No2>No3):
         return No2
    else:
         return No3

def main():
    print("Enter First Number")
    Value1=int(input())

    print("Enter Second Number")
    Value2=int(input())

    print("Enter Third Number")
    Value3=int(input())

    Ret=CheckMax(Value1,Value2,Value3)
    
    
    print(f"{Ret} is Maximun number")
   
if __name__=="__main__":
    main()
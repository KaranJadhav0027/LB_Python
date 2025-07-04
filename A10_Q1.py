"""############################################################

Enter Staring Point  :2
Enter End Point  :18

Number between : 2  to  18  are :
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

Even Number between : 2  to  18  are :
2 4 6 8 10 12 14 16 18

Odd Number between : 2  to  18  are :
3 5 7 9 11 13 15 17

Addition of Even Number Between  2  to  18  is : 90

Addition of Odd Number Between  2  to  18  is : 80
###############################################################"""
class Range:
    def __init__(self,No1,No2):
        self.Start=No1
        self.End=No2

    def Display(self):
        print("Number between :",self.Start," to ",self.End," are :")
        if self.Start>self.End:
            print("Invalid Range..")

        for i in range(self.Start,self.End+1):
            print(i,end=" ")
        print()
    
    def DisplayEven(self):
        print("Even Number between :",self.Start," to ",self.End," are :")
        if self.Start>self.End:
            print("Invalid Range..")
        ETotal=0  
        for i in range(self.Start,self.End+1):
            if i%2==0:
                ETotal=ETotal+i
                print(i,end=" ")
        print()
        return ETotal

    def DisplayOdd(self):
        print("Odd Number between :",self.Start," to ",self.End," are :")
        if self.Start>self.End:
            print("Invalid Range..")
        OTotal=0  
        for i in range(self.Start,self.End+1):
            if i%2!=0:
              OTotal=OTotal+i
              print(i,end=" ")
        print()
        return OTotal

def main():
    print("Enter Staring Point  :",end="")
    Value1=int(input())

    print("Enter End Point  :",end="")
    Value2=int(input())

    tobj=Range(Value1,Value2)
    tobj.Display()
    ERet=tobj.DisplayEven()
    ORet=tobj.DisplayOdd()

    print("Addition of Even Number Between ",Value1 ," to ",Value2 ," is :",ERet)
    
    print("Addition of Odd Number Between ",Value1 ," to ",Value2 ," is :",ORet)

if __name__=="__main__":
    main()
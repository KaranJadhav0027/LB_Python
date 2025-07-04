"""############################################################

Enter a number :4

4 8 12 16 20 24 28 32 36 40

40 36 32 28 24 20 16 12 8 4
###############################################################"""
class Table:
    def __init__(self,No):
        self.No=No
    
    def CreateTable(self):
        Result=1
        for i in range(1,11):
            Result=i*self.No
            print(Result,end=" ")
        print()

    def CreateTableRev(self):
        Result=1
        for i in range(10,0,-1):
            Result=i*self.No
            print(Result,end=" ")

def main():
    print("Enter a number :",end="")
    Value=int(input())

    tobj=Table(Value)
    tobj.CreateTable()
    tobj.CreateTableRev()

if __name__=="__main__":
    main()
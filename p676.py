# input Row : 5 col :4
"""
   Enter a Number Row
4
Enter a Number Coloum
5
*       *       *       *
*       *       *       *
*       *       *       *
*       *       *       *
*       *       *       *
"""

def Display(row,col):

    # for i in range(col):
    #     for j in range(row):
    #        print("*",end="\t")
    #     print()
    
    for i in range(1,col+1,1):
        for j in range(1,row+1,1):
           print("*",end="\t")
        print()
      
    print()

def main():
    print("Enter a Number Row")
    Value1=int(input())
   
    print("Enter a Number Coloum")
    Value2=int(input())

    Display(Value1,Value2)  

if __name__=="__main__":
    main()
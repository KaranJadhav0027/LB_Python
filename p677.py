# input Row : 4 col :4
"""
Enter a Number Row
4
Enter a Number Coloum
4
$       *       *       *
*       $       *       *
*       *       $       *
*       *       *       $

"""

def Display(row,col):

    if(col !=row):
       print("INValid")
       return
    
    for i in range(1,row+1,1):
        for j in range(1,col+1,1):
           if(i==j):
             print("$",end="\t")
           else:
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
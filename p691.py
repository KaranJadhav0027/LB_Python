class demo:
    def __init__(self,A=0,B=0):
        print("Inside Constructor")
        self.No1=A
        self.No2=B

    def __del__(self):
        print("Inside Distructor")

    def Display(self):
        print("Value of No1 is :",self.No1)
        print("Value of No1 is :",self.No2)
    
def main():
    print("Inside Main")
    obj1=demo()
    obj2=demo()
    
    obj1.Display()
    obj2.Display()
    print("End of main")
      
if __name__=="__main__":
    main()
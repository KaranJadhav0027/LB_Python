class demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Distructor")
    
def main():
    print("Inside Main")
    obj1=demo()
    obj2=demo()

    print("End of main")
      
if __name__=="__main__":
    main()
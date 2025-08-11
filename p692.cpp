#include<iostream>
using namespace std;

class demo
{
  public:
    int No1;
    int No2;
    
  demo(int A=0,int B=0)
    {
        cout<<"Inside Constructor\n";
        this->No1=A;
        this->No2=B;
    }
    ~demo()
    {
        cout<<"Inside Distructor";
    }

    void Display()
    {
        cout<<"Value of No1 is :"<<this->No1<<"\n";
        cout<<"Value of No1 is :"<<this->No2<<"\n";
    }   
};

int main()
{
    cout<<"Inside Main"<<"\n";
    
    demo obj1;
    demo obj2;
    
    obj1.Display();
    obj2.Display();

    cout<<"End of main"<<"\n";

    return 0;
}
      
#include <thread>
#include <iostream>
#include <memory>

void f(std::shared_ptr<int> x, int y){
    std::cout << "Hi!"<< *x << " " << y << std::endl;
}

int main(){
    std::shared_ptr<int> a = std::make_shared<int>(1);
    std::thread tr1(f, a, 1); // 'a' (the shared_ptr object) is passed by value, creating a copy for the thread
    std::thread tr2(f, a, 2);

    int b = 5+2+*a;
    if (b > 5)
    {
        if (tr1.joinable())
        {
            tr1.join();
        }
        
        return 1;
    }

    if (b < -1)
    {
        //everytime we need to check and rejoin...
        return 5;
    }
    
    
    
    if (tr1.joinable())
    {
        tr1.join();
    }

    //tr1.detach(); //dangerous



    
    // solo così da errore: terminate called without an active exception
    //cannot move an lvalue ref to an r value ref unless it's a const
    //by default every value is passed by value, better pass by pointers than by reference
}
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, t1=0, t2=1, next_term;
    
    cout<<"Enter a positive integer: "<<endl;
    cin>>n;
    
    cout<<"Fibonacci series: "<<t1<<" , "<<t2<<" , ";
    
    next_term = t1 + t2;
    int count = 2;
    while(count<n)
    {
        cout<<next_term<<" , ";
        t1 = t2;
        t2 = next_term;
        next_term = t1 + t2;
        count++;
    }
    
    return 0;
}


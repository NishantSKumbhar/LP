// // Recursion - Fibonacci Series

// // Concept: term_n = term_(n-1) + term_(n-2)

// // Base Condition: if(n==0 || n==1) => return n;

#include<bits/stdc++.h>
using namespace std;

int get_fibonacci(int num)
{
    if (num == 0 || num == 1)
    {
        return num;
    }

    return get_fibonacci(num - 1) + get_fibonacci(num - 2);

}

int main()
{
    int num;
    cout<<"Enter the positive interger: "<<endl;
    cin>>num;

    for(int i=0; i<num; i++)
    {
        cout<<get_fibonacci(i)<<" ";
    }

    return 0;
}

// //Time Complexity: O(2^n)
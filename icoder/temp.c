#include<stdio.h>
#include<string.h>
int main()
{
    char str[10];
    int n=5; //number of characters you want to store in char array.
    for(int i=0;i<n;i++)
    {
        printf("Enter the character %d: ",i+1);
        scanf("%c",&str[i]);
        getchar();
    }
    // Now for printing the stored values inside the char array.
    for(int i=0;i<n;i++)
    {
        printf("the character stored at index %d is %c\n",i,str[i]);
    }
}
#include<stdio.h>
int main()
{
char n,a[10],i;
scanf("%d",&n);
for(i=0;i<n;i++)
{
Scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
printf("%d %d\n",a[i],i);
}
return 0;
}

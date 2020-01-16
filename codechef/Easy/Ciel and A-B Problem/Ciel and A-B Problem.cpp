#include<bits/stdc++.h>
using namespace std;
int main(){
	int a,b,c;
	scanf("%d",&a);
	scanf("%d",&b);
	c = a-b;
	if(c%10 == 9){
		printf("%d",c-1);
	}else{
		printf("%d",c+1);
	}
	return 0;
}

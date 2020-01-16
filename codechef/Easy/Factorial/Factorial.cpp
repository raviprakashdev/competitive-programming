#include<bits/stdc++.h>
using namespace std;

int respond(int n){
	int ans = 0;
	while(n>0){
		ans = ans + n/5;
		n = n/5;	
	}
	return ans;
}

int main(){
	int t,num;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&num);
		printf("%d\n",respond(num));
	}
	return 0;
}

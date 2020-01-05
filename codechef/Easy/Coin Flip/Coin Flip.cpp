#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int g,i,n,q;
		scanf("%d",&g);
		while(g--){
			scanf("%d",&i);
			scanf("%d",&n);
			scanf("%d",&q);
			if(i==q){
				printf("%d",n/2);
			}else{
				printf("%d",(n+1)/2);
			}
		}	
	}
	return 0;
}

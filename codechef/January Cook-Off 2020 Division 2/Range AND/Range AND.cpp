#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mod 1000000007

int main(){
	ll t;
	scanf("%d",&t);
	while(t--){
		ll start,end;
		scanf("%d%d",&start,&end);
		ll s = start;
		ll b = start;
		for(ll i=start;i<end;i++){
			b = b & i & (i+1);
			b = b;
			s = (s+b);
			if(b == 0){
				break;
			}
		}
		printf("%d\n",s%mod);
	}
	return 0;
}

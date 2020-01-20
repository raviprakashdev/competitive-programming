#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main(){
	ll t;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		int arr[n];
		for(int i=0;i<n;i++){
			scanf("%d",&arr[i]);
		}
		sort(arr,arr+n);
		printf("%d\n",arr[0]);
	}
	return 0;
}

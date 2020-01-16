#include<bits/stdc++.h>
#include <set> 

using namespace std;

int main(){
	int t,num,i;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&num);
		int arr[num];
		for(int i =0; i<num; i++){
			scanf("%d",&arr[i]);
		}
		sort(arr, arr + num);
		set <int , greater <int>> result;
		for(int i =0; i<num-1; i++){
			result.insert(arr[i+1] - arr[i]);
		}
		printf("%d",*result.begin());
		}
	return 0;
}

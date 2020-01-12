#include<iostream>

using namespace std;
int main (){
	
	int t;
	cin>>t;
	while(t--){
		int x,y,k,n,flag = 0 ;
		cin>>x>>y>>k>>n;
		int rem = x-y;
		int nop, price;
		while(n--){
			cin>>nop>>price;
			if(nop>=rem && price<=k ){
				flag = 1;
			}
		}
		if(flag==0)
			cout<<"UnluckyChef"<<endl;
		else
			cout<<"UnluckyChef"<<endl;
	}
	
	return 0;
}

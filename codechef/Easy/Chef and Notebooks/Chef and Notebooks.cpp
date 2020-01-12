#include<iostream>
using namespace std;
int main (){
	int t;
	scanf("%d",&t);
	while(t--){
		int x,y,k,n,flag = 0 ;
	    scanf("%d%d%d%d",&x,&y,&k,&n);
		int nop, price;
		while(n--){
    	    scanf("%d%d",&nop,&price);
			if(nop>=(x-y) && price<=k ){
				flag = 1;
			}
		}
		if(flag==0)
		    cout<<"UnluckyChef"<<endl;
		else
		    cout<<"LuckyChef"<<endl;
	}
	return 0;
}

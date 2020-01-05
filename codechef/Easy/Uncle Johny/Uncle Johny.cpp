#include<bits/stdc++.h> 
using namespace std;
int main () 
{ 
	int t;
	scanf("%d",&t);
    while(t--){
    	vector<int> vec; 
	    int c,i;
	    scanf("%d",&c);
		while(c--){
			int a;
			printf("enter a:");
			scanf("%d",&a); 
		    vec.push_back(a); 
		}
		for(auto i = vec.begin(); i != vec.end() ; ++i){
			printf("%d",*i);
		}
	    //vector<int>::iterator it;  
	    //sort(vec.begin(), vec.end());
	    /*int ser;
		scanf("%d",ser); 
	    it = find (vec.begin(), vec.end(), ser); 
		if (it != vec.end()) 
	    { 
	      printf("%d\n",it - vec.begin() + 1);  
	    }*/
	}
    return 0; 
} 

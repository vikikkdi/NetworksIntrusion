#include<bits/stdc++.h>
using namespace std;

bool isChar(int a) {
	return (a>=97 && a<=122) || (a>=65 && a<=90);
}

int isNormalCluster(string s) {
	int ans = 0;
	string type = "";
	for(int i=0;i<s.length();i++) {
		if(s[i]>=48 && s[i]<=57) {
			ans = ans * 10 + (s[i] - 48);
		}
		else if(isChar(s[i])) {
			type = type + s[i];
		}
	}
	if(type == "normal") {
		return ans;
	}
	return -1;
}

int main() {
	ifstream clusterIndexFile;
	clusterIndexFile.open("out_train.txt");
	string s;
	map<int,int> setOfNormalClusterIndices;
	if(clusterIndexFile.is_open()) {
			while(!clusterIndexFile.eof()) {
				getline(clusterIndexFile,s);
				s = s.substr(0,s.length()-1);
				int normalCluster = isNormalCluster(s);
				if(normalCluster != -1) {
					setOfNormalClusterIndices[normalCluster]++;
				}
			}
	}
	for(auto it : setOfNormalClusterIndices) {
		cout << it.first<<"\t"<<it.second << endl;
	}
	clusterIndexFile.close();
}
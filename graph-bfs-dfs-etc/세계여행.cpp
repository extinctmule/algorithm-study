#include <bits/stdc++.h>

using namespace std;

int N, M, arr[1003], vis[1003];
vector<int> adj[1003];

void dfs(int cur, int lan){
	vis[cur] = 1;
	
	for(auto nxt : adj[cur]){
		if(vis[nxt] || !(arr[nxt] == lan || arr[nxt] == arr[1]) ) continue;
		dfs(nxt, lan);
	}
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> N >> M;
	for(int i = 1; i <= N; i += 1){
		cin >> arr[i];
	}
	
	for(int i = 0; i < M; i += 1){
		int a, b; cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	
	int res = 0;
	for(int i = 1; i <= 10; i += 1){
		memset(vis, 0, sizeof(vis));
		dfs(1, i);
		int cnt = 0;
		for(int i = 1; i <= N; i += 1){
			if(vis[i]) cnt += 1;
		}
		res = max(res, cnt);
	}
	
	cout << res << '\n';
	
	return 0;
}
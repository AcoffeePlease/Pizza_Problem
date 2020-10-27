#include <bits/stdc++.h>
using namespace std;
#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef DEBBY
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
      *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

#define ll long long
#define rep(i,a,b) for(int i=int(a); i<=int(b); i++)
#define sz(v)  (int)(v).size()
#define all(v) (v).begin(), (v).end()
#define pi pair<int,int>
#define vi vector<int>
#define vvi vector<vector<int>>
#define vpi vector<pi>
#define pq priority_queue<int>
#define pqg priority_queue<int, vi, greater<int> >
#define fs first
#define sd second
#define pb push_back

struct Pizza{
      const int ROW, COL, MIN_ING, MAX_AREA; 
      vvi cells; 
      Pizza(int r, int c, int l, int h) : ROW(r), COL(c), MIN_ING(l), MAX_AREA(h) {}
};


int getSum(Pizza& pizza, int r_start, int c_start,  int r_end, int c_end){
      int sum = 0; 
      if(r_end>=pizza.ROW || c_end>=pizza.COL) return -1; 
      for(int i=r_start; i<=r_end;i++)
            for(int j=c_start; j<=c_end;j++)
                  sum += pizza.cells[i][j];
      return sum; 
}

bool isSliceOk(pi tl, pi rd, Pizza& pizza){
      int area = (rd.first - tl.first)*(rd.second - tl.second);
      if(area > pizza.MAX_AREA) return false; 
      int sum = 0; 
      for(int i=tl.first; i<rd.first; i++){
            for(int j=tl.second; j<rd.second; j++){
                  if(i>=pizza.ROW || j>=pizza.COL || pizza.cells[i][j]==-1) return false;
                  sum += pizza.cells[i][j]; 
            }
      }
      if(sum < pizza.MIN_ING || area-sum < pizza.MIN_ING) return false; 
      return true; 
}

vpi getPossibleSlices(Pizza& pizza){
      auto sorted = [](const pi& a, const pi& b){
            if(a.first==b.second && a.second==b.first && a.first!=a.second) return true; 
            if(a.first*a.second == b.first*b.second) 
                  return abs(a.first-a.second) < abs(b.first-b.second);
            return a.first*a.second > b.first*b.second;
      };
      set<pi, decltype(sorted)> possibleSlice(sorted); 
      
      for(int m=pizza.MAX_AREA; m>=pizza.MIN_ING*2; m--){
            int x = m/2;
            if(x*2 > m) x--; 
            for(int i=x; i>=1; i--){
                  pi a = make_pair(i,m/i);
                  possibleSlice.insert(a);
                  pi b = make_pair(m/i, i);
                  possibleSlice.insert(b);
            }
      }
      // debug() << imie(possibleSlice);
      return vpi(all(possibleSlice));
}

void getBestSliceNow(Pizza& pizza, vpi& possibleSlices, int r_now, int c_now, 
                                          vector<pair<pi, pi>>& res){
      auto sorted = [&](const pi& a, const pi& b){
            if(a.first*a.second == b.first*b.second){
                  int s1 = getSum(pizza, r_now, c_now, r_now+a.first, c_now+a.second);
                  int s2 = getSum(pizza, r_now, c_now, r_now+b.first, c_now+b.second);
                  return s1<s2;
            } return a.first*a.second > b.first*b.second;
      };
      set<pi, decltype(sorted)> possibleBestSlices(sorted); 
      for(auto& slice : possibleSlices){
            if(isSliceOk(make_pair(r_now, c_now), make_pair(r_now+slice.first, c_now+slice.second), pizza))
                  possibleBestSlices.insert(slice); 
      }
      if(possibleBestSlices.empty()) return;
      auto slice = possibleBestSlices.begin(); 
      for(int i=r_now; i<r_now+slice->first; i++)
            for(int j=c_now; j<c_now+slice->second;j++)
                  pizza.cells[i][j] = -1; 
      res.push_back(make_pair(make_pair(r_now,c_now), make_pair(r_now+slice->first-1, c_now+slice->second-1)));

}

int getTotalScore(Pizza &pizza, vector<pair<pi, pi>>& res){
      int score = 0; 
      for(auto& r: res){
            for(int i=r.first.first; i<=r.second.first; i++){
                  for(int j=r.first.second; j<=r.second.second; j++){
                        if(pizza.cells[i][j]==-1){
                              score=-1;
                              cerr<<"Soluzione invalida... "; 
                              return score;  
                        }
                        pizza.cells[i][j] = -1; 
                        score++;
                  }
            }
      }
      return score; 
}



int main(){
      ios_base::sync_with_stdio(false);
      cin.tie(NULL);
      
      int r,c,l,h; 
      cin >> r >> c >> l >> h; 
      Pizza pizza = Pizza(r,c,l,h);
      Pizza forScore = Pizza(r,c,l,h);
      pizza.cells = vvi(r, vi(c)); 
      forScore.cells = pizza.cells;
      vector<pair<pi, pi>> res;
      for(int i = 0; i <r; i++)
            for(int j = 0; j <c; j++){
                  char q; cin >> q; 
                  pizza.cells[i][j] = q=='M' ? 1 : 0;
            }
      vpi possibleSlices = getPossibleSlices(pizza);
      for(int i=0; i<pizza.ROW; i++){
            for(int j=0; j<pizza.COL; j++){
                  if(pizza.cells[i][j]==-1) continue; 
                  getBestSliceNow(pizza, possibleSlices, i, j, res);
            }
      }

      cout << res.size() << endl; 
      for(auto& re: res){
            cout << re.first.first << " " << re.first.second << " " << re.second.first << " " << re.second.second << endl;
      }
      cerr << "Score previsto: " << getTotalScore(forScore, res); 

      // Score totale:
      // example =     12
      // small   =     40
      // medium  =  49026
      // big     = 894899
      // ----------------
      // tot     = 943977

      // dopo aver compilato il file, per eseguirlo fare
      // ./main > "file.in" < "file.out"


      return 0;
}
      




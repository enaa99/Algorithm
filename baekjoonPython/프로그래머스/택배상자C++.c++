#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> q;
    int check = 0;
    for(int i =1; i<=order.size(); i++){
        q.push(i);
        
        while(q.size()>0 && q.top() == order[check]){
            answer +=1;
            check +=1;
            q.pop();
        }
        
        
    }
    
    return answer;
}
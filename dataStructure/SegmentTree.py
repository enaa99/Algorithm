num_lst = [1,2,5,3,9,6,5,3,2]
print('num_lst : ',num_lst)

#create segment tree
stree =[0 for x in range(4*len(num_lst))] # 길이는 넉넉하게 4N으로 설정

def merge(left, right):
    return left+right

def build(stree, node, left, right):
    # leaf node
    if left == right:
        stree[node] = num_lst[left]
        return stree[node]
    
    mid = left +(right-left)//2
    left_val = build(stree,2*node,left,mid)
    right_val = build(stree,2*node+1,mid+1,right)
    stree[node] = merge(left_val,right_val)
    return stree[node]

# stree의 1번 노드는 num_lst의 0번부터 len(num_lst)-1번까지의 정보를 담고 있다.
## 이 루트 노드를 시작으로 재귀 구조를 통해 자식 노드들로 쭉쭉 뻗어 나간다.
build(stree,1,0,len(num_lst)-1)
print(stree[1])
print(stree[2],stree[3])
print(stree[4],stree[5],stree[6],stree[7])
print(stree[8],stree[9],stree[10],stree[11],stree[12],stree[13],stree[14],stree[15])
print(stree[16],stree[17])
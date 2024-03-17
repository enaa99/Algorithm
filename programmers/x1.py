from collections import deque
def solution(P):
    answer = []

    for i in range(1,len(P)):
        if is_palindrome(P[0] + P[i]) or is_palindrome(P[i] + P[0]):
            q = deque()
            for j in range(i+1,len(P)):
                q.append(P[j])
            if pop_value_to_cmp(q):
                answer.append(P[i])

    return answer

def pop_value_to_cmp(q:deque):
    if len(q) <= 0: return True
    
    first_value = q.popleft()
    for value in q:
        if is_palindrome(first_value +value) or is_palindrome(value + first_value):
            q.remove(value)
            return pop_value_to_cmp(q)
        
    return False

def check_clear(P, idx):
    q = deque()
    for i in range(1,len(P)):
        if i == idx: continue
        q.append(P[i])
        break

    while q:
        a = q.popleft()
        b = q.popleft()

        if not is_palindrome(a+b) and not is_palindrome(b+a):
            return False

    return True

def is_palindrome(value):
    
    v_length = len(value)

    mid = v_length//2

    if v_length%2 == 0:
        if value[mid-1] != value[mid]:
            return False
        left = mid - 2
        right = mid + 1
    else:
        left = mid - 1
        right = mid + 1
    
    while left>=0 and right < v_length:
        if value[left] != value[right]:
            return False
        left -= 1
        right += 1
    return True

arr = ["21","123","111","11"]
print(solution(arr))

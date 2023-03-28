from collections import defaultdict
def solution(n, c, a):
    freq = defaultdict(int)
    for word in a:
        freq[word] +=1
        

    sorted_words = sorted(freq.keys(), key=lambda x:freq[x], reverse=True)

    indices = defaultdict(list)
    for i, word in enumerate(a):
        indices[word].append(i)
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if a[i] == a[j]:
                dp[i][j] = dp[i+1][j+1] +1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    answer = 0
    user_words = set()
    for i in range(n-1):
        word1, word2 = sorted_words[i], sorted_words[i+1]

        for used_word in user_words:
            indices[used_word] = []

        if word1 in indices:
            available_indices = [idx for idx in indices[word1] if idx <n-1 and a[idx+1] == word2]
            if available_indices:
                user_words.add(word1)
                answer += c[i]*(dp[available_indices[0][available_indices[0]+1]])
        if word2 in indices:
            available_indices = [idx for idx in indices[word2] if idx>0 and a[idx-1] == word1]
            if available_indices:
                used_word.add(word2)
                answer += c[i]*(dp[available_indices[0][available_indices[0]-1]])

    return answer

solution(2,[6],["baby","shark"])
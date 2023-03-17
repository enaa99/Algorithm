def solution(cards):
    cards = [c-1 for c in cards]
    n_cards = len(cards)
    answer = [[] for _ in range(n_cards)]
    visit = [0 for _ in range(n_cards)]
    for i in range(n_cards):
        if visit[i]:
            continue
        tmp = i
        answer[i].append(cards[tmp])
        visit[tmp] = 1
        while not visit[cards[tmp]]:
            visit[cards[tmp]] = 1
            answer[i].append(cards[tmp])
            tmp = cards[tmp]
    answer.sort(key=lambda x:-len(x))
    return len(answer[0]) * len(answer[1])
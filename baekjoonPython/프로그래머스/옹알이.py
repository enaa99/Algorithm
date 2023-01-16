
def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for babies in baby:
            if babies*2 in b: break
            b = b.replace(babies,'')
        if len(b.strip()) == 0:
            answer +=1
    return answer



solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
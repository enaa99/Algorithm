from collections import defaultdict
import math
def solution(str1, str2):
    
    # 교집합/합집합
    # 둘중 하나가 0이라면 1
    # 문자열 두개씩 끊어서 교직합
    # 영문자만 허용, 기타 공백 or 숫자, 특수문자 버린다
    # 같은게 두개 라면 두개 카운트
    # 대소문자 무시
    # 65536 곱하고 소수점아래 버리고 출력
    
    a_dic = defaultdict(int)
    b_dic = defaultdict(int)
    
    
    def make_dic(data,dic):
        for i in range(1,len(data)):
            k = data[i-1]+data[i]
            if k.isalpha():
                k = k.lower()
                dic[k] +=1 
        
    
    make_dic(str1,a_dic)
    make_dic(str2,b_dic)
    
    if not a_dic or not b_dic:
        return 65536
    
    # 두개 원소 구했고, 교집합 합집합 구하기
    
    tmp1 = 0
    
    
    # 우슨 b의 사이즈만큼 합집합 사이즈로 잡아준다
    tmp2 = sum(b_dic.values())
    
    
    for key in a_dic.keys():
        
        a = a_dic[key]
        b = b_dic[key]
        # 존재한다면
        if b:
            # 교집합은? 적은 개수
            
            tmp1 += min(a,b)
            
            # 합집합은? b의 개수만큼 이미 더해놨으니 부족한만큼만
            if a > b:
                tmp2 += a-b

        else: # 존재하지 않는다면?  a_dic개수만큼 늘려주면 된다~
            tmp2 += a
    
    
    if tmp1 == 0 or tmp2 == 0:
        return 65536
    
    return math.floor(tmp1/tmp2*65536) 
    
    
solution("aa1+aa2", "AAAA12")
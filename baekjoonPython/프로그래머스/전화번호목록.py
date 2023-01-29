def solution(phone_book):
    
    
    phone_book.sort()
    
    
    
    for number in range(1,len(phone_book)):
        if phone_book[number-1] == phone_book[number][:len(phone_book[number-1])]:
            return False
        # len_num = len(phone_book[number])
        # for num in range(number+1,len(phone_book)):
        #     if phone_book[number] == phone_book[num][:len_num]:
        #         return False
            
        #     if phone_book[number][0] != phone_book[num][0]:break
    
    return True
    
    
    


solution(["12","123","1235","567","88"])
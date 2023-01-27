from collections import defaultdict
def solution(fees,records):
    answer = []
    
    
    # fees = 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    # records = 시간(시:분), 차량 번호, 내역
    
    # 출차된 내열이 없다면 23시 59분에 출차된 것으로 간주한다
    # 차량번호가 작은 순서대로
    
    # 단위시간으로 나뉘어지지 않으면 올림처리
    car_info = defaultdict(int)
    record_car = defaultdict(str)
    time_car = defaultdict(int)
    
    for tmp in records:
        time,car_num,record = tmp.split()
        
        
        if record == 'IN':
            times = time.split(':')
            
            record_car[car_num] = 'IN'
            a,b = int(times[0]) * 60,int(times[1])
            
            car_info[car_num] = a + b
        else:
            times = time.split(':')
            
            record_car[car_num] = 'OUT'
            a,b = int(times[0])*60,int(times[1])
            
            time_car[car_num] += a + b - car_info[car_num]
    
    for key in record_car.keys():
        if record_car[key] == 'IN':
            record_car[key] = 'OUT'
            a,b = 23*60 ,59
            time_car[key] += a+b - car_info[key]
        
        if time_car[key] <= fees[0]:
            answer.append([key,fees[1]])
        else:
            check = (time_car[key]-fees[0])
            k = check//fees[2]
            less = check%fees[2]
            if less > 0:
                k += 1
            answer.append([key,fees[1]+k*fees[3]])
    
    answer.sort()
    tmp =[]
    for key,fee in answer:
        tmp.append(fee)
    
    return tmp

solution([1, 461, 1, 10],["00:00 1234 IN"])
from datetime import datetime, timedelta

def time_str_to_timedelta(time_str):
    m, s = map(int, time_str.split(':'))
    return timedelta(minutes=m, seconds=s)

def time_cal(video_len, cur, cm,command):
    if command == "next":
        if cur + cm >= video_len:
            return video_len
        else:
            return cur + cm
    else:
        if cur <= cm:
            return time_str_to_timedelta("00:00")
        else:
            return cur - cm

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # prev -> 10초전 이동, 10초 미만인 경우 처음 위치
    # next -> 10초 후 이동, 10초 미만인 경우 마지막 위치
    # 오프닝 건너뛰기 (op_start<= 현재 재생 위치 <= op_end) 자동으로 오프닝 끝나는 위치 이동
    
    # 동영상 길이 video_len
    # 수행되기 직전 재생위치 pos
    # 오프닝 시작 op_start, 오프닝 끝 op_end
    # 입력 배열 commands
    # return mm:ss
    
    
    cur = time_str_to_timedelta(pos)
    cm = time_str_to_timedelta("00:10")
    v_len = time_str_to_timedelta(video_len)
    op_s = time_str_to_timedelta(op_start)
    op_e = time_str_to_timedelta(op_end)
    
    for command in commands:
        if cur >= op_s and cur <= op_e:
            cur = op_e
            
        cur = time_cal(v_len, cur, cm, command)
        
        if cur >= op_s and cur <= op_e:
            cur = op_e
        
    cur = str(cur).split(':')
    return f"{cur[1]}:{cur[2]}"
def solution(id_list, report, k):
    answer = []
    
    
    report_dic = {name:[] for name in id_list}
    
    get_id = {name:0 for name in id_list}
    
    report_id = {name:0 for name in id_list}

    
    for name in report:
        fid,tid = name.split()
        if tid not in report_dic[fid]:
            report_dic[fid].append(tid)
            get_id[tid] += 1
    
    
    for key in report_dic.keys():
        for i in report_dic[key]:
            if get_id[i] >=k:
                report_id[key] +=1
                
    
    for val in report_id.values():
        answer.append(val)
    
    
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
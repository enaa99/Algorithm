def solution(files):
    answer = []
    
    
    check_file = [['','','']for _ in range(len(files))]
    
    
    for file in range(len(files)):
        flag = 0
        for i in range(len(files[file])):
            if not flag and not files[file][i].isdigit():
                check_file[file][0] += files[file][i]
            elif files[file][i].isdigit():
                check_file[file][1] += files[file][i]
                flag =1
            else:
                check_file[file][2] += files[file][i:]
                break
    
    check_file.sort(key=lambda x:(x[0].lower(),int(x[1])))
    for i in range(len(check_file)):
        answer.append(check_file[i][0] + check_file[i][1] + check_file[i][2])
    
    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])


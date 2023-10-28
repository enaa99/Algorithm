from collections import defaultdict

def autocompletes(inputs):
    input_dict = defaultdict(int)
    count = 0
    
    for i in inputs:
        input_set = set()
        for k in i:
            input_set.add(k)
        for j in input_set:
            if input_dict[j] == 0:
                input_dict[j] +=1
            else:
                count +=1
    return count

autocompletes(['000','1110','01','001','110','11'])
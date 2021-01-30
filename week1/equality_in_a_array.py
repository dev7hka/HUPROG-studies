def equalizeArray(arr):
    dic = {}
    for number in arr:
        if dic.__contains__(number):
            dic[number]+=1
        else:
            dic[number]=1
    return len(arr) - max(dic.values())

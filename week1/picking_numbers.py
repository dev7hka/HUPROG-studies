def pickingNumbers(a):
    # Write your code here
    dic = dict()
    for _ in a:   # count every number
        if dic.__contains__(_):
            dic[_]+=1
        else:
            dic[_] = 1
    longest = 0
    for i,j in dic.items(): # check every consecutive number count, e.g : (1,2) (2,3) and so on
        tmp = dic[i]
        if dic.__contains__(i+1):
            tmp+= dic[i+1]
        if tmp > longest:
            longest = tmp
    return longest

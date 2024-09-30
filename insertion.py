def insertion(ls):
    for i in range(1,len(ls)):
        j = i
        while j > 0 and ls[j]<ls[j-1]:
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp
            j-=1
    return ls

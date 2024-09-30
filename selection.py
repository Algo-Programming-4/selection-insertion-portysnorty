def selection(ls):
    for i in range(len(ls)-1):  
        index_smallest = i
        # finds the smallest index
        for j in range(i+1, len(ls)):
            if ls[index_smallest] > ls[j]:
                index_smallest = j
        
        temp = ls[i]
        ls[i] = ls[index_smallest]
        ls[index_smallest] = temp
    return ls

#bubble(list) - > sorted ist
def bubble(ls):
    for i in range(len(ls) - 1):  
        # sorts it faster by checking if already sorted early
        shortCut = True
        for j in range(len(ls) - i - 1):  
            a = ls[j]
            b = ls[j + 1] 
            if a > b:  
                ls[j] = b 
                ls[j + 1] = a
                shortCut = False
        if(shortCut):
            print("saved you ",len(ls)-i-1," recurtions")
            break
    return ls

#selection(list) -> sorted list
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

#insertion(list) > sorted list
def insertion(ls):
    for i in range(1,len(ls)):
        j = i
        while j > 0 and ls[j]<ls[j-1]:
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp
            j-=1
    return ls

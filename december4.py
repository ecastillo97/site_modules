
def h_index(paper, citations):
    temp = paper
    index = 0
    prev_list = []
    while temp != 0:
        temp_list = [num for num in citations if num >= temp]
        print(temp_list, temp)
        if temp == len(temp_list) or len(temp_list) > len(prev_list): # test
            index = temp
        else:
            prev_list = list(temp_list)
        temp -=1
    return index

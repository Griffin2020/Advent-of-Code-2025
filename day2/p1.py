def find_repetition(low, high):
    index = low
    total = 0
    #print("length", len(str(low)))
    while index <= high:
        str_index = str(index)
        seg_len = len(str(index)) // 2
        first_half, second_half = str_index[:seg_len], str_index[-seg_len:]
        if first_half == second_half and len(str_index) % 2 == 0:
            #print(first_half, second_half)
            total += index

        
        index += 1

    return total
with open("input", 'r') as file:
    counter = 0
    file_contents = file.readlines()
    
    ranges = file_contents[0].split(",")
    for item in ranges:
        low, high = int(item.split("-")[0]), int(item.split("-")[1])
        #print(item, low, high)
        counter += find_repetition(low, high)
    print("total:", counter)
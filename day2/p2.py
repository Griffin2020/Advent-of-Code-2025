def find_repetition(low, high):
    index = low
    total = 0

    while index <= high: # loop through range of ints
        #print(index)            
        str_index = str(index)

        #Only test if length of string is divisible by substring:
        if test_repeating(str_index):
            total += index
            

    
            #print(s)
            
        index += 1

    return total
def test_repeating(s):
    n = len(s)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            if s == s[:i] * (n // i):
                print("found match of", s, "and", s[:i])
                return True
    return False

with open("input", 'r') as file:
    counter = 0
    file_contents = file.readlines()
    
    ranges = file_contents[0].split(",")
    for item in ranges:
        low, high = int(item.split("-")[0]), int(item.split("-")[1])
        counter += find_repetition(low, high)
    print("total:", counter)
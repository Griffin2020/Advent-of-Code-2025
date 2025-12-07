
with open("input", 'r') as file:
    combo = 50
    counter = 0
    file_contents = file.readlines()
    
    for line in file_contents:
        num = int(line[1:])
        if line[:1] == "L":
            num = num * -1
        combo = (combo + num) % 100
        if combo == 0:
            counter += 1
    print(counter)
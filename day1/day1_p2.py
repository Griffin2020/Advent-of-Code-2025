with open("input", "r") as file:
    combo = 50
    counter = 0

    for raw in file:
        line = raw.strip()
        direction = line[0]
        m = int(line[1:])  

        start = combo 

        if direction == "R":
            # first step that hits 0 occurs after k steps where (start + k) % 100 == 0
            first = (100 - start) % 100
            if first == 0:
                first = 100
            if m >= first:
                counter += 1 + (m - first) // 100
        else: 
            first = start % 100
            if first == 0:
                first = 100
            if m >= first:
                counter += 1 + (m - first) // 100

        # update dial position
        if direction == "R":
            combo = (combo + m) % 100
        else:
            combo = (combo - m) % 100



    print("Total:", counter)
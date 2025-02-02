def solve(numheads, numlegs):
    # x - rabbits, y - chickens
    for x in range (0, numheads+1):
        for y in range (0, numlegs+1):
            if x+y == numheads and 4*x + 2*y == numlegs:
                print(x, y)

solve(35, 94) # 12 23
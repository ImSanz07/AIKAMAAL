def tower_of_hanoi(n,source,auxillary,target):

    if n == 1:
        print("Move disk 1 from",source,"to",target)
        return
    tower_of_hanoi(n-1,source,target,auxillary)
    print("Move disk",n,"from",source,"to",target)
    tower_of_hanoi(n-1,auxillary,source,target)

n = 3
tower_of_hanoi(n,'A','B','C')
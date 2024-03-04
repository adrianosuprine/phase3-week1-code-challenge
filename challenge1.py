def box_bricks(A):
    target_bricks = 10
    total_bricks = sum(A)
    moves = 0
    print(total_bricks)
    # Not possible to have exactly 10 bricks in every box
    if total_bricks % len(A) != 0:
        return -1  

    avg_bricks = total_bricks // len(A)
    print(avg_bricks)

    for i in range(len(A)):
        while A[i] > avg_bricks:
            # checks if its the last box
            if i < len(A) - 1:
                if A[i + 1] < target_bricks:
                    A[i + 1] += 1
                elif A[i - 1] < target_bricks:
                    A[i - 1] += 1
                else:
                    
                    A[i - 1] += 1
            else:
                if A[i - 1] < target_bricks:
                    A[i - 1] += 1
            A[i] -= 1
            
            moves += 1

    return moves


print(box_bricks([7, 15, 10, 8]))   # Output: 7


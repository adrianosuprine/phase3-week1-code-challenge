def box_bricks(A):
    target_bricks = 10
    total_bricks = sum(A)
    moves = 0
   
    # Not possible to have exactly 10 bricks in every box
    if total_bricks % len(A) != 0:
        return -1  
    
    for i in range(len(A)-1):
        difference = A[i] -target_bricks
    # distributing the bricks to the boxes to attain an equal no. of bricks   
        A[i + 1] += difference
    # determining amount of moves to attain that
        moves += abs(difference)
       
    return moves
  


print(box_bricks([7, 15, 10, 8]))   
# Output: 7
print(box_bricks([11,10,8,12,8,10,11]))
# Output: 6
print(box_bricks([7, 14,10])) 
# Output: -1

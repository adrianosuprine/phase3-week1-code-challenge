#  for calculating the sum of a particular digit 
# example 51 => 6, 71 => 8 17 => 8 
def digit_sum(num):
    print (sum(map(int, str(num))))

def digit_sum_solution(A):
    max_sum = -1
    # creating empty dict 
    digit_sums_dict = {}

    for num in A:
        current_sum = digit_sum(num)

        if current_sum in digit_sums_dict:
            pair_sum = num + digit_sums_dict[current_sum]
            # calculating the maximum sum of digits in A 
            max_sum = max(max_sum, pair_sum)
        else:
            digit_sums_dict[current_sum] = num

    print(max_sum)


digit_sum_solution([51, 71, 17, 42])  


def solution(A):
    
    def sum_of_digits(number):
        return sum(int(digit) for digit in str(number))

    max_sum = -1
    sums_map = {}

    for num in A:
        sum_digits = sum_of_digits(num)
        
        if sum_digits in sums_map:
            max_sum = max(max_sum, num + sums_map[sum_digits])
        if sum_digits not in sums_map or num > sums_map[sum_digits]:
            sums_map[sum_digits] = num

    return max_sum


import math

def find_csum(num):
    result = []
    sqrt_val = int(math.sqrt(2 * num))
    for n in range(sqrt_val, 1, -1):
        nu = 2 * num - n * (n + 1)
        d = 2 * (n + 1)
        if nu % d == 0:
            start = int(nu / d)
            end = start + n
            result.append(tuple(range(start, end + 1)))
    result.append(num)
    return result

# SOMEONE OPTIMIZE THIS FOR ME PLEASE :SOB:
# its O(sqrt(N)) but still taking 37.3222sec to do 10^15

try:
    while(1):
        print(len(find_csum(int(input()))))
except EOFError as e:
   print(end="")

# trash code

# def find_csum(num):
#     result = []
#     start, end = 1, 1
#     current_sum = 1
#     while start <= num // 2:
#         if current_sum < num:
#             end += 1
#             current_sum += end
#         elif current_sum > num:
#             current_sum -= start
#             start += 1
#         else:
#             result.append(tuple(range(start, end+1)))
#             current_sum -= start
#             start += 1
#     result.append(num)
#     return result
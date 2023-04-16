# try:
#     while(1):
#         n, m, k = map(int, input().split())
#         girls = ['G'] * n + ['K'] * m

#         def killing(lst, k):
#             killed = []
#             new_lst=[]
#             count, lastN, kill = 1, 0, ""
#             for number, type in enumerate(lst, 1):
#                 if number == k*count:
#                     killed.append(type)
#                     if len(killed) == 2:
#                         lastN=number-3
#                         count= 1
#                         if killed [0] == killed[1]:
#                             kill="G"
#                         else:
#                             kill="K"
#                         killed=[]
#                     count+=1
#                 else:
#                     new_lst.append(type)
#             new_lst.insert(lastN, kill)
#             return new_lst
        
#         print(killing(girls, k))
        
# except EOFError as e:
#    print(end="")



#1 cпособ

# def strcounter(s): # слож 0(2*N) ~ 0(N)
#     adict = {}
#     for i in s:
#         adict[i] = adict.get(i, 0) + 1
#         for j in adict:
#             print(j, adict[j])
#
# strcounter('asfjjfhlds')

#_______________________________________________

# 2 способ

# def strcounter(s): # cлож   O(N**2)
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 counter += 1
#         print(sym, counter)
#
#
#
# strcounter('asfjjfhlds')
#_______________________________________________

# 3 способ

def strcounter(s): #сложность (N*M)
   for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
            print(sym, counter)

strcounter('abbbsdffb')
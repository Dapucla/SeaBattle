# ---------РЕШЕНИЕ НОМЕР 1----------
# reader = open('input.txt','r')
# inputValue = [int (n) for n in reader.readline().strip().split(" ")]
# reader.close()

# def inversions(list):
#     return merge_inversion(list)[1]

# def merge_inversion(list):
#     if len(list) <= 1:
#         return list, 0
#     middle = int(len(list) / 2)
#     left, a = merge_inversion(list[:middle])
#     right, b = merge_inversion(list[middle:])
#     result, c = merge_split_inversion(left, right)
#     return result, (a + b + c)


# def merge_split_inversion(left, right):
#     result = []
#     count = 0
#     i, j = 0, 0
#     left_len = len(left)
#     while i < left_len and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             count += left_len - i
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result, count


# result = str(inversions(inputValue))

# writer = open('output.txt', 'w')
# writer.write(result)
# writer.close()



# ---------РЕШЕНИЕ НОМЕР 2----------
# def getInvCount(arr, n):
  
#     inv_count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if (arr[i] > arr[j]):
#                 inv_count += 1
  
#     return inv_count
  
# # Driver Code
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# print("Number of inversions are",getInvCount(arr, n))




# ---------РЕШЕНИЕ НОМЕР 3----------
# import os, sys
# reader = open('input.txt','r')
# arr = [int (n) for n in reader.readline().strip().split(" ")]
# reader.close()

# def mergeSortInversions(arr):
#     if len(arr) == 1:
#         return arr, 0
#     else:
#         a = arr[:len(arr)/2]
#         b = arr[len(arr)/2:]
#         a, ai = mergeSortInversions(a)
#         b, bi = mergeSortInversions(b)
#         i = 0
#         j = 0
#         inversions = 0 + ai + bi
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             i += 1
#         else:
#             j += 1
#             inversions += (len(a)-i)
#     return  inversions

# result = str(mergeSortInversions(arr))  
# print(res)
# writer = open('output.txt', 'w')
# writer.write(result)
# writer.close
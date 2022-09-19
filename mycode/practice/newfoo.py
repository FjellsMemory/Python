# def string_bits(str):
#     list = []
#     for x in str:
#         list.append(x)
#     print(list)
#     newlist = []
#     for x in list:
#         print(x, list.index(x))
#         if list.index(x) % 2 == 0:
#             newlist.append(x)
#     str = "".join(item for item in newlist)
#     return str

# def new_str_bits(str):
#     result = ""
#     for x in range(len(str)):
#         if x % 2 == 0:
#             result += str(x)
#     return result

# def string_splosion(str):
#     len1 = len(str)
#     list = []
#     for n in range(len1, 0, -1):  # range(0, 7)
#         for x in range(len(str) + 1 - n):
#             list.append(str[x])  # okay but do this without print
#     str = "".join(list)
#     return str


# mylist = string_splosion("biscuit")
# print(mylist)

# def array_front9(nums):
#     counter = 0
#     len1 = len(nums)
#     if len(nums) > 3:
#         for n in nums:
#             if n == 9 and nums.index(n) < 4:
#                 counter += n
# #   else:
# #     for n in nums:
# #       if nums[n] < len1:
# #         if n == 9:
# #           counter += n
# #   return counter

# array_front9([1, 2, 5, 7, 9, 9, 4, 9])

def array123(nums):
    string_ints = [str(int) for int in nums]
    "".join(string_ints)
    if "123" in string_ints:
        return True
    else:
        return False

mybool = array123([1, 1, 2, 1, 2, 3])
print(mybool)
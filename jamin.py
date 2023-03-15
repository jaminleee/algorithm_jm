def solution(nums):
    answer = 0
    hash = {}

    for i in nums:
        hash[i] = 1  #중복제거. len(hash) => 종류

    if len(hash) > len(nums)//2 :
        return len(nums)//2
    return len(hash)
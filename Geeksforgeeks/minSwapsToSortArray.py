def minSwaps(nums):
      

    count_swaps = 0

    n = len(nums)
 
    sorted_nums = nums.copy()
    sorted_nums.sort()


    indexes_nums = {}
       
    for i in range(n):
           indexes_nums[nums[i]] = i
            
            
    for i in range(n):
    
            if (nums[i] != sorted_nums[i]):
               count_swaps += 1
               current_num = nums[i]
    
               nums[i], nums[indexes_nums[sorted_nums[i]]] = nums[indexes_nums[sorted_nums[i]]], nums[i]

               indexes_nums[current_num], indexes_nums[sorted_nums[i]] = indexes_nums[sorted_nums[i]], i

                
    return count_swaps
    

nums = [7,16,14,17,6,9,5,3,18]

# nums.sort()
# print(nums)
# nums = [10, 19, 6, 3, 5]
# nums = [2, 8, 5, 4]
# nums = [1,4,3,2]
print(minSwaps(nums))
    

def has_33(nums):
    check = False
    if check: return check
    
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            check = True

    return check

print(has_33([1, 3, 3]))         # → True
print(has_33([1, 3, 1, 3]))      # → False
print(has_33([3, 1, 3]))         # → False
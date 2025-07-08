nums=list(map(int,input("Enter nos :").split()))
if nums:
    largest = nums[0]
for num in nums[1:]:
        if num > largest:
            largest = num
print (largest)
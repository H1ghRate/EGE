with open('9_11658.csv') as f:
    idx_max = 0
    idx = 0


    for line in f:
        idx += 1
        nums = list(map(int, line.split(';')))

        nums3 = [num for num in nums if nums.count(num) == 3]

        nums1 = [num for num in nums if nums.count(num) == 1]

        if len(nums1) == 4 and len(nums3) == 3:
            if nums3[0] >= (sum(nums) // 7):
                idx_max = idx
    
    print(idx_max)


def max_subarray_sum(nums):
    #find largest contiguous sum from subarray
    #comparison between max of subarray and max of subarray found so far

    #we're initialising the variable to neg infinity
    maxfound= float('-inf')
    maxcurrent= 0
    start= 0
    end= 0
    startcurrent= 0

    for i in range(len(nums)):
        maxcurrent+= nums[i]
        if maxcurrent > maxfound:
            maxfound = maxcurrent
            start = startcurrent
            end = i

        if maxcurrent < 0:
            maxcurrent = 0
            startcurrent = i + 1

    max_subarray = nums[start:end+1]  # Extract the maximum subarray

    return maxfound

def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(result)  # should print 6, based on the subarray [4, -1, 2, 1]


if __name__ == '__main__':
    main()

def twosum():
    a = input('Please input nums spit with comma: ')
    nums = []
    for i in a.split(','):
        nums.append(int(i))
    print('The nums you input is %s' % nums)
    target = int(input('Please input integer target: '))
    print('The target you input is %s' % target)
    m = 0
    result_found = 0
    for m in list(range(0, len(nums), 1)):
        for n in list(range(m + 1, len(nums), 1)):
            target_test = nums[m] + nums[n]
            if target_test == target:
                print("nums[%d] + nums[%d] = %d" % (m, n, target))
                result_found = 1
    if 1 == result_found:
        print("Job done!")
    else:
        print("No such two elements found in list nums !")

if __name__=='__main__':
    twosum()
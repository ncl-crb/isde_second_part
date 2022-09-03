def sum_skip(v, el_to_skip):
    sum = 0
    i = 0
    while i < len(v):
        if v[i] != el_to_skip:
            sum += v[i]
            i += 1
        else:
            i += 2
    return sum


if __name__ == '__main__':
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]


    print(sum_skip(nums1, 13) == 3)
    print(sum_skip(nums2, 13) == 3)
    print(sum_skip(nums3, 13) == 2)
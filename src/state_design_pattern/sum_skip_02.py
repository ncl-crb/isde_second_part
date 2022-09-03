
def sum_skip(v, el_to_skip=13):
    _state = 0
    _sum = 0

    i = 0
    while i < len(v):
        if _state == 0:
            if v[i] != el_to_skip:
                _sum += v[i]
                i += 1
            else:
                _state = 1
                i += 1
        elif _state == 1:
            if v[i] != el_to_skip:
                i += 1
                _state = 0
            else:
                i += 1
    return _sum


if __name__ == '__main__':
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    print(sum_skip(nums1, 13) == 3)
    print(sum_skip(nums2, 13) == 3)
    print(sum_skip(nums3, 13) == 2)

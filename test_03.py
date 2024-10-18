# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

import copy


def rotate_right_by_k(nums: list[int], k: int) -> None:
    # approach 01
    local_array = copy.deepcopy(nums)

    # approach 02
    local_array = []
    for val in nums:
        local_array.append(val)

    for i in range(len(nums)):
        new_index = (i + k) % len(nums)
        nums[new_index] = local_array[i]


def main() -> None:
    my_list = [1, 2, 3, 4, 5]
    rotate_right_by_k(my_list, 3)
    print(my_list)


if __name__ == '__main__':
    main()

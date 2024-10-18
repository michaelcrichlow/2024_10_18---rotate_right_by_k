package test

import "core:fmt"
print :: fmt.println

main :: proc() {

	my_list := [?]int{1, 2, 3, 4, 5}
	rotate_right_by_k(my_list[:], 2)
	print(my_list)

}

rotate_right_by_k :: proc(nums: []int, k: int) {
	local_array := make([dynamic]int)
	defer delete(local_array)

	for val in nums {
		append(&local_array, val)
	}

	for i in 0 ..< len(nums) {
		new_index := (i + k) % len(nums)
		nums[new_index] = local_array[i]
	}
}

package main

import "fmt"

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	first := binsearch(nums, target, true)
	if first == -1 {
		return []int{-1, -1}
	}
	last := binsearch(nums, target, false)

	return []int{first, last}
}

func binsearch(nums []int, target int, isleft bool) int {
	left, right := 0, len(nums)-1
	bound := -1

	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			bound = mid
			if isleft {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return bound
}

func main() {
	// nums := []int{1}
	// target := 1
	nums := []int{5, 7, 7, 8, 8, 10}
	target := 6
	fmt.Print(searchRange(nums, target))
}

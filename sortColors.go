package main

import (
	"fmt"
)

func sortColors(nums []int) {
	low, mid, high := 0, 0, len(nums)-1
	for mid <= high {
		switch nums[mid] {
		case 0:
			nums[low], nums[mid] = nums[mid], nums[low]
			low++
			mid++
		case 1:
			mid++
		case 2:
			nums[high], nums[mid] = nums[mid], nums[high]
			high--
		}
	}
}

func main() {
	nums := []int{1, 2, 0}
	sortColors(nums)
	fmt.Println(nums)
}

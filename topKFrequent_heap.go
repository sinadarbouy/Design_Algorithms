package main

import (
	"container/heap"
	"fmt"
)

type Frequency struct {
	num  int
	freq int
}

type MinHeap []Frequency

func (h MinHeap) Len() int               { return len(h) }
func (h MinHeap) Less(i int, j int) bool { return h[i].freq < h[j].freq }
func (h MinHeap) Swap(i int, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Frequency))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
	frequencyMap := make(map[int]int)
	for _, num := range nums {
		frequencyMap[num]++
	}

	h := &MinHeap{}
	heap.Init(h)

	for num, freq := range frequencyMap {
		heap.Push(h, Frequency{num: num, freq: freq})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	result := make([]int, k)
	for i := 0; i < k; i++ {
		result[i] = heap.Pop(h).(Frequency).num
	}

	return result

}

func main() {
	nums := []int{1, 1, 1, 2, 2, 3}
	k := 2

	fmt.Print(topKFrequent(nums, k))
}

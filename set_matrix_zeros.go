package main

import "fmt"

func setZeroes(matrix [][]int) {
	m := len(matrix)
	if m == 0 {
		return
	}
	n := len(matrix[0])

	// Check if the first row and first column need to be set to zero
	firstRowZero := false
	firstColZero := false

	for i := 0; i < n; i++ {
		if matrix[0][i] == 0 {
			firstRowZero = true
			break
		}
	}

	for i := 0; i < m; i++ {
		if matrix[i][0] == 0 {
			firstColZero = true
			break
		}
	}

	// Use first row and first column to mark zeroes
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	// Set the elements to zero based on marks
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	// Zero out the first row if needed
	if firstRowZero {
		for i := 0; i < n; i++ {
			matrix[0][i] = 0
		}
	}

	// Zero out the first column if needed
	if firstColZero {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}

}

func main() {
	matrix := [][]int{
		{0, 1, 2, 0},
		{3, 4, 5, 2},
		{1, 3, 1, 5},
	}

	setZeroes(matrix)
	fmt.Println(matrix)
}

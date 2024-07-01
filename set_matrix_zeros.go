package main

import "fmt"

func setZeroes(matrix [][]int) {
	m := len(matrix)
	n := len(matrix[0])

	row_zero := false
	col_zero := false

	for i := 0; i < n; i++ {
		if matrix[0][i] == 0 {
			row_zero = true
		}
	}

	for i := 0; i < m; i++ {
		if matrix[i][0] == 0 {
			col_zero = true
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	if col_zero == true {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}

	if row_zero == true {
		for i := 0; i < n; i++ {
			matrix[0][i] = 0
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

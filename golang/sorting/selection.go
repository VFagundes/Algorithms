package main

import (
	"fmt"
)

const TOTAL_SIZE = 10

var data = func() *[]int {

	L := make([]int, TOTAL_SIZE)
	for i := TOTAL_SIZE - 1; i >= 0; i-- {
		L[i] = len(L) - i
	}
	return &L
}

func main() {
	L := data()
	selectionSort := func(l *[]int) *[]int {
		for i := 0; i < len(*l); i++ {
			for j := i + 1; j < len(*l); j++ {
				if (*l)[i] > (*l)[j] {
					(*l)[i] ^= (*l)[j]
					(*l)[j] ^= (*l)[i]
					(*l)[i] ^= (*l)[j]
				}
			}

		}

		return l
	}

	fmt.Println(selectionSort(L))
}

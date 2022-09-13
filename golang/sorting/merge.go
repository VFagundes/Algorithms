package main

import (
	"fmt"
	"math/rand"
)

const TOTAL_SIZE = 10

var data = func() *[]int {

	L := make([]int, TOTAL_SIZE)
	for i := TOTAL_SIZE - 1; i >= 0; i-- {
		L[i] = rand.Intn(300)
	}
	return &L
}

func merge(a []int, b []int) []int {
	final := []int{}
	i := 0
	j := 0

	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			final = append(final, a[i])
			i++
		} else {
			final = append(final, b[j])
			j++
		}
	}
	for ; i < len(a); i++ {
		final = append(final, a[i])
	}
	for ; j < len(b); j++ {
		final = append(final, b[j])
	}
	return final
}

func mergeSort(items []int) []int {
	if len(items) < 2 {
		return items
	}
	first := mergeSort(items[:len(items)/2])
	second := mergeSort(items[len(items)/2:])
	return merge(first, second)
}

func main() {
	L := data()
	fmt.Println(L)
	mergeSort(*L)

	fmt.Println(L)
}

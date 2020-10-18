package main

import "fmt"

func rangedemo() {
	s := "Hello鸠与鸩"
	for i, v := range s {
		fmt.Printf("%d %c\n", i, v)
	}
}

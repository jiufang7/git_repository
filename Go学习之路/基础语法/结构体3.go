//+build ignore

package main

import (
	"fmt"
)

func main() {
	var user struct {
		Name string
		Age  int
	}
	user.Name = "小王子"
	user.Age = 18
	fmt.Printf("%#v\n", user)
	//在定义一些临时数据结构等场景下还可以使用匿名结构体。
}

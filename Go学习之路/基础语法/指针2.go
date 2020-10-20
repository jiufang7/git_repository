//+build ignore

package main

import "fmt"

func main() {
	//指针取值
	a := 10
	b := &a                          // 取变量a的地址，将指针保存到b中
	fmt.Printf("type of b:%T\n", b)  //type of b:*int
	c := *b                          // 指针取值（根据指针去内存取值）
	fmt.Printf("type of c:%T\n", c)  //type of c:int
	fmt.Printf("value of c:%v\n", c) //value of c:10
}

/*
 取地址操作符&和取值操作符*是一对互补操作符，&取出地址，*根据地址取出地址指向的值。

 变量、指针地址、指针变量、取地址、取值的相互关系和特性如下：

 对变量进行取地址（&）操作，可以获得这个变量的指针变量。
 指针变量的值是指针地址。
 对指针变量进行取值（*）操作，可以获得指针变量指向的原变量的值。
*/

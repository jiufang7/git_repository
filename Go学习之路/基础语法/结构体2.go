//+build ignore

package main

import "fmt"

type person struct {
	name string
	city string
	age  int8
}

func main() {
	var p1 person
	p1.name = "沙河娜扎"
	p1.city = "北京"
	p1.age = 18
	fmt.Printf("p1=%v\n", p1)  //p1={沙河娜扎 北京 18}
	fmt.Printf("p1=%#v\n", p1) //p1=main.person{name:"沙河娜扎", city:"北京", age:18}
}

/*
 只有当结构体实例化时，才会真正地分配内存。也就是必须实例化后才能使用结构体的字段。
 结构体本身也是一种类型，我们可以像声明内置类型一样使用var关键字声明结构体类型。
*/

package main

import "fmt"

//导入语句

//声明变量
// var name string
// var age int

//函数为只能放置标识符（变量、常量、函数、类型）的声明
var (
	name string // ""
	age  int    // 0
	isok bool   // false
)

func vardeem() {
	name = "理想"
	age = 16
	isok = true
	//go语言中变量声明必须使用，不使用就编译不过去
	fmt.Print(isok) //在终端中输出要打印的内容
	fmt.Printf("name:%s", name)
	fmt.Println(age) //打印完内容后会有换行符
}

package main

import "fmt"

type Person struct {
	name   string
	age    int8
	dreams []string
}

/*
func (p *Person) SetDreams(dreams []string) {
	p.dreams = dreams
}
*/

//如果用上一种方法，在修改了传递来的参数数组之后，结构体里的数据也会被修改

func (p *Person) SetDreams(dreams []string) {
	p.dreams = make([]string, len(dreams))
	copy(p.dreams, dreams)
}

func main() {
	p1 := Person{name: "小王子", age: 18}
	data := []string{"吃饭", "睡觉", "打豆豆"}
	p1.SetDreams(data)

	//因为slice和map这两种数据类型都包含了指向底层数据的指针，因此我们在需要复制它们时要特别注意

	// 你真的想要修改 p1.dreams 吗？
	data[1] = "不睡觉"
	fmt.Println(p1.dreams) // [吃饭 睡觉 打豆豆]

}

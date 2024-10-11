package main

import (
	"fmt"

	"golang.org/x/term"
)

var (
	SHeight int
	SWidth  int
	THeight int
	TWidth  int
)

func init() {
	var (
		tw  = &TWidth
		th  = &THeight
		err error
	)
	*tw, *th, err = term.GetSize(0)
	if err != nil {
		panic("couldn't get terminal size")
	}

}

func main() {
	fmt.Println(TWidth, THeight)
}

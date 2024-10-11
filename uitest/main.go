package main

import (
	"fmt"
	"os"

	"github.com/fstanis/screenresolution"
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
		tw = &TWidth
		th = &THeight

		sw = &SWidth
		sh = &SHeight

		err error
	)
	*tw, *th, err = term.GetSize(0)
	if err != nil {
		fmt.Println("failed to get terminal size")
		os.Exit(1)
	}

	res := screenresolution.GetPrimary()
	if res == nil {
		fmt.Println("failed to get screen resolution")
		os.Exit(1)
	}
	*sw = res.Width
	*sh = res.Height

}

func main() {
	fmt.Println(TWidth, THeight)
	fmt.Printf("Screen res is %v x %v", SWidth, SHeight)

}

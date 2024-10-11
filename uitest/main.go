package main

import (
	"fmt"
	"math"
	"os"

	"github.com/fstanis/screenresolution"
	"golang.org/x/term"
)

var (
	// screen resolution sizes in px
	SHeight int
	SWidth  int

	// terminal scren size in format that is used for terminal measurements
	THeight int
	TWidth  int

	// terminal cell size in px
	CHeight float64
	CWidth  float64
)

func init() {
	var (
		tw = &TWidth
		th = &THeight

		sw = &SWidth
		sh = &SHeight

		cw = &CWidth
		ch = &CHeight

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

	*cw = math.Round(float64(*sw / *tw))
	*ch = math.Round(float64(*sh / *th))

}

func main() {
	fmt.Println(TWidth, THeight)
	fmt.Printf("Screen res is %v x %v\n", SWidth, SHeight)
	fmt.Printf("Single cell size in px is %v, %v", CWidth, CHeight)

}

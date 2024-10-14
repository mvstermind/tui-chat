package main

import (
	"fmt"
	"math"
	"os"
	"time"

	"github.com/fstanis/screenresolution"
	"github.com/go-vgo/robotgo"
	"golang.org/x/term"
)

var (
	// screen resolution sizes in px
	SHeight int
	SWidth  int
	// terminal screen size in format that is used for terminal measurements
	THeight int
	TWidth  int
	// terminal cell size in px
	CHeight int
	CWidth  int
)

func init() {
	var (
		tw  = &TWidth
		th  = &THeight
		sw  = &SWidth
		sh  = &SHeight
		cw  = &CWidth
		ch  = &CHeight
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
	*cw = int(math.Round(float64(*sw / *tw)))
	*ch = int(math.Round(float64(*sh / *th)))
}

func main() {
	fmt.Println(TWidth, THeight)
	fmt.Printf("Screen res is %v x %v\n", SWidth, SHeight)
	fmt.Printf("Single cell size in px is %v, %v\n", CWidth, CHeight)

	// width cells map
	cellsSliceX := make([]int, TWidth+1)
	for i := range cellsSliceX {
		cellsSliceX[i] = CWidth * i
	}

	// height cells map
	cellsSliceY := make([]int, THeight+1)
	for i := range cellsSliceY {
		cellsSliceY[i] = CHeight * i
	}

	ticker := time.NewTicker(100 * time.Millisecond)
	defer ticker.Stop()

	for range ticker.C {
		mouseX, mouseY := robotgo.Location()
		cellX := findCell(mouseX, cellsSliceX)
		cellY := findCell(mouseY, cellsSliceY)
		fmt.Printf("\rCell: X: %d, Y: %d    ", cellX, cellY)
	}
}

func findCell(pos int, cellsSlice []int) int {
	for i := 0; i < len(cellsSlice)-1; i++ {
		if pos >= cellsSlice[i] && pos < cellsSlice[i+1] {
			return i
		}
	}
	return len(cellsSlice) - 2 // return the last valid cell if not found
}


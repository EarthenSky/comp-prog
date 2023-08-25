package main

import (
	"bufio"
    "fmt"
	"strconv"
	"os"
	"strings"
	"math"
)

func main() {
	// read input integer
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	val, _ := strconv.Atoi(strings.TrimSpace(line))
	
	// find all or n-1 prime factors
	var counter int = 0
	max := int(math.Ceil(math.Sqrt(float64(val))))
	for i := 2; (i <= max); i++ {
		for val % i == 0 {
			val = val / i
			counter++
		}
	}

	// include the last number, but only if non-zero
	if val != 1 {
		counter++
	}

	fmt.Println(counter)
}
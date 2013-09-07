package main

import (
	"github.com/aaasen/dingo"
)

func main() {
	server := dingo.New(config)
	server.Run()
}

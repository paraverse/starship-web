package main

import (
	"fmt"
	"net/http"
)

type IndexController struct{}

func (c IndexController) Respond(w http.ResponseWriter, r *http.Request, data map[string]string) {
	fmt.Fprintf(w, "hello, world")
}

package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

type IndexController struct{}

func (c IndexController) Respond(w http.ResponseWriter, r *http.Request, data map[string]string) {
	fmt.Fprintf(w, "hello, world")
}

type JSONController struct{}

func (c JSONController) Respond(w http.ResponseWriter, r *http.Request, data map[string]string) {
	json, err := loadJSON(data["filename"])

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	fmt.Fprintf(w, string(json))
}

func loadJSON(name string) ([]byte, error) {
	filename := "static/data/" + name + ".json"

	body, err := ioutil.ReadFile(filename)

	if err != nil {
		return nil, err
	}

	return body, nil
}

package main

import (
	"github.com/aaasen/dingo"
)

var config = dingo.Config{
	Port:        "1337",
	TemplateDir: "/",
	StaticDir:   "/static/",
	Routes:      routes,
}

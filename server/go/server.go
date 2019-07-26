package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadFile("index.html")

	if err != nil {
		fmt.Println(err)
	}
	_, _ = w.Write(data)
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("server is listening on 3000")
	_ = http.ListenAndServe(":3000", nil)
}

package main

import (
	"os/exec"
	"os"
	"github.com/buger/jsonparser"
)

func main() {
	out, err := exec.Command("rfkill","-o","SOFT,HARD","-n","-J").Output()
	if err != nil {
		os.Exit(1)
	}
	value, _ := jsonparser.GetString(out, "", "[0]", "soft")
	if value == "blocked" {
		os.Exit(0)
	} else {
		os.Exit(1)
	}
}

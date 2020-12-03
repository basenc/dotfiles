package main

import (
	"fmt"
	"os/exec"
	"os"
	"regexp"
	"strconv"
)

func progressBar(progress int, maximum int, divs int, icons []string, spacer string) string {
	bar := spacer
	num_of_filled := progress * divs / maximum
	if progress == maximum {
		for i := 0; i < divs; i++ {
			bar += icons[len(icons) - 1]
			bar += spacer
		}
	} else {
		for i := 0; i < num_of_filled; i++ {
			bar += icons[len(icons) - 1]
			bar += spacer
		}
		bar += icons[(progress - (maximum / divs) * num_of_filled) * len(icons) / (maximum/divs)]
		bar += spacer
		for i := 0; i < (divs - num_of_filled - 1); i++ {
			bar += icons[0]
			bar += spacer
		}
	}
	return bar
}

func main() {
	icons := []string{"○","◔","◐","◕","●"}
	mute_icon := ""
	default_icon := ""
	headphones_icon := ""
	headset_icon := ""
	dots := 5
	spacer := " "

	out, err := exec.Command("pacmd","list-sinks").Output()
	if err != nil {
		os.Exit(1)
	}

	pacmd := string(out)

	pacmd = regexp.MustCompile("[[:blank:]]").ReplaceAllString(pacmd,"")
	pacmd = regexp.MustCompile("(?Us)\\*index:.+activeport:.+\\n").FindString(pacmd)

	muted := regexp.MustCompile("muted:yes").FindString(pacmd)
	activeport := regexp.MustCompile("activeport:(<.+>)").FindStringSubmatch(pacmd)[1]
	volumeStr := regexp.MustCompile("(?U)volume:.+((\\d?\\d?\\d?)%)").FindStringSubmatch(pacmd)[2]
	volume, _ := strconv.Atoi(volumeStr)

	if muted != "" {
		fmt.Print(mute_icon)
		os.Exit(0)
	} else {
		fmt.Print(default_icon)
		fmt.Print(progressBar(volume,100,dots,icons,spacer))
		if activeport == "<analog-output-headphones>" {
			fmt.Print(headphones_icon)
		} else if activeport == "<headset-output>" {
			fmt.Print(headset_icon)
		} else if activeport != "<analog-output-speaker>" {
			fmt.Print("?")
		}
	}
}

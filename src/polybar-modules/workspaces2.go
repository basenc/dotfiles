package main

import (
	"fmt"
	"os/exec"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	icons := []string{"􀀺","􀀼","􀀾","􀁀","􀁂","􀁄","􀁆","􀁈","􀁊","􀓵"}
	active_icons := []string{"􀀻","􀀽","􀀿","􀁁","􀁃","􀁅","􀁇","􀁉","􀁋","􀔔"}
	spacer := " "
	bar := []string{}

	out, err := exec.Command("xprop","-root").Output()

	if err != nil {
		os.Exit(1)
	}

	xprop := string(out)

	if !regexp.MustCompile("_NET_ACTIVE_WINDOW.+(0x.+)").MatchString(xprop) {
		os.Exit(0)
	}

	desktopNamesStr := regexp.MustCompile("\\d+").FindAllString(regexp.MustCompile("_NET_DESKTOP_NAMES.+").FindString(xprop),-1)[1:]
	desktopNames := []int{}
	for i := range desktopNamesStr {
			desktop, _ := strconv.Atoi(desktopNamesStr[i])
			desktopNames = append(desktopNames, desktop)
	}

	currentDesktopStr := regexp.MustCompile("_NET_CURRENT_DESKTOP.+(\\d)").FindStringSubmatch(xprop)[1]
	currentDesktop, _ := strconv.Atoi(currentDesktopStr)

	for i := range desktopNames {
		bar = append(bar,icons[desktopNames[i] - 1])
	}

	bar[currentDesktop] = active_icons[desktopNames[currentDesktop] - 1]

	fmt.Print(strings.Join(bar,spacer))
}

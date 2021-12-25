package main

import (
	"os/exec"
	"C"
	"fmt"
)

//export ShowSwarmNodeInfo
func ShowSwarmNodeInfo(containerID *C.char) ([]byte, error) {
	cmd := exec.Command("docker", "node inspect"+ " " + containerID)
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("stdout:\n%s\n", err)
	}
	return out, err
}

//export ReturnDockerImagesNum
func ReturnDockerImagesNum() int {
    return 1+2;
}

func main(){}
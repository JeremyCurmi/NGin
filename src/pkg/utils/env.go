package utils

import (
	"flag"
	"github.com/alex-ant/envs"
)

func ParseEnvVariables() error {
	flag.Parse()
	return envs.GetAllFlags()
}

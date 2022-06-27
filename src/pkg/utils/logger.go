package utils

import (
	"github.com/JeremyCurmi/NGin/src/app/api/config"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	"os"
)

const (
	InfoLevel  = "info"
	DebugLevel = "debug"
)

func parseLogLevel(level string) zapcore.Level {
	switch level {
	case DebugLevel:
		return zapcore.DebugLevel
	case InfoLevel:
		return zapcore.InfoLevel
	default:
		return zapcore.InfoLevel
	}
}

func SetUpLogger() (logger *zap.Logger) {
	atom := zap.NewAtomicLevel()
	logger = zap.New(zapcore.NewCore(zapcore.NewJSONEncoder(zap.NewProductionEncoderConfig()), zapcore.Lock(os.Stdout), atom))
	defer func(logger *zap.Logger) {
		_ = logger.Sync()
	}(logger)

	atom.SetLevel(parseLogLevel(*config.LogLevel))
	return logger
}

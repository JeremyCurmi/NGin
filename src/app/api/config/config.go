package config

import "flag"

var (
	LogLevel          = flag.String("log-level", "info", "application log level")
	DBURL             = flag.String("database-url", "user=postgres password=password dbname=Database sslmode=disable", "db connection string")
	DBConnMaxLifetime = flag.Int("database-max-conn-lifetime", 60, "connection lifetime in minutes if greater than 0")
	APIPort           = flag.String("api-port", "3000", "api for application")
	ServiceName       = "NGin"
	DatabaseDriver    = "postgres"
	MigrationsPath    = "../../app/api/migrations"
)

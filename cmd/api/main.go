package main

import (
	"github.com/JeremyCurmi/NGin/src/app/api/config"
	"github.com/JeremyCurmi/NGin/src/app/api/services"
	"github.com/JeremyCurmi/NGin/src/app/handlers"
	"github.com/JeremyCurmi/NGin/src/pkg/database"
	"github.com/JeremyCurmi/NGin/src/pkg/utils"
	"github.com/gin-gonic/gin"
	"github.com/jmoiron/sqlx"
	"go.uber.org/zap"
)

func main() {
	var db *sqlx.DB
	logger := utils.SetUpLogger()

	err := utils.ParseEnvVariables()
	if err != nil {
		logger.Error("failed to initialize Environment variables")
	}

	dbClient, err := database.New(*config.DBURL, *config.DBConnMaxLifetime, logger)
	if err != nil {
		logger.With(zap.Error(err)).Error("database connection issue!")
	}
	db = dbClient.Conn()

	n, err := database.RunMigrations(db)
	if err != nil {
		logger.With(zap.Error(err)).Error("unable to run database migrations")
	}
	logger.Info("Applied migrations", zap.Int("migrations", n))

	err = initAPI(db, logger)
	if err != nil {
		logger.With(zap.Error(err)).Error("unable to set up api")
	}
}

func initAPI(db *sqlx.DB, logger *zap.Logger) error {
	router := gin.Default()

	// set up services
	userService := services.NewUserService(db, logger)

	// set up api manager
	api := handlers.NewManager(userService)
	err := api.InitRoutes(router)
	if err != nil {
		return err
	}

	err = router.Run(":" + *config.APIPort)
	if err != nil {
		return err
	}
	return nil
}

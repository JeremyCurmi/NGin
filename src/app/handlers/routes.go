package handlers

import (
	"github.com/JeremyCurmi/NGin/src/app/api/config"
	"github.com/JeremyCurmi/NGin/src/app/api/services"
	"github.com/gin-gonic/gin"
)

type Manager struct {
	ServiceName string
	UserService services.UserServices
}

func NewManager(userService services.UserServices) *Manager {
	return &Manager{
		ServiceName: config.ServiceName,
		UserService: userService,
	}
}

func (manager *Manager) InitRoutes(r *gin.Engine) error {
	manager.userRoutes(r.Group("/users"))
	return nil
}

func (manager *Manager) userRoutes(r *gin.RouterGroup) {
	r.GET("", manager.getUsers)
	r.GET("/:userID", manager.getUserByID)
	r.POST("", manager.createUserID)
}

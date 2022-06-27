package handlers

import (
	"github.com/JeremyCurmi/NGin/src/pkg/models"
	"github.com/JeremyCurmi/NGin/src/pkg/utils"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

func (manager *Manager) getUsers(c *gin.Context) {
	users, err := manager.UserService.GetUsers()
	if err != nil {
		utils.SendErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}
	utils.SendOKResponse(c, users)
}

func (manager *Manager) getUserByID(c *gin.Context) {
	userID, err := strconv.Atoi(c.Param("userID"))
	if err != nil {
		utils.SendErrorResponse(c, http.StatusBadRequest, err.Error())
	}

	user, err := manager.UserService.GetUserByID(userID)
	if err != nil {
		utils.SendErrorResponse(c, http.StatusInternalServerError, err.Error())
	}
	utils.SendOKResponse(c, user)
}

func (manager *Manager) createUserID(c *gin.Context) {
	var user *models.User
	err := c.Bind(&user)
	if err != nil {
		utils.SendErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	err = manager.UserService.CreateUser(user)
	if err != nil {
		utils.SendErrorResponse(c, http.StatusInternalServerError, err.Error())
		return
	}

	utils.SendOKResponse(c, user)
}

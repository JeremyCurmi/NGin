package utils

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func SendOKResponse(c *gin.Context, data interface{}) {
	c.JSON(http.StatusOK, data)
}

func SendErrorResponse(c *gin.Context, errCode int, errMessage string) {
	c.AbortWithStatusJSON(errCode, map[string]string{"error": errMessage})
}

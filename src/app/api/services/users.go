package services

import (
	"database/sql"
	"github.com/JeremyCurmi/NGin/src/pkg/models"
	"github.com/jmoiron/sqlx"
	"go.uber.org/zap"
)

type UserServices interface {
	GetUsers() ([]models.User, error)
	GetUserByID(id int) (*models.User, error)
	CreateUser(user *models.User) error
}

type UserService struct {
	Database *sqlx.DB
	Logger   *zap.Logger
}

func NewUserService(db *sqlx.DB, logger *zap.Logger) *UserService {
	return &UserService{
		db,
		logger,
	}
}

func (service *UserService) GetUsers() ([]models.User, error) {
	stmt := `SELECT * FROM users;`
	var users []models.User
	err := service.Database.Select(&users, stmt)
	if err != nil {
		service.Logger.Error("failed to get users from db", zap.String("method", "GetUsers"), zap.Error(err))
		return nil, err
	}
	return users, nil
}

func (service *UserService) GetUserByID(userID int) (*models.User, error) {
	var user models.User

	stmt := `SELECT * FROM users WHERE id = $1;`
	err := service.Database.Get(&user, stmt, userID)

	if err != nil {

		if err == sql.ErrNoRows {
			return nil, nil
		}

		service.Logger.Error("user not found", zap.String("method", "GetUserByID"), zap.Int("userID", userID), zap.Error(err))
		return nil, err
	}

	return &user, nil
}

func (service *UserService) CreateUser(user *models.User) error {
	stmt := `INSERT INTO users (username, email, password) VALUES (:username, :email, :password);`
	_, err := service.Database.NamedExec(stmt, user)

	if err != nil {
		service.Logger.Error("failed to create user",
			zap.String("method", "CreateUser"),
			zap.Any("user", user),
			zap.Error(err))
		return err
	}
	return nil
}

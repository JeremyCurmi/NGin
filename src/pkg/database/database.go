package database

import (
	"errors"
	"github.com/JeremyCurmi/NGin/src/app/api/config"
	"github.com/gobuffalo/packr"
	_ "github.com/jackc/pgx"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	migrate "github.com/rubenv/sql-migrate"
	"go.uber.org/zap"
	"time"
)

// Client conn attribute contains db connection
type Client struct {
	conn *sqlx.DB
}

func (c *Client) Close() {
	_ = c.conn.Close()
}

func (c *Client) Conn() *sqlx.DB {
	return c.conn
}

// New returns a new database client
func New(url string, maxConnTimeout int, logger *zap.Logger) (*Client, error) {
	var (
		err  error
		conn *sqlx.DB
	)

	logDBError := func(err error) {
		logger.With(zap.Error(err)).Warn("⚠️ failed to initialize database connection, retrying in 3 seconds ...")
		time.Sleep(3 * time.Second)
	}

	startTimer := time.Now()

	for {
		if time.Since(startTimer) > time.Second*30 {
			return nil, errors.New("❌ connection timeout occurred while trying to connect to database")
		}

		conn, err = sqlx.Connect(config.DatabaseDriver, url)
		if err != nil {
			logDBError(err)
			continue
		}

		err = conn.Ping()
		if err != nil {
			logDBError(err)
			continue
		}

		logger.Info("⚡️ Connected to database")
		break
	}

	if maxConnTimeout > 0 {
		conn.SetConnMaxLifetime(time.Duration(maxConnTimeout) * time.Minute)
	}

	return &Client{
		conn: conn,
	}, nil
}

func RunMigrations(dbClient *sqlx.DB) (int, error) {

	migrations := &migrate.PackrMigrationSource{
		Box: packr.NewBox(config.MigrationsPath),
	}

	migrate.SetTable("db-migrations")

	n, err := migrate.Exec(dbClient.DB, config.DatabaseDriver, migrations, migrate.Up)
	if err != nil {
		return 0, err
	}
	return n, nil
}

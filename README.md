[![CI/CD](https://github.com/JeremyCurmi/NGin/actions/workflows/main.yml/badge.svg)](https://github.com/JeremyCurmi/NGin/actions/workflows/main.yml)
# NGin
## Deploy Machine Learning at Scale
![project image](misc/pic.jpg)


## Project Setup

1. DB Setup

### DB Setup
1. run make setup-db
2. edit alembic/env.py file:
```python
from dotenv import load_dotenv
load_dotenv()
config = context.config
section = config.config_ini_section
config.set_section_option(section, "sqlalchemy.url", os.environ["DATABASE_URL"])
```
3. set `DATABASE_URL` in .env file
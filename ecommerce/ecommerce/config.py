# cred as env variables 
import os


APP_ENV = os.getenv("APP_ENV", "development")

DATABASE_USERNAME = os.getenv("APP_ENV", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_USERNAME", "muku123")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")
TEST_DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce_test")
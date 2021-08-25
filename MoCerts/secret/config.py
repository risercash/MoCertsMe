import os
from dotenv import load_dotenv

load_dotenv()


ADMINS=os.getenv("ADMINS")
EMAIL_HOST_PASSWORD=os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER=os.getenv("EMAIL_HOST_USER")
EMAIL_HOST=os.getenv("EMAIL_HOST")
EMAIL_PORT=os.getenv("EMAIL_PORT")
SECRET_KEY=os.getenv("SECRET_KEY")
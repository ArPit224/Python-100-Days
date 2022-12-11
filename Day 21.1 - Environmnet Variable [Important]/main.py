from dotenv import load_dotenv
import os

load_dotenv()

SECRET = os.getenv("TEST_API_KEY")

print(SECRET)

#ADD .env FILE TO .gitignore IF USING GITHUB
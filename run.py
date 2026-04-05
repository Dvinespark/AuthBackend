from dotenv import load_dotenv
import os

# load env files
load_dotenv()


print(os.getenv('DB_NAME'))
from dotenv import load_dotenv
import os

load_dotenv()  

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOSTNAME"),
    "database": os.getenv("MYSQL_DATABASE"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),  
    "user": os.getenv("MYSQL_USERNAME"),
    "password": os.getenv("MYSQL_PASSWORD")
}

MONGO_CONFIG = {
    "host": os.getenv("MONGO_HOSTNAME"),
    "port": int(os.getenv("MONGO_PORT", 27017)),
    "database": os.getenv("MONGO_DATABASE"),
    "username": os.getenv("MONGO_USERNAME"),
    "password": os.getenv("MONGO_PASSWORD")
}

MONGO_URI = f"mongodb://{MONGO_CONFIG['username']}:{MONGO_CONFIG['password']}@{MONGO_CONFIG['host']}:{MONGO_CONFIG['port']}/{MONGO_CONFIG['database']}"

# Azure ADLS Gen2 config
AZURE_CONFIG = {
    "storage_account": os.getenv("AZURE_STORAGE_ACCOUNT"),
    "application_id": os.getenv("AZURE_APPLICATION_ID"),
    "directory_id": os.getenv("AZURE_DIRECTORY_ID"),
    "client_secret": os.getenv("AZURE_CLIENT_SECRET")
} 
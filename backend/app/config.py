import os

# Default values are provided in case the environment variables are not set
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://gurukardruv:3zh972ROB6vBwqGV@cluster0.xxc1uwg.mongodb.net/collegehub?retryWrites=true&w=majority')
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Convert string to boolean

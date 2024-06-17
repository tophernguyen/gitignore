from dotenv import load_dotenv
import os

#always make sure to have .gitignore file before doing git init

#this loads my .env file
load_dotenv()


#this loads my .env variables
id = os.getenv('client_id')
password = os.getenv('client_secret')

print(id)
print(password)


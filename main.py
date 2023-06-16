import dropbox
from dotenv import load_dotenv
import os
from ringer import *
from dropbox.exceptions import AuthError
from dropbox.files import WriteMode
from datetime import date

load_dotenv()  # load the environment variables

# Constant variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
URL = 'https://www.theringer.com/nba'


def upload_file_to_dropbox(url):
    try:
        # Create an instance of the Dropbox class with access token, app key and app_secret
        dbx = dropbox.Dropbox(oauth2_access_token=ACCESS_TOKEN, app_key=APP_KEY, app_secret=APP_SECRET)

        # Get today's date
        current_date = (date.today()).strftime('%m-%d-%Y')

        # Get txt file containing links
        get_links(URL)

        # Set path for txt file containing today's news
        ringer_news = os.path.basename(f"drop-box/NBA News.txt")

        # Name of the file we will write into dropbox
        file_name = f"NBA-News-{current_date}.txt"

        # Open the file in binary mode and read its contents
        with open(ringer_news, "rb") as file:
            file_data = file.read()

        # Specify the remote file path where you want to upload the file
        remote_path = f"/The Ringer-NBA News/{file_name}"

        # Upload the file to Dropbox
        dbx.files_upload(file_data, remote_path, mode=WriteMode("overwrite"))

        print("File uploaded successfully to Dropbox!")

    # Satch potential errors and print to console
    except AuthError as e:
        print("An error occurred while authenticating with Dropbox.")
        print(e)

    except Exception as e:
        print("An error occurred while uploading the file to Dropbox.")
        print(e)


upload_file_to_dropbox(URL)

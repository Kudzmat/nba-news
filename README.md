# nba-news
Grabbing the latest news articles from The Ringer

![ringer news](https://github.com/Kudzmat/nba-news/assets/65554208/e26aad04-9e9d-4736-b32d-a9665d7b920d)

FUNCTION & PURPOSE:

NBA News is a python script which parses through The Ringer.com's NBA page, grabs every article and headline for that day, 
and uploads it to a folder in dropbox in a txt file. This app serves as a quick way to see what the latest news is in the NBA while
you're busy coding and craving some NBA news, but you just don't have the time to go through the entire website.

REQUIREMENTS:

You will need a Dropbox account and create an app on the Dropbox Developer website
Visit the Dropbox Developer website at https://www.dropbox.com/developers/apps and sign in with your Dropbox account.

Python3
beautifulsoup4==4.12.2
certifi==2023.5.7
charset-normalizer==3.1.0
dropbox==11.36.2
idna==3.4
ply==3.11
python-dotenv==1.0.0
requests==2.31.0
six==1.16.0
soupsieve==2.4.1
stone==3.3.1
urllib3==2.0.3

SETUP:

Install the dropbox library by running pip install dropbox in your terminal.

Generate an access token, app key, and app secret for your Dropbox app and use them as environmental variables. You can create an app and generate an access token by visiting the Dropbox Developer website.

FUNCTIONALITY:

upload_file_to_dropbox(url)

  This is the main function, it takes in the required url (https://www.theringer.com/nba). It reads a file which is stored locally, that contains all the articles and links and proceeds to write and upload this information to Dropbox using the Dropbox API.

get_links(url)
  This is a function which is called inside the upload_file_to_dropbox function. It takes in the url and uses BeautifulSoup to parse through the website and collect the relevant information.
  
  <img width="1351" alt="Screen Shot 2023-06-15 at 8 30 12 PM" src="https://github.com/Kudzmat/nba-news/assets/65554208/95db876d-def9-4778-b951-dea12b90d535">
  
  <img width="789" alt="Screen Shot 2023-06-15 at 8 54 56 PM" src="https://github.com/Kudzmat/nba-news/assets/65554208/1c8b637d-d6d6-4c61-b8c5-0938f147168d">


ERROR HANDLING:

Potential errors may occur such as the DropBox API not being successful in connecting or the file failing to write and upload into your DropBox folder. If this occurs, you may need to check your scope to ensure your app is allowed to write and upload to DropBox. Generating a new access token is also often a good fix.






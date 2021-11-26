# DREAM MAIL

## API

### Instalation

 1. Clone or download the repository
 2. Make sure [python3](https://www.python.org/downloads/release/python-3810/) is installed (API was tested in Python 3.8)
 3. Make sure [PIP](https://pip.pypa.io/en/stable/installation/) is installed for your python version
 4. Install [virtualenv](https://pypi.org/project/virtualenv/) using PIP
 5. Inside the downloaded repository, create a virtual enviroment
	 - `virtualenv env`
 6. Enter the virtual enviroment
	- For Windows:
		- `.\env\Scripts\activate.bat`
	- For Mac or Linux:
		- `source env/bin/activate`
 7. Install the required dependencies:
	- `pip install -r requirements.txt`
 8. Exit the virtual enviroment
	- `deactivate` 

### Run

 1. Make sure you completed the instalation
 2. Get inside the downloaded repository
 3. Enter the virtual enviroment
	- For Windows:
		- `.\env\Scripts\activate.bat`
	- For Mac or Linux:
		- `source env/bin/activate`
4. Run the app by executing the following command:
	- For Windows:
		- `python .\src\app.py`
	- For Mac or Linux:
		- `python ./src/app.py`
5. The host url of the server will be http://127.0.0.1:5000
6. By default, you can access the API using any API Client like [Postman](https://www.postman.com/)
7. To stop the server simply type Ctrl+C in the terminal you are running it

### Endpoints

 - POST: /mail/send
	 - Description:
		 - Sends an email
	- Body:
		- "from" -> email address of the sender (REQUIRED)
		- "password" -> password of the user (REQUIRED)
		- "to" -> email address of the reciever (REQUIRED)
		- "message" -> content of the email (REQUIRED)
- POST: /mail/fetch
	- Description:
		- Gets all the emails from the SMTP server and saves them to local server
	- Body:
		- "from" -> email address to fetch emails from  (REQUIRED)
		- "password" -> password of the user (REQUIRED)
		- "date" -> date since the emails will be fetched {must be in format 01-Jan-2021] (REQUIRED)
- GET: /mail
	- Description:
		- Gets all the saved emails from the local server
	- Parameters:
		- "from" -> email address to fetch emails from  (REQUIRED)
- POST /news:
	- Description:
		- Fetches news from internet and saves them to local server
	- Body:
		- "lang" -> language of the news (NO REQUIRED | `"es"` BY DEFAULT)
		- "date" -> date since the news will be retrieved {must be in format 2021-01-01] (NOT REQUIRED | CURRENT DATE BY DEFAULT )
- GET /news:
	- Description:
		- Gets all news saved in local server
	-	No Parameters
- POST /news/sources:
	- Description:
		- Sets all news sources to look for news
	- Body:
		- "sources" -> list of all news domains (REQUIRED)
- GET /news/sources
	- Description:
		- Gets the current news sources
	- No Parameters


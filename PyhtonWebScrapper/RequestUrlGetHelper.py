from requests import get
from contextlib import closing

# So currently, this uses the package request to use a HttpVerb to access the html
# The closing context lib is used to close the connection once a response is recived, and we alise the output to response
# We then use a custom function to check if a success. Might add a logger that connects to a [txt and db] to keep a track
def getUrlContent(url):
	try:
		with closing(get(url, stream=True)) as response:
			if successResponse(response):
				return response.content
			else:
				return None
	except:
		print("error")

def successResponse(response):
	contentType = response.headers["Content-Type"].lower()
	return(response.status_code == 200
		and contentType is not None
		and contentType.find("html") > -1)
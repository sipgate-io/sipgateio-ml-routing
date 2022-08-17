import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.environ.get("DATABASE_HOST") or 'localhost'
username = os.environ.get("DATABASE_USERNAME") or 'admin'


def getCallHistory(items=10):
	base_url = 'https://api.sipgate.com/v2'

	token_id = os.environ.get("SIPGATE_TOKEN_ID")
	token = os.environ.get("SIPGATE_TOKEN")
	
	headers = {
		'Content-Type': 'application/json'
	}
	
	request_body = {
		"types": "CALL",
		"limit": items,
		"direction": "INCOMING"
	}
	
	response = requests.get(
		base_url + '/history',
		params=request_body,
		auth=requests.auth.HTTPBasicAuth(token_id, token),
		headers=headers
	)

	data = json.loads(response.content.decode("utf-8"))

	return data['items']
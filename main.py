import requests

import urllib.parse

string = "Write your question here."

question = urllib.parse.quote(string)
cookie = "your_cookie"
# first open bing chatgpt chat page
# get cookie from -> dev tools -> applications -> cookies -> https:/www.bing.com -> _U

url = "https://chatgpt-4-bing-ai-chat-api.p.rapidapi.com/chatgpt-4-bing-ai-chat-api/0.2/send-message/"
payload = f"bing_u_cookie={cookie}&question={question}"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "cd4a63d8a5msh9b83baaa95f2e46p1c4739jsn4d6673a161ff",
	"X-RapidAPI-Host": "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

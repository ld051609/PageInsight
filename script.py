import requests
from dotenv import load_dotenv
import os
import json
from bs4 import BeautifulSoup 
import cohere


load_dotenv()
token = os.environ.get("TOKEN")
website_url = "https://www2.gnb.ca/content/gnb/en/gateways/about_nb/geography.html"
# print(token)
url = f'https://api.diffbot.com/v3/article?token={token}&url={website_url}'
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
# if(response.status_code != 200 or response.status_code != 201):
#     print("Reponse is not ok")
json_response = response.text

# Parse JSON
data = json.loads(json_response)

# Extract html of the webpage 
html_content = data["objects"][0]["html"]
# print(html_content)

soup = BeautifulSoup(html_content, "html.parser") 
tag_name = soup.find_all('p')
message = ""
for tag in tag_name:
    message += tag.get_text()
    # print(tag.get_text())
# print(message)


api_key = os.getenv("CO_API_KEY")
co = cohere.Client(api_key)

# Keep track of historical responses
chat_history = []
max_turns = 10
def chatboxAPI(message):
    # get user input
    # message = input("Send the model a message: ")


    #generate chat response
    response = co.chat(
        message=message, 
        model="command", 
        temperature=0.3,
        chat_history=chat_history
    )


    # add message and answer to chat history
    user_message = {"role": "USER", "text": message}
    bot_message = {"role": "CHATBOT", "text": response.text}
    chat_history.append(user_message)
    chat_history.append(bot_message)

    # TODO: change the # of max_turns
    print(response.text)
    return response.text

chatboxAPI(f'Summarize {message}')
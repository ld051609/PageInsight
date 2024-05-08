from flask import Flask, request, jsonify
from extract_text import get_message, chatboxAPI, get_url
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/home', methods=['POST', 'GET'])  # Update to handle POST requests
def get_data():
    # Extract URL from POST request data
    url_fetch = ""
    if request.method == 'POST':
        request_data = request.get_json()
        url_fetch = request_data.get('url')
    print(f'URL fetched before {url_fetch}')
    url_fetch = "https://www2.gnb.ca/content/gnb/en/gateways/about_nb/geography.html"

    url = get_url(url_fetch) 
    message_res = get_message(url)
    answer = chatboxAPI(f'Summarize {message_res}')
    print(answer)
    # Create a dictionary to hold text data
    data = {
        "message": answer
    }

    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)

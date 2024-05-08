# SummarEyes
## Description

This Chrome extension allows users to enter a URL and receive a summary of the text content of the webpage associated with that URL. The summary is generated using the Diffbot API for content extraction and the Cohere API for text summarization.

## Prerequisites

Before using this Chrome extension, you'll need to perform the following steps:

1. **Register for Diffbot API Key**
   - Sign up for a Diffbot account at [Diffbot Developer Portal](https://www.diffbot.com/plans).
   - Obtain your API key from the portal. This key will be used to authenticate requests to the Diffbot API.

2. **Register for Cohere API Key**
   - Sign up for a Cohere account at [Cohere Developer Portal](https://cohere.ai/signup).
   - Obtain your API key from the portal. This key will be used to authenticate requests to the Cohere API.

## Installation

1. **Clone the project**

2. **Run the Python Script**
   - Navigate to the directory containing the `app.py` file.
   - Run the Python script using the command `python app.py`.

3. **Install the Extension**
   - Open Google Chrome and navigate to `chrome://extensions/`.
   - Enable the "Developer mode" toggle in the top right corner.
   - Click on "Load unpacked" and select the "chrome_extension" folder.

## Usage

1. **Enter URL**
   - Click on the extension icon in the Chrome toolbar.
   - Enter the URL of the webpage you want to summarize into the input field.
   - Click the "Summarize" button.

2. **View Summary**
   - After a brief moment, the summary of the webpage content will be displayed in the extension popup.

## Troubleshooting

If you encounter any issues while using the extension, please ensure that:
- The Flask server (`app.py`) is running and accessible.
- You have obtained valid API keys for Diffbot and Cohere.
- The API keys are correctly configured in the Chrome extension code (`background.js`).

If you continue to experience problems, feel free to [open an issue](https://github.com/your-repo/issues) on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

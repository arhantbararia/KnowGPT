# KnowGPT

Version 1.0

## About

The purpose of this web application is to provide a chatbot-like interface that can generate responses to user inputs using the OpenAI GPT-3 API. The application consists of a Flask web server that listens for user inputs and makes API calls to the OpenAI GPT-3 API to generate responses, which are then displayed to the user in a simple web interface.

## Installation

To set up and run the web application, follow these steps:

1. Clone the application code from the Github repository: [https://github.com/arhantbararia/Know_Wallet_Assignment-ARH](https://github.com/arhantbararia/Know_Wallet_Assignment-ARH)

    ```python
    git clone https://github.com/arhantbararia/Know_Wallet_Assignment-ARH.git
    ```
2. Recommend installing and running a virtual environment before installing the requirements. Check out [Running Virtual Environments](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Set up your OpenAI API credentials by creating a new API key in the [OpenAI dashboard](https://platform.openai.com/account/api-keys) and saving it to a file called `secret_key.txt` in the project root directory.
4. Start the Flask web server by running the following command in the project root directory.

    ```python
    python app.py
    ```

5. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000/) to access the web application.

## Test
Test cases are discussed in pdf under the test_cases directory.

## Examples

Here's an example of an API call to the Flask endpoint that generates chatbot responses using the OpenAI GPT-3 API:

```bash
POST http://localhost:5000/chat
Content-Type: application/json

{
  "message": "What is the weather like today?"
}

```

And here's an example of the JSON response from the server:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "response": "The weather is currently sunny and warm, with a high of 75 degrees."
}

```

In this example, the user has entered a question about the weather, and the Flask server has made an API call to the OpenAI GPT-3 API to generate a response. The generated response is then returned to the client in JSON format, with a key called "response" containing the text of the generated response.

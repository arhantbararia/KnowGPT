from flask import Flask, jsonify, render_template, request
import openai
import datetime





today = datetime.date.today()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/chat' , methods=['POST'])
def chat():
    message = request.form.get('message-input' , '')
    print(message)
    # response = "this should be it!"
    try:
        prompt = f"Q: {message} \nA:"

        response = openai.Completion.create(
            engine = "davinci",
            prompt = prompt,
            max_tokens = 1024,
            n =1,
            stop = None,
            temperature = 0.5
        )
        response = "response.choices[0].text.strip()"
        print(response)
    except Exception as e:
        print(e)
        response = "Error occurred! "
        with open("log.txt", "a") as log_file:
            log_file.write(f"{str(today)} - {current_time}: ERROR! : {e}\n") 


    return jsonify({'response': response})



if(__name__ == "__main__"):
    
    with open('secret_key.txt', 'r') as f:
        api_key = f.read().strip()
    
    
    if(api_key):
        openai.api_key = api_key
        app.run(debug= True)
    else:
        print("Enter OpenAI api key in secret_key.txt")
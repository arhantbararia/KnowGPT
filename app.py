from flask import Flask, jsonify, render_template, request
import openai


secret = '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'
openai.api_key = secret



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/chat' , methods=['POST'])
def chat():
    message = request.form.get('message-input' , '')
    print(message)
    response = "this should be it!"
    # try:
    #     prompt = f"Q: {message} \nA:"

    #     response = openai.Completion.create(
    #         engine = "davinci",
    #         prompt = prompt,
    #         max_tokens = 1024,
    #         n =1,
    #         stop = None,
    #         temperature = 0.5
    #     )
    #     answer = "response.choices[0].text.strip()"
    #     print(response)
    # except Exception as e:
    #     print(e)
    #     #return "Error: " + str(e)


    return jsonify({'response': response})



if(__name__ == "__main__"):
    app.run(debug= True)

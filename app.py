from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "order" in user_input and "status" in user_input:
        return "Please provide your order ID to check the status."
    elif "refund" in user_input:
        return "Refunds are processed within 5–7 business days."
    elif "delivery" in user_input:
        return "Delivery usually takes 3–5 working days."
    elif "support" in user_input or "contact" in user_input:
        return "You can reach support at support@example.com."
    else:
        return "I'm sorry, I didn’t understand that. Could you please rephrase?"

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json["message"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

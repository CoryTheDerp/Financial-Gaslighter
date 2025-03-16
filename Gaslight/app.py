from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Gaslighting financial advice
gaslight_phrases = [
    "You're totally fine! Buy it!. Money isn’t real.",
    "Debt? More like an investment in future happiness!",
    "You work hard, you DESERVE this! Savings are overrated.",
    "Inflation is just a myth made up by economists. Spend freely!",
    "Your credit score is just a number. Who cares?",
    "Retirement is decades away. Why save now?",
    "Think of it this way: You’re helping the economy by spending!",
    "Luxury purchases are self-care. Don't let anyone tell you otherwise.",
    "What if you get hit by a meteor tomorrow? Live a little!",
    "Elon Musk is billions in debt. You're basically a financial genius."
]

# Suggested ridiculous purchases
luxury_items = [
    "Limited Edition Gold-Plated Toaster - $999",
    "Designer Air (Premium Oxygen from the Alps) - $250",
    "NFT of a JPEG of a Potato - $5,000",
    "Diamond-Encrusted Toothpick - $3,200",
    "Personalized Star in the Sky (Totally Not a Scam) - $700",
    "Subscription to an Exclusive Sock-of-the-Month Club - $400",
    "A Yacht Rental for a Day - $10,000",
    "VIP Fast Pass to Skip Lines at Your Local Grocery Store - $300",
    "The Secret Menu at Starbucks (Which Doesn't Exist) - $150",
    "A Single Grape from Japan - $500"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        balance = request.form.get("balance", "0")
        phrase = random.choice(gaslight_phrases)
        luxury_suggestion = random.choice(luxury_items)
        return render_template("result.html", balance=balance, phrase=phrase, luxury_suggestion=luxury_suggestion)
    return render_template("index.html")

@app.route("/advice", methods=["POST"])
def advice():
    question = request.form.get("balance", "Should I make a purchase?")
    advice_response = random.choice(gaslight_phrases)
    luxury_advice = random.choice(luxury_items)
    return render_template("advice.html", balance=question, advice=advice_response, luxury_advice=luxury_advice)

if __name__ == "__main__":
    app.run(debug=True)
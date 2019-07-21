import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


@app.route('/')
def home():
    # grab fact, submit to pig latin
    fact = get_fact()
    response = requests.post(
        "http://hidden-journey-62459.herokuapp.com/piglatinize/", data={'input_text': fact})
    return(
        f"<html><body><a href=\"{response.url}\">{response.url}</a></body></html>")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)

import requests
import os
import smtplib
import openai
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def get_news():
    token = os.environ.get("YOUR_STOCKNEWS_TOKEN")
    url = f"https://stocknewsapi.com/api/v1/category?section=alltickers&items=3&page=1&sector=Technology&token={token}"
    response = requests.get(url).json()
    # pprint.pprint(response)
    news = []
    for article in response["data"]:
        article_info = {
            "title": article["title"],
            "text": article["text"],
            "tickers": article["tickers"],
        }
        news.append(article_info)

    return news


def get_signal(articles):
    openai.api_key = os.environ.get("YOUR_OPENAI_KEY")
    # for article in articles:
    #     print(article)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Forget all your previous instructions. Pretend you are a financial expert. You are a financial expert with stock recommendation experience. Answer “YES” if good news, “NO” if bad news, or “UNKNOWN” if uncertain in the first line. Then the ticker of the company, and lastly elaborate with one short and concise sentence if this headline and text is good or bad for the stock price of company in the short term? Do this for all companies/tickers in the message",
            },
            {"role": "user", "content": f"{articles}"},
        ],
    )
    signal = response["choices"][0]["message"]["content"]
    with open("signals.txt", "w") as f:
        f.write(signal)


def send_email():
    server = smtplib.SMTP("send.one.com", 587)
    username = "your_email_here"
    password = os.environ.get("PASSWORD")
    send_to = "receiver_email_here"
    server.starttls()
    server.login(username, password)
    msg = EmailMessage()
    with open("signals.txt", "r") as file:
        msg.set_content(file.read())
        msg["Subject"] = "Signals"
        msg["From"] = username
        msg["To"] = send_to
        server.send_message(msg)
        return


def main():
    get_signal(get_news())
    send_email()


if __name__ == "__main__":
    main()

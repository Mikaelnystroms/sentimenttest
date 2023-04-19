# AI-Driven Stock Forecasting Trial

This Python script uses OpenAI's GPT-3.5-turbo to analyze financial news and predict their impact on stock prices. It fetches news articles from the Stock News API, evaluates their sentiment using GPT-3.5-turbo, and emails the results to a specified address. It's based on a research study published [Here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4412788)

## Features
- Fetch financial news articles from Stock News API, focusing on the Technology sector.
- Perform sentiment analysis using OpenAI API and GPT-3.5-turbo.
- Write the sentiment signals to a text file.
- Email the signals to a specified email address.
## Requirements
- Python 3.9
- Requests library
- OpenAI library
- Python-dotenv library
You can install the required libraries using pip:
```
pip install requests openai python-dotenv
```
## Setup
- Obtain an API key from the Stock News API and replace the placeholder token in the url variable with your actual API key.
- Obtain an API key from OpenAI and set the OPENAI_API_KEY environment variable with your actual API key.
- Configure your email account credentials by setting the PASSWORD environment variable with your email account password and updating the username variable to match your email address.
- Replace the placeholder receiver_email_here with the email address where you'd like to receive the sentiment signals.
## Running the Script
After completing the setup, simply run the script with:
```
python ai_stock_forecasting.py
```

The script will fetch news, analyze their sentiment, and send an email with the results to the specified email address.

## Note 
that while GPT-3.5-turbo has shown promising results in research, it doesn't guarantee perfect accuracy in stock market predictions. Use the results as a supplementary tool for your investment decision-making process and always conduct your research before making any investment decisions.

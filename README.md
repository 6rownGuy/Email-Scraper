# Email Scraper

A small python code to to scrape emails from an existing email address on the basis of their subject containing keywords "Thank you for applying" and categorize them into a "job" category. 

## What does it do?

- It takes user's email id, password and application date as its input.
- It then pulls all the emails received after the specified date, checks for the ones with **Thank you for applying** in their subject and flags them.
- It then displays all those mails in a `DataFrame`, categorizing each of them as **'Job'** or **'Other'**.

## Requirements

Just run the provided requirements.txt in your terminal by typing
`pip install -r requirements.txt`
and you are good to go.

## Note

- This program only works with **Gmail** at the moment.
- For the code to work, you have must [allow less secure apps](https://myaccount.google.com/lesssecureapps?pli=1) to access your gmail account.
- Also mke sure that you have turned your IMAP settings on by going to
[Gmail](https://gmail.com) -> Settings -> Forwarding and POP/IMAP  -> Enable IMAP

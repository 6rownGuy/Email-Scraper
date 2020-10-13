import imaplib
import email
from email.header import decode_header
import os
import datetime
from dateutil import parser
import pandas as pd


def get_email_data(username, password, a_date, verbose):

    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)

    status, messages = imap.select("INBOX")

    before_date_flag = 0

    # total number of emails
    messages = int(messages[0])

    subject_list = []
    category_list = []
    date_list = []
    sender_list = []

    for i in range(messages, 0, -1):

        if before_date_flag == 1:
            break
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):

                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])

                date = parser.parse(msg["Date"]).date()
                subject = decode_header(msg["Subject"])[0][0]

                if date < a_date:
                    before_date_flag = 1
                    break

                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()

                date = msg["Date"][0:25]
                from_ = msg.get("From")

                sender_list.append(from_)
                subject_list.append(subject)
                date_list.append(date)
                if "Thank you for applying".lower() in subject.lower():
                    category_list.append(1)
                else:
                    category_list.append(0)

                if verbose:
                    print("Subject:", subject)
                    print("Date:", date)
                    print("=" * 100)

    # close the connection and logout
    imap.close()
    imap.logout()

    return {
        "Sender": sender_list,
        "Subject": subject_list,
        "Date": date_list,
        "Category": category_list,
    }


def num_to_str(x):
    if x == 1:
        return "Job"
    else:
        return "Other"


if __name__ == "__main__":
    mail_id = input("Enter mail id: ")
    mail_pswd = input("Enter mail password: ")
    app_date = input("Enter date of application (for the job): ")

    app_date = parser.parse(app_date).date()

    email_data = get_email_data(mail_id, mail_pswd, app_date, True)

    mail_df = pd.DataFrame.from_dict(email_data)

    print("Mail data: \n")
    mail_df["Category"] = mail_df["Category"].apply(num_to_str)

    print(mail_df)
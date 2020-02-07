import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host_office365 = 'smtp.office365.com'
port_office365 = 587
sender_email_id, sender_email_id_password = 'axy@ma.com', ''
# multiple people 'agoph@qnt.com, aaaiah@qnt.com'
receiver_email_id = 'bnz@qut.com'


def send_mail(**kwargs):
    # creates SMTP session
    s = smtplib.SMTP(host=host_office365, port=port_office365)
    # Identify yourself to an ESMTP server using EHLO
    s.ehlo()
    # start TLS Transport Layer Security for security
    s.starttls()
    s.login(sender_email_id, sender_email_id_password)

    msg = MIMEMultipart()
    message = kwargs['message']
    msg['From'] = kwargs['from']
    msg['To'] = kwargs['to']
    msg['CC'] = ''
    msg['Subject'] = kwargs['subject']

    # add in the message body
    msg.attach(MIMEText(message, 'html'))
    # send the message via the server set up earlier.
    s.sendmail(sender_email_id, receiver_email_id, str(msg))
    print('Mail Successfully sent to ', receiver_email_id)

    # Terminate the SMTP session and close the connection
    s.close()


if __name__ == '__main__':
    data = {'from': sender_email_id,
            'to': receiver_email_id,
            'subject': 'Alert',
            'message': 'This is a test msg'
            }
    send_mail(**data)


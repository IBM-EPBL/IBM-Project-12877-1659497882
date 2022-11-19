import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Interview Call"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    print("Proceeding...")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("19cs034@syedengg.co.in", "#Good2002$")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("19cs034@syedengg.co.in", email, message)
    s.quit()
def sendgridmail(user,TEXT):
    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("19cs034@syedengg.co.in")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.batch.post()
    
    #response = sg.client.mail.send.post(request_body=mail_json)

    print(response.status_code)
    #print(response.headers)
    


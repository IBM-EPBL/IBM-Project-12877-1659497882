import sendgrid
import os
from sendergrid.helpers.mail import *
sg=sendgrid.SendGridAPIClient(api_key='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')
from_email=Email("19cs054@syedengg.co.in")
to_email=To("19cs009@syedengg.co.in")
subject="Sending with SendGrid"
content=Content("text/plain","Skill/Job Recommender")
mail=Mail(from_email, to_email, subject, content)
response=sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

from flask import Flask, request, jsonify

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)   # needed for initialization


@app.route('/api/email')
# Setup port number and server name
def send_emails():

  # gets all the json that was passed in the body of the request
  # data_email = request.get_json()

  smtp_port = 587       # standard secure SMTP port
  smtp_server = 'smtp.gmail.com'    #google smtp server


  email_from = 'nicksmusicstore55@gmail.com'
  email_to = 'nicksmusicstore55@gmail.com'

  pswd = 'ynbpnuwxbrpjchaw'

  subject = "Nick's music store order confirmation and delivery!"



    
  # make the body of the email
  body = "Thank you for purchasing a midi file. Here is your order!"


  # make a MIME object to define parts of the email

  msg = MIMEMultipart()
  msg['From'] = email_from
  msg['To'] = email_to
  msg['Subject'] = subject

  # Attach the body of the message
  msg.attach(MIMEText(body, 'plain'))

  # Define the file to attach
  filename = 'Project_1_copy.flp'

  # Open the file in python as a binary
  attachment = open(filename, 'rb')

  # Encode as base 64
  attachment_package = MIMEBase('application', 'octet-stream')
  attachment_package.set_payload((attachment).read())
  encoders.encode_base64(attachment_package)
  attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
  msg.attach(attachment_package)


  # Cast as string
  text = msg.as_string()

  try:
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Connected to server :)")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, text)
    print(f"Email successfully sent to - {email_to}")

  except Exception as e:
    print(e)


  finally:
    TIE_server.quit()
    data = {'message': 'Email sent!'}
    return jsonify(data)





if __name__ == "__main__":    # needed for initialization
  app.run(debug=True)

  
# import smtplib
# sender_email = "mdm17b020@iiitdm.ac.in"
# recever_email = "omnish22@gmail.com"
# sender_password = input("enter your password")
# message = "this email is send useing python"

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(sender_email,sender_password)
# print("login Success")
# server.sendmail(sender_email,recever_email,message)
# print("Email has been sent to ",recever_email)

import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox7b9234b5e962442baa465c21629eb7a2.mailgun.org/messages",
		auth=("api", "3f3ecc1b20d55cae4f548f03684f6c05-64574a68-45febc5b"),
		data={"from": "Pricing Services <mdm17b020@iiitdm.ac.in>",
			"to": ["omnish22@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})


print(send_simple_message())
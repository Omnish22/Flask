from email import message
from requests import Response, post 
from typing import List 
import os 


class MailgunException(Exception):
	def __init__(self,message:str):
		self.message= message



class Mailgun:
	MAILGUN_API_KEY= os.environ.get("MAILGUN_API_KEY",None)
	MAILGUN_DOMAIN= os.environ.get("MAILGUN_DOMAIN",None)
	FROM_TITLE= "Pricing Service"
	FROM_EMAIL="mdm17b020@iiitdm.ac.in"


	@classmethod 
	def send_mail(cls,email:List[str],subject:str,text:str,html:str)->Response:
		if cls.MAILGUN_API_KEY is None:
			raise MailgunException("API key is missing")
		if cls.MAILGUN_DOMAIN is None:
			raise MailgunException("Domain is missing")

		response = post(f"{cls.MAILGUN_DOMAIN}/messages",
						auth=("api", cls.MAILGUN_API_KEY),
						data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
							"to": email,
							"subject": subject,
							"text":text})
		if response.status_code!=200:
			print(response.json())
			raise MailgunException("Error occured when sending e-mail")
		return response


Mailgun.send_mail(["omnish22@gmail.com"],"Price Alert","Your Item reached it's price","<h1>Perchase your Item</h1>")

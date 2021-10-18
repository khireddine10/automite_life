# Importing libraries
import time,os
import hashlib
import subprocess
import requests
import smtplib, ssl

def sendmessage():
    subprocess.run(["notify-send", "-u", "critical", "-i", "'notification-message-IM'", 'TCF CONSTANTINE !!'
					,'TCF CONSTANTINE YOU MUST CHECK NOW !!! https://portail.if-algerie.com/exams'], capture_output=False)
    return

def send_email():
    port = 465
    email_password = os.getenv("EMAIL_PASSWORD")
    email = os.getenv("EMAIL")
    smtp_server = "smtp.gmail.com"
    message = "TCF CONSTANTINE YOU MUST CHECK NOW !!! https://portail.if-algerie.com/exams"
    secure = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=secure)
        server.login(email, email_password)
        server.sendmail(email, email, message)

    except Exception as e:
		print(e)

def webrequest():
    my_web_site_session = os.getenv("SESSION")
    cookies = {'ifa_session': my_web_site_session}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get('https://127.0.0.1:8000', cookies=cookies, headers=headers)
    webpage = response.content
    return webpage

currentHash = hashlib.sha224(webrequest()).hexdigest()
print("running")
time.sleep(10)
while True:
	try:
		response = webrequest()
		currentHash = hashlib.sha224(response).hexdigest()
		time.sleep(3)
		response = webrequest()
		newHash = hashlib.sha224(response).hexdigest()

		if newHash == currentHash:
			continue

		else:	
			while  True:
				time.sleep(3)
				print("something changed")
				sendmessage()
				send_email()

			response = webrequest()
			currentHash = hashlib.sha224(response).hexdigest()
			time.sleep(3)
			continue
			
	except Exception as e:
		print("error")

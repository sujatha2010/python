import smtplib    
sender_mail = 'nuthalapatisujatha16@gmail.com'    
receivers_mail = ['nuthalapatisujatha16@gmail.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
Hi How are You.  
"""%(sender_mail,receivers_mail)    
try:    
   password = input('Enter the password');    
   smtpObj = smtplib.SMTP('gmail.com',587)    
   smtpObj.login(sender_mail,password)
   print("successfully login")    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")
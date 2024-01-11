import smtplib    
sender_mail = "nuthalapatisujatha16@gmail.com" 
num_receivers = int(input("Enter number of receivers\n"))
receivers = []
for _ in range(num_receivers):
   receivers.append(input("Enter receiver mail\n"))
   
message = input("Enter Message you want to send\n")  
try:    
   password = input("Enter the password\n");    
   smtpObj = smtplib.SMTP("gmail.com",587)    
   smtpObj.login(sender_mail,password)
   print("successfully login")    
   smtpObj.sendmail(sender_mail, receivers, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")
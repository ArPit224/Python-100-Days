import smtplib

email = "noirarry@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    
    connection.starttls()
    connection.login(user = email, password = "kvinglsvnfmcpzcp")
    connection.sendmail(from_addr = email, to_addrs = "ar10936325@gmail.com", msg = "Subject: Test Message\n\nTest Message, i have activated 2 factor and this email is a throwaway")

#Challange


import smtplib

email = "noirarry@gmail.com"
passw  = ""

#+++++++++++++ Emailer +++++++++++++#

def senmail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        
        connection.starttls()
        connection.login(user = email, password = passw)
        connection.sendmail(from_addr = email, to_addrs = "ar1096325@gmail.com", msg = "Subject: ISS SPOTTED\n\nLOOK UP!!!")

#+++++++++++++ Emailer +++++++++++++#
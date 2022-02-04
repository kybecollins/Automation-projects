import smtplib
def sendEmail():
    sender_email= ""    # your password or organization email
    receiver_email = ""  
    password = ''  # your password or organization email password

    message = "Hey, your rent is due "  #Message to be sent
    server =smtplib.SMTP('smtp.gmail.com',587)  #smtp server and port number
    
    server.starttls()
    try:
        server.login(sender_email,password)
        print("Login was Successful")
        server.sendmail(sender_email,receiver_email,message)
        print ("email has been sent to" , receiver_email)

    except:print("Could not login or send Mail. Verify credentials and try again")
        
sendEmail()

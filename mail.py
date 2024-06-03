# muav vaky nxrs yned
import smtplib
try:
    server = smtplib.SMTP(host = 'smtp.gmail.com',port =587)
    server.starttls()
    recever_email= input("enter you email")
    sender_email = 'jaikrishan2001@gmail.com'
    password = 'muav vaky nxrs yned'
    server.login(sender_email,password=password)
    subject = input("what is your problem")
    body = input("Toda deatails me btaoo")
    message = f"subject: {subject}\n\n{body}"
    server.sendmail(sender_email,recever_email,message)
    print("mene mail send kr di hai ")
    server.quit()
except Exception as e:
    print("mail send nhi huiii")
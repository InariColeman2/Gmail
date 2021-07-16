import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn
conn.ehlo()
conn.starttls()
#Gmail account login information
conn.login('xxx@gmail.com','SugarFox56')
#Gmail sender account and reciever name , Message to be sent
conn.sendmail('xxx@gmail.com','xyxy@gmail.com', 'Subject: Hi Jerry  \n\n Dear \n\n Jerry  hello Welcome to Miami ')
conn.quit()









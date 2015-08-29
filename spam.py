import smtplib

fromaddr = 'YOUREMAILHERE'
print "What number do you want to spam?"
number = raw_input()
if len(number) == 10 and number.isdigit():
   print "What is their cell phone provider?"
   provider = raw_input()
   dct = {"sprint" : '@messaging.sprintpcs.com', "t-mobile" : "@tmomail.net", "tmobile" : "@tmomail.net", "t mobile" : "@tmomail.net", "at&t" : "@txt.att.net", "att" : "@txt.att.net", "us cellular" : "@email.uscc.net", "u.s cellular" : "@email.uscc.net", "uscellular" : "@email.uscc.net", "verizon" : "@vtext.com", "verizon wireless" : "vtext.com", "virgin" : "@vmobl.com", "virgin mobile" : "@vmobl.com"}
   
else:
   print "That is not a valid phone number, please try again!"
   execfile("spam.py")
   
toaddrs = number + dct[provider.lower()]

print "What message would you like to send?" 
msg = raw_input()
username = 'YOUR EMAIL USERNAME HERE'
password = 'YOUR PASSWORD HERE'

n = 10
while True: 
    n = n - 1
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    
    #I only got it working with gmail, editing it to work with other email providers shouldn't be too difficult though.

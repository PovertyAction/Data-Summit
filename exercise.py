### Data Summit Exercise

# The purpose of this script is to give you a brief taste of the 
# awesome power of Python! The code below uses the smtplib package to
# send an automated email introducing yourself to the Data Summit Team. 

# You may have noticed that the '#' character is used to mark a line as
# a comment in Python (in the same way that the '*' character functions 
# in Stata). Although the script iteslf only requires a few lines of
# Python code to execute, we've included extensive comments below to 
# help you understand what each line is doing.


# This line loads the SMTP function/class from the smtplib package;
# in Python, little is built in, you'll almost always start your
# scripts with import statements.  
from smtplib import SMTP

# This line defines an SMTP server instance
server = SMTP('smtp.gmail.com', 587)

# This line starts the connection to the SMTP server
server.starttls()

# This line logs in to the server using the email address and password 
# specified. We had to customize the account's setting to allow this.
server.login("data_summit@poverty-action.org", "the_password")

# These lines define two variables, subject and text, containing the 
# email content we plan to send to the server.
subject = "Your name" + "'s introduction!" 
text = "My message all about myself." # REPLACE WITH OWN

# This combines our subject and text into the format required.
message = 'Subject: {}\n\n{}'.format(subject, text)

# This is where the magic happens, this line sends your email!
server.sendmail("", "data_summit@poverty-action.org", message)


### GOING EVEN FURTHER
 
# If you've mastered the basics of python on DataCamp and successfully
# run the code above we encourage you to modify it to do something even 
# cooler. If you don't know where to start, try to make the following
# message: "There are __ people attending the Data Summit. Here's the
# alphabetized list: " (with the list). We've gotten you started:

# You'll need to uncomment these two lines
# import pandas as pd
# attendee_list = list(pd.read_csv("summit_attendees.csv")['unordered_names'])

### Add Your Code Here ###

# And uncomment these 5 lines
# subject = "Your name" + "'s Python customization." 
# text = "My description of my customization: " # REPLACE WITH OWN
# text = text + str(attendee_list)
# message = 'Subject: {}\n\n{}'.format(subject, text)
# server.sendmail("", "data_summit@poverty-action.org", message)


# This line closes the connection to the SMTP server
server.quit()
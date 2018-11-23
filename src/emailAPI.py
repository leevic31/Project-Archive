import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# used https://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email as reference to create sendEmail function
def sendEmail(self, to_address, password):
    """(sendEmail, str) -> None
    Send email with login information to agency employee

    Arguments:
        to_address {str} -- email address to send login information to
        password {str} -- agency employee password
    """

    from_address = "c01group12@gmail.com"
    # to_addr is the agency employee's email
    to_address = to_address
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "TEQ Login Information"
    # username is the agency employees email
    # password is the agency employees name
    body = "Welcome to the TEQ database application. Below is your username and password.\nUsername: "+ to_address + "\nPassword: "+ password
    msg.attach(MIMEText(body, 'plain'))
    # establish server so that emails from a google email address can be sent
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, "group1100")
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

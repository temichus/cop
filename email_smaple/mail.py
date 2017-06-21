# -*- coding: utf-8 -*-
import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText
import csv
import codecs
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
import sys
import time

LOGGER = 'logger'

user = "robot.artsiom.mishuta"
password = "robot1234"

# Logger initialization
logger = logging.getLogger(LOGGER)
logger.setLevel(logging.DEBUG)

# Dump handler initialization
console = StreamHandler(sys.stdout)
console.setLevel(logging.DEBUG)
logger.addHandler(console)

# File handler initialization if need
logfile = RotatingFileHandler("log1.txt", backupCount=10, maxBytes=13107200)
logfile.setLevel(logging.DEBUG)
log_format = '%(asctime)s - %(levelname)s - %(message)s'
log_datefmt = '%d-%m-%Y %H:%M:%S'
file_formatter = logging.Formatter(log_format, log_datefmt)
logfile.setFormatter(file_formatter)
logger.addHandler(logfile)
logfile.doRollover()



server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(user, password)


body = None
subject = None
with codecs.open('body.txt', 'rb') as myfile:
    body=myfile.read()


with codecs.open('subject.txt', 'rb') as myfile:
    subject=myfile.read()



with codecs.open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        try:
            msg = MIMEText(body.format(name=row[1]))
            msg['Subject'] = subject
            msg['From'] = '{0}@gmail.com'.format(user)
            msg['To'] = row[0]
            server.sendmail("{0}@gmail.com".format(user), ['{0}@gmail.com'.format(user) ,row[0]], msg.as_string())
            logger.info("email: \n -------------------------------- \n {0} \n -------------------------------- \n send to {1}".format(msg.as_string(), msg['To']  ))
            time.sleep(5)
        except SMTPException as e:
            logger.error("email: \n -------------------------------- \n {0}\n -------------------------------- \n was not send to {1}".format(msg.as_string(), msg['To']  ))
            logger.error(e)
server.quit()


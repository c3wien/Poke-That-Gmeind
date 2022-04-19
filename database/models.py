# -*- coding: utf-8 -*-

from datetime import datetime
from json import load
from random import choice
from uuid import uuid4
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from flask import url_for
from sqlalchemy import UniqueConstraint, Column, Boolean, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from config import DEBUG, MAIL_FROM, MAIL_DEBUG
from config.mail import *
from . import Base

def sendmail(addr_from, addr_to, subject, msg, attachment=None, attachment_name=None):
    if not attachment:
        mail = MIMEText(msg)
    else:
        mail = MIMEMultipart()
        mail.attach(MIMEText(msg))
        app = MIMEApplication(attachment)
        app['Content-Disposition'] = 'attachment; filename="%s"' % attachment_name
        mail.attach(app)

    mail["Subject"] = subject
    mail["From"] = addr_from
    if type(addr_to) == str:
        mail["To"] = addr_to
    else:
        mail["To"] = ', '.join(addr_to)

    with SMTP("localhost") as s:
        s.send_message(mail)


class Mail(Base):
    __tablename__ = "mails"

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("senders.id"))
    recipient = Column(String(5), nullable=False)
    date_sent = Column(DateTime)

    __table_args__ = tuple(
            UniqueConstraint(sender_id, recipient)
            )

    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def send(self):
        self.date_sent = datetime.now()

        city = CitiesObjects.get_city_by_id(self.recipient)

        addr_from = '"' + MAIL_FROM + '" <' + MAIL_FROM + '>'
        if DEBUG:
            addr_to = '"' + MAIL_DEBUG + '" <' + MAIL_DEBUG + '>'
        else:
            addr_to = str(city) + " <" + city.contact.mail + ">"
        subject = "Luftfilterbegehren"
        msg = MAIL_DISCLAIMER.format(name_user=self.sender.name, mail_user=self.sender.email_address) + "\n" * 2
        msg = msg + MAIL_CITY.format(name_city=str(city), name_user=self.sender.name)
        sendmail(addr_from, addr_to, subject, msg)

class Sender(Base):
    __tablename__ = "senders"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    email_address = Column(String(254), unique=True, nullable=False)
    mails = relationship("Mail", order_by="Mail.id", backref="sender")
    hash = Column(String(64), unique=True, nullable=False)
    date_validated = Column(DateTime)
    date_requested = Column(DateTime, nullable=False)

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.request_validation()

    def validate(self):
        self.date_validated = datetime.now()

        addr_from = '"' + MAIL_FROM + '" <' + MAIL_FROM + '>'
        addr_to = self.name + " <" + self.email_address + ">"
        subject = "Vielen Dank für Ihre Teilnahme auf luftfilterbegehren.at"
        msg = MAIL_WELCOME.format(name_user=self.name)
        sendmail(addr_from, addr_to, subject, msg)

    def request_validation(self):
        self.hash = uuid4().hex
        self.date_requested = datetime.now()

        addr_from = '"' + MAIL_FROM + '" <' + MAIL_FROM + ">"
        addr_to = self.name + " <" + self.email_address + ">"
        subject = "Bestätigung für luftfilterbegehren.at"
        url = url_for("act.validate", hash=self.hash, _external=True)
        msg = MAIL_VALIDATE.format(name_user=self.name, url=url)
        sendmail(addr_from, addr_to, subject, msg)


class Cities():
    def __init__(self):
        self.cities = load_cities("cities.json")

    def get_city_by_id(self, id):
        cities = self.cities
        try:
            city = [city for city in cities if city.id == id][0]
        except IndexError:
            city = None
        return city

    def get_city_by_name(self, prettyname):
        cities = self.cities
        try:
            city = [city for city in cities if city.name.prettyname == prettyname][0]
        except IndexError:
            city = None
        return city

    def get_party(self, shortname):
        return self.parties[shortname]


class Contact():
    def __init__(self, mail, phone, facebook, twitter):
        self.mail = mail
        self.phone = phone
        self.facebook = facebook
        self.twitter = twitter


class Name():
    def __init__(self, name):
        self.name = name
        self.prettyname = name.replace(' ', '')


class City():
    def __init__(self, id, name, plz, contact):
        self.id = id
        self.name = name
        self.plz = plz
        self.contact = contact
        self.state = get_state_from_id(id)
        self.imagename = get_imagename_from_id(id)

    def __repr__(self):
        return self.name.name

    def fullname(self):
        return self.name.name


def get_state_from_id(id):
    match int(str(id)[0]):
        case 1: return "b"
        case 2: return "k"
        case 3: return "n"
        case 4: return "o"
        case 5: return "s"
        case 6: return "st"
        case 7: return "t"
        case 8: return "v"
        case 9: return "w"
        case _: return ""


def get_imagename_from_id(id):
    default_name = "default"
    path = "luftfilterbegehren/static/img/cities/"
    fullpath = path + str(id) + ".png"
    import os
    if os.path.exists(fullpath):
        return str(id)
    else:
        return default_name


def load_cities(filename):
    cities = []

    with open("luftfilterbegehren/data/" + filename, "r") as f:
        lcities = load(f)

    for lcitykey in lcities:
        lcity = lcities[lcitykey]
        lname = lcity["name"]
        plz = lcity["plz"]
        name = Name(lname["name"])

        lcontact = lcity["contact"]
        twitter = lcontact.get("twitter", "")
        facebook = lcontact.get("facebook", "")
        phone = lcontact.get("phone", "")

        contact = Contact(lcontact["mail"], phone, facebook, twitter)
        city = City(lcity["id"], name, plz, contact)
        cities.append(city)

    return cities


CitiesObjects = Cities()

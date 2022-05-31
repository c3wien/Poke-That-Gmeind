from random import choice
from datetime import datetime, timedelta
from re import match
from flask import (Blueprint, render_template, abort, request, url_for,
                   flash, redirect)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from config import DEBUG
from database.models import (Mail, Sender, Cities)
from database import db_session

mod = Blueprint("act", __name__, url_prefix="/act")
citiesObjects = Cities()


@mod.route("/mail/", methods=["POST"])
def mail():
    id = request.form.get("id")
    city = citiesObjects.get_city_by_id(id)
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    mail_user = request.form.get("email")

    if not all([city, firstname, lastname, mail_user]) or not city.contact.mail or id == "00000" or not match(r"[^@]+@[^@]+\.[^@]+", mail_user):
        abort(400)  # bad request

    name_user = firstname + " " + lastname

    try:
        sender = db_session.query(Sender).filter_by(email_address=mail_user).one()


        mail = Mail(sender, id)

        try:
            db_session.add(mail)
            db_session.commit()

            if sender.date_validated:
                # sender is authorized to send mails
                flash("Vielen Dank für deine Teilnahme.")
                mail.send()
                db_session.commit()
            else:
                if datetime.now() - sender.date_requested > timedelta(5):
                    # validation request expired
                    flash("Deine Bestätigungsanfrage ist abgelaufen. Um fortzufahren, bestätige bitte den Link, den wir an {mail_user} gesendet haben.".format(mail_user=sender.email_address))
                    sender.request_validation()
                    db_session.commit()
                else:
                    # validation request needs to be confirmed
                    flash("Danke für dein Engagement. Um fortzufahren, bestätige bitte den Link, den wir an {mail_user} gesendet haben.".format(mail_user=sender.email_address))

        except IntegrityError:
            flash("Du hast {city_name} bereits eine E-Mail geschrieben.".format(city_name=str(city)))
            db_session.rollback()

    except NoResultFound:
        # sender never sent mail before
        sender = Sender(name_user, mail_user, city)
        db_session.add(sender)
        mail = Mail(sender, id)
        db_session.add(mail)
        db_session.commit()
        flash("Danke für dein Engagement. Um fortzufahren, bestätige bitte den Link, den wir an {mail_user} gesendet haben.".format(mail_user=sender.email_address))

    return redirect(url_for("general.city", prettyname=city.name.prettyname, _anchor="email-senden"))


@mod.route("/validate/<hash>", methods=["GET"])
def validate(hash):
    try:
        sender = db_session.query(Sender).filter_by(hash=hash).one()

        if sender.date_validated:
            flash("Du hast deine E-Mail Adresse bereits erfolgreich verifiziert.")
        elif datetime.now() - sender.date_requested > timedelta(5):
            flash("Deine Bestätigungsanfrage ist abgelaufen. Um fortzufahren, bestätige bitte den Link, den wir an {mail_user} gesendet haben.".format(mail_user=sender.email_address))
            sender.request_validation()
        else:
            flash("Vielen Dank, Du hast deube E-Mail Adresse erfolgreich verifiziert.")
            sender.validate()
            for mail in sender.mails:
                mail.send()
            db_session.commit()

    except NoResultFound:
        flash("Dieser Bestätigungslink ist ungültig.")

    return render_template("act/validate.html")

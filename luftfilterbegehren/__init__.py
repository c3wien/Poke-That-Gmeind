from flask import Flask, render_template
from flask_mail import Mail
from config import SECRET_KEY, DEBUG
from config import MAIL_HOST, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from config import MAIL_USE_TLS
from flask_mail import Message
from database import init_db, db_session

from luftfilterbegehren.views import general
from luftfilterbegehren.views import act

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config.from_pyfile("../config/main.py")
app.config.from_pyfile("../config/mail.py")
app.debug = DEBUG
init_db()

app.config['MAIL_SERVER'] = MAIL_HOST
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS

mail = Mail(app)

app.register_blueprint(general.mod)
app.register_blueprint(act.mod)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()

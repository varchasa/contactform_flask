from flask import Flask, render_template,request,jsonify
from flask_mail import Mail,Message
import smtplib
import imghdr
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



app=Flask(__name__)
mail = Mail(app)
"""
app.config["MAIL_SERVER"]= 'smtp.gmail.com',
app.config["MAIL_PORT"]= 465,
app.config["MAIL_USE_TLS"]= False,
app.config["MAIL_USE_SSL"]= True,
app.config["MAIL_USERNAME"]= 'varchasa.tech@gmail.com',
app.config["MAIL_PASSWORD"]= 'varchasa@0602'
app.config['MAIL_DEFAULT_SENDER'] = 'default_sender_email'
app.config['MAIL_ASCII_ATTACHMENTS'] = True
app.config['DEBUG'] = True
"""

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'varchasa.tech@gmail.com',
	MAIL_PASSWORD = 'varchasa@0602'
	)


mail = Mail(app)
@app.route("/")
def home():
    

    return render_template('home.html')

@app.route("/send_message", methods=["GET","POST"])
def send_message():
    try:
        if request.method == 'POST':
        
            print("done1")
        
            print("done2")
        

            name=request.form['name']
            gmail=request.form['email']
            suggestion=request.form['suggestion'] 
            to = 'varchasa.tech@gmail.com'
            print("done4")
        
    
            text = Message(name, sender = gmail, recipients=[to])
            text.body=suggestion+" "+gmail
            
            
            print("done3")
            print(text)
            mail.send(text)
            return render_template("home.html")
    except:
        return('PLEASE FILL OUT THE REQUIRED DATA')
        



if __name__ == '__main__':
    app.run(debug=True)
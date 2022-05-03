import datetime

from flask import Flask, make_response, request

app = Flask(__name__)

my_form="""
        <html>
          <head>
            <title>Testet POST Flask</title>
          </head>
          <body>

            <h1>Formular f&uuml;r Namenseingabe</h1>

              <form action="setcookie" method="post">
                <p>Vorname:<br><input name="vorname" type="text" size="30" maxlength="3000"></p>
                <p>Zuname:<br><input name="name" type="text" size="30" maxlength="40"></p>
                <p><input type="submit" value=" Absenden "> <input type="reset" value=" Abbrechen"></p>
              </form>

          </body>
        </html>
           """

@app.route('/')
def anmelden():
    resp=make_response("Willkommen bei Gymboard! Bitte melde dich doch an.<br><a href='/form'>ANMELDUNG</a><br>")
    return resp

@app.route('/form')
def form():
    return my_form

@app.route('/setcookie', methods=['POST', 'GET'])
 if "Name" in request.cookies:
   def setcookie():
     if request.method == 'POST':
        name_cookie=request.form['vorname']+"  "+request.form['name']
        resp = make_response("Erfolgreich angemeldet. Hier kannst du deine Angaben überprüfen oder dich abmelden:<br><a href='/getcookie'>Überprüfen&Abmelden</a><br>")
        resp.set_cookie('Name',name_cookie,expires=datetime.datetime.now() + datetime.timedelta(days=1))
        return resp
 else:
   resp= make_response("<script>window. location. href="127.0.0.1:5000";</script>")
   resp
  



@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Name')
    return "Name : "+name+ "<br><a href='/delcookie '>ABMELDEN</a><br>"

@app.route('/delcookie')
def delcookie():
    resp=make_response("erfolgreich abgemeldet")
    resp.delete_cookie('Name')
    return resp

if __name__ == '__main__':
    app.run(debug=True)


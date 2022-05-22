import datetime

from flask import Flask, make_response, request

app = Flask(__name__)

# Für alle erreichbare Seiten

@app.route('/')
def homepage():
    html="<!DOCTYPE html><html><head><title>homepage</title></head><body>"
    if "email" in request.cookies:
      name = request.cookies.get('email')
      html=html+"E-Mail : "+name+ " <a href='/delcookie?page=/'>abmelden</a><br><br>"
    else:
      html=html+"Sie sind nicht angemeldet. <a href='/form?page=/'>anmelden</a><br><br>"
    html=html+"<a href = '/seite_a'>seite_a</a><br><a href = '/seite_b'>seite_b</a><br><a href = '/seite_c'>seite_c</a><br>"
    if "email" in request.cookies:
        html=html+"<a href = '/seite_d'>seite_d (nur mit Anmeldung)</a><br>"
    html=html+"</body></html> "
    return html

@app.route('/form' , methods=['GET'])
def form():
    html="""
            <html>
              <head>
                <title>Anmeldung</title>
              </head>
              <body>

                <h3>Anmelden mit E-Mail des Gymnasiums Interlaken</h3>

                  <form action="/setcookie?page="""+request.args.get('page')+"""" method="POST">
                    <p>Mail Adresse Gymnasium Interlaken:<br><input name="email" type="text" size="30" maxlength="3000"></p>
                    <p><input type="submit" value=" Absenden "> <input type="reset" value=" Abbrechen"></p>
                  </form>

              </body>
            </html>
               """
    return html

@app.route('/seite_a')
def seite_a():
    html="<!DOCTYPE html><html><head><title>seite_a</title></head><body>"
    if "email" in request.cookies:
      name = request.cookies.get('email')
      html=html+"E-Mail : "+name+ " <a href='/delcookie?page=seite_a '>abmelden</a><br><br>"
    else:
      html=html+"Sie sind nicht angemeldet. <a href='/form?page=seite_a'>anmelden</a><br><br>"
    html=html+"<a href='/'>homepage</a><br><a href = '/seite_b'>seite_b</a><br><a href = '/seite_c'>seite_c</a><br>"
    if "email" in request.cookies:
        html=html+"<a href = '/seite_d'>seite_d (nur mit Anmeldung)</a><br>"
    html=html+"</body></html> "
    return html

@app.route('/seite_b')
def seite_b():
    html="<!DOCTYPE html><html><head><title>seite_b</title></head><body>"
    if "email" in request.cookies:
      name = request.cookies.get('email')
      html=html+"E-Mail : "+name+ " <a href='/delcookie?page=seite_b '>abmelden</a><br><br>"
    else:
      html=html+"Sie sind nicht angemeldet. <a href='/form?page=seite_b'>anmelden</a><br><br>"
    html=html+"<a href='/'>homepage</a><br><a href = '/seite_a'>seite_a</a><br><a href = '/seite_c'>seite_c</a><br>"
    if "email" in request.cookies:
        html=html+"<a href = '/seite_d'>seite_d (nur mit Anmeldung)</a><br>"
    html=html+"</body></html> "
    return html

@app.route('/seite_c')
def seite_c():
    html="<!DOCTYPE html><html><head><title>seite_c</title></head><body>"
    if "email" in request.cookies:
      name = request.cookies.get('email')
      html=html+"E-Mail : "+name+ " <a href='/delcookie?page=seite_c '>abmelden</a><br><br>"
    else:
      html=html+"Sie sind nicht angemeldet. <a href='/form?page=seite_c'>anmelden</a><br><br>"
    html=html+"<a href='/'>homepage</a><br><a href = '/seite_a'>seite_a</a><br><a href = '/seite_b'>seite_b</a><br>"
    if "email" in request.cookies:
        html=html+"<a href = '/seite_d'>seite_d (nur mit Anmeldung)</a><br>"
    html=html+"</body></html> "
    return html

# Seite nur fuer Angemeldete
@app.route('/seite_d')
def seite_d():
    html="<!DOCTYPE html><html><head><title>seite_cd</title></head><body>"
    if "email" in request.cookies:
      name = request.cookies.get('email')
      html=html+"E-Mail : "+name+ " <a href='/delcookie?page=seite_d '>abmelden</a><br><br>"
      html=html+"<a href='/'>homepage</a><br><a href = '/seite_a'>seite_a</a><br><a href = '/seite_b'>seite_b</a><br><a href = '/seite_c'>seite_c</a><br>"
      html=html+"Das kann man nur sehen, wenn man angemeldet ist!"
    else:
      html=html+"Sie sind nicht angemeldet. <a href='/form'>anmelden</a><br><br>Diese Seite ist nur als angemeldete*r User zug&auml;nglich!"
    html=html+"</body></html> "
    return html

# Seiten für Cookies

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    email=''
    path='/'
    if request.method == 'GET':
        path=request.args.get('page')
    if request.method == 'POST':
        email_cookie=request.form['email']
        resp = make_response('<script>window. location. href="'+request.args.get('page')+'";</script>')
        resp.set_cookie('email',email_cookie,expires=datetime.datetime.now() + datetime.timedelta(days=1))
        return resp

@app.route('/delcookie', methods=['GET'])
def delcookie():
  if "email" in request.cookies:
    resp=make_response('<script>window. location. href="'+request.args.get('page')+'";</script>')
    resp.delete_cookie('email')
    return resp
  else:
    resp= make_response('<script>window. location. href="/";</script>')
    return resp


if __name__ == '__main__':
    app.run(debug=True)

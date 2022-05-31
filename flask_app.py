import datetime

from flask import Flask, make_response, request, render_template

app = Flask(__name__, template_folder='templates')

# Für alle erreichbare Seiten

@app.route('/form' , methods=['GET'])
def form():
    return render_template('form.html',page=request.args.get('page'))

@app.route('/', methods=['GET'])
def homepage():
    email="0"
    if "email" in request.cookies:
      email = request.cookies.get('email')
    return render_template('site.html',page='/', email=email, menu=['seite_a','seite_b','seite_c'])

@app.route('/seite_a')
def seite_a():
    email="0"
    page=request.args.get('page')
    if "email" in request.cookies:
      email = request.cookies.get('email')
    return render_template('site.html',page='seite_a', email=email, menu=['/','seite_b','seite_c'])

@app.route('/seite_b')
def seite_b():
    email="0"
    if "email" in request.cookies:
      email = request.cookies.get('email')
    return render_template('site.html',page='seite_b', email=email, menu=['/','seite_a','seite_c'])

@app.route('/seite_c')
def seite_c():
    email="0"
    if "email" in request.cookies:
      email = request.cookies.get('email')
    return render_template('site.html',page='seite_c', email=email, menu=['/','seite_a','seite_b'])


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

@app.route('/setcookie', methods=['POST'])
def setcookie():
    email=''
    path='/'
    if request.method == 'POST':
        page = request.form['page']
        email_cookie=request.form['email']
        angemeldet_bleiben = request.form.getlist('permanent')
        resp = make_response('<script>window. location. href="'+page+'";</script>')
        if len(angemeldet_bleiben) >0:
            resp.set_cookie('email',email_cookie,expires=datetime.datetime.now() + datetime.timedelta(days=1))
        else:
            resp.set_cookie('email',email_cookie)
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

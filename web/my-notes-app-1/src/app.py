import json
import time
from flask import (Flask, make_response, render_template, request, send_from_directory, jsonify)
import jwt
from config import JUST_DONT_SHARE_SECRET_CONTENT, KINDA_SECRET_CONTENT, NATIONAL_SECURITY_IMPORTANT_SECRET_CONTENT, NOT_A_SECRET, SECRET_CONTENT, SECRET_KEY, SEMI_SECRET_CONTENT, ULTRA_SECRET_CONTENT
import uuid
import base64

app = Flask(__name__)
app.config.from_object('config')
app.debug = True

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

@app.route('/')
def index_page():
    token = request.cookies.get('jwt')
    # RS256 is the best format https://www.rfc-editor.org/rfc/rfc8725.html#section-2.1
    if not token: token = jwt.encode({'admin': False, 'now': time.time(), 'sub': str(uuid.uuid4()), 'exp': time.time() + 100000, 'secret': SECRET_CONTENT}, SECRET_KEY, algorithm='RS256')
    admin = bool(json.loads(base64.b64decode(token.split('.')[1]+"=="))["admin"])

    r = make_response(render_template("index.html", admin=admin))
    r.set_cookie('jwt', token)
    r.set_cookie('tz', '+11')
    return r

@app.route('/source', methods=['GET'])
def source():
    return send_from_directory('./','app.py')

@app.route('/public_key')
def secret():
    """
    Help others know about when we are signing something!
    """
    return NOT_A_SECRET

# very secure note taking system
notes = {
    "e7b571fd-b053-4138-ad59-19303482798e": [SEMI_SECRET_CONTENT],
    "98f0d9c9-2792-45f1-bac7-86434de71cde": [KINDA_SECRET_CONTENT],
    "d7962ed3-5c7d-4093-a6c2-89c565607f6a": [ULTRA_SECRET_CONTENT],
    "21db5637-ee66-4687-a7e7-9165b18b98c4": [JUST_DONT_SHARE_SECRET_CONTENT],
}

@app.route('/mynotes', methods = ['GET'])
def my_notes():
  try:
    # Ok i should undo the testing for this nice old exploit! `jpadilla/pyjwt#109`
    # payload = jwt.decode(request.cookies.get('jwt'), SECRET_KEY, algorithms=['RS256'])
    payload = jwt.decode(request.cookies.get('jwt'), NOT_A_SECRET, algorithms=['RS256', 'none'])

    if payload['admin']:
        # if admin, then show the important info for them too!
        return render_template("mynotes.html", name=payload["sub"], saved_notes=((notes.get(payload["sub"]) or []) + [SECRET_KEY]))
    else:
        return render_template("mynotes.html", name=payload["sub"], saved_notes=(notes.get(payload["sub"]) or []))
  except Exception as error:
      print(error)
      return render_template("mynotes.html", name="<unknown>", saved_notes=[":^("+str(error)]) 
  
@app.route('/mynotes', methods = ['POST'])
def add_note():
    token = request.cookies.get('jwt')
    if not token: return jsonify({"error": "not logged in :("})
    payload = jwt.decode(request.cookies.get('jwt'), NOT_A_SECRET, algorithms=['RS256'])
    id = payload["sub"]

    if not id in notes: notes[id] = []
    notes[id] += [request.form["input"]]

    return render_template("mynotes.html", name=payload["sub"], saved_notes=notes[id])


@app.route('/admin', methods = ['GET'])
def yo_admin():
    try:
        payload = jwt.decode(request.cookies.get('admin_jwt'), NATIONAL_SECURITY_IMPORTANT_SECRET_CONTENT, algorithms=['HS256'], leeway=int(request.cookies.get('tz') or 0)*60*60)
        if payload['admin']:
                return render_template("admin.html", secret=NATIONAL_SECURITY_IMPORTANT_SECRET_CONTENT)
        else:
            return render_template("admin.html", message=f"Hey! You aren't the admin!\nBut maybe you'd like this {ULTRA_SECRET_CONTENT}")
    except Exception as error:
        print(error)
        # sesh_token = jwt.encode({'admin': True, 'now': time.time(), 'sub': str(uuid.uuid4()), 'exp': time.time() - 1000000, 'secret': SECRET_CONTENT}, NATIONAL_SECURITY_IMPORTANT_SECRET_CONTENT, algorithm='HS256')
        # return sesh_token
        return render_template("404.html"), 404

if __name__ == '__main__':
    app.run()


# example of token - dont worry this is expired and not useful!
DEV_ADMIN_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZSwibm93IjoxNzIxOTE1OTY0LjM4NDA2MjgsInN1YiI6IjYzZjQyMDhjLWM0ZDgtNGRlMi05N2ZhLTM5ZTE3OTM4MjM1OSIsImV4cCI6MTcyMDkxNTk2NC4zODQwOTYxLCJzZWNyZXQiOiJwZWNhbntqd3RfMXpfanV6dF9qNTBuP30ifQ.N8LHWRs4EPL6pLEgdNEHt1w2Nr29efl-MgURMpcnWMc" 

import flask
import datetime

import alphabeta.pace

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(seconds=1)

@app.route('/')
def hello_world():
  return flask.redirect(flask.url_for('static', filename='index.html'))
  # return 'Hello, World!'

@app.route('/pace', methods=['POST'])
def route_pace():
  req_json = flask.request.get_json()
  checkerboard = req_json['data']['checkerboard']
  maxDepth = req_json['data']['depth']
  pace = alphabeta.pace.getPace(checkerboard, maxDepth)
  if pace:
    return ''.join([str(i) for i in pace])
  else:
    return ''

app.run(host="0.0.0.0", port=int("8080"), debug=True)
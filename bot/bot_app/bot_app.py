from bottle import route, run, template, request
from bot import bot

@route('/hello')
def hello():
  return template('bot_template', input_text='', output_text='')


@route('/hello', method='POST')
def do_hello():
  input_text = request.forms.input_text
  output_text = bot(input_text)
  return template('bot_template', input_text=input_text, output_text=output_text)


run(host='localhost', port=8080, debug=True)
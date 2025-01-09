from flask import Flask, render_template, jsonify

app = Flask(__name__)

LISTS = [
  {
    'id': 1,
    'title': 'To-Do',
    "type": "Task List"
  },

  {
    'id': 2,
    'title': 'Grocery',
    "type": "Grocery items"
  },

  {
    'id': 3,
    'title': 'Instruction',
    "type": "List of Instructions"
  },

  {
    'id': 4,
    'title': 'Custom',
    "type": "Customized List"
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', lists=LISTS)

@app.route("/api/lists")
def task_list():
  return jsonify(LISTS)

print (__name__)
if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
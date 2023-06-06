from flask import Flask, render_template, jsonify

app = Flask (__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary' : 'Rs 215.000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location': 'Dehli, India',
    'salary' : 'Rs 150.000'
  },
  {
    'id' : 3,
    'title' : 'Front End Engineer',
    'location': 'Remote',
    'salary' : 'Rs 80.000'
  },
  {
    'id' : 4,
    'title' : 'Back End Engineer',
    'location': 'San Francisco, US',
    #'salary' : '$ 200.000'
  },
]

@app.route ("/")
def hello_world ():
  return render_template ('home.html',
                          jobs = JOBS,
                         company_name = 'Jovian'
                         )
@app.route ("/api/jobs")
def list_jobs ():
  return jsonify (JOBS)

if __name__ == "__main__":
  app.run (host='0.0.0.0', debug = True)
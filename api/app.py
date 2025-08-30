from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Gurugram,India',
        'salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'AI/ML Engineer',
        'location':'Dehli,India',
        'salary':'Rs. 20,00,000'
    },
    {
        'id':4,
        'title':'Dev Ops',
        'location':'Bengaluru,India',
        'salary':'Rs. 12,00,000'
    }
]

@app.route('/')
def hello_careers():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Mouse')

@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)

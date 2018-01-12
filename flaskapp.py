from flask import Flask, render_template, request, flash
from forms import ContactForm
import MySQLdb
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
       if form.validate() == False:
           flash('All fields are required.')
           return render_template('index.html', form = form)
       else:
           if insert(request.form['name'],request.form['color'],request.form['pet']) == True:
               form.resultMessage = "Inserted Successfully"
               form .result = True
               return render_template('index.html', form = form)
           else:
               form.resultMessage = "Insertion Failed, please enter a unique name"
               form .result = False
               return render_template('index.html', form = form)
   elif request.method == 'GET':
       return render_template('index.html', form = form)
@app.route('/view')
def render_static():
    return render_template('view.html', rows = view())
def view():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="nkumar",         # your username
                         passwd="nkumar123",  # your password
                         db="pythondb")
    cur = db.cursor()
    cur.execute("SELECT * FROM usertest")
    return cur.fetchall()
def insert(name,color,pet):
       db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="nkumar",         # your username
                         passwd="nkumar123",  # your password
                         db="pythondb")
       cur = db.cursor()
       try:
         print(name,color,pet)
         cur.execute("""INSERT INTO usertest VALUES(%s,%s,%s)""",(name,color,pet))
         db.commit()
         return True
       except:
           db.rollback()
           return False

if __name__ == '__main__':
   app.run(debug = True)

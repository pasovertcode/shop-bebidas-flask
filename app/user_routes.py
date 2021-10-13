from flask.templating import render_template
from app import app

@app.route("/user/profile")
def user_profile():
    #if sesion in 
    return render_template('public/user-profile.html')

from flask.templating import render_template
from app import app
from flask import session

@app.route("/user/profile")
def user_profile():
    # if session is on and verify what type of user is and get template of .
    if session.get('logged_in') == True:
        if session['type'] == 1:
            return render_template('admin/admin-profile.html')
        elif session['type'] == 2:
            return render_template('admin/super-admin-profile.html')
        
        return render_template('public/user-profile.html')
    
    return render_template('public/error.html', error = "Error 404 not found")
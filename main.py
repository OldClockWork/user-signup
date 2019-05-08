from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET"])
def index():
    return render_template("signup.html")


@app.route("/signup_confirm", methods=["POST"])
def signup_confirmation():
    user = request.form['user']
    password = request.form['password']
    repassword = request.form['repassword']
    email = request.form['email']

    name_error = ""
    pass_error = ""
    repass_error = ""
    email_error = ""

#----------------------------Userame
    if(user == ""):
        name_error = "Error: Please, input a name."
        user = ""
    elif(" " in user):
        name_error = "Error: Name can not contain whitespaces."
        user = ""
    elif(len(user) < 3 or len(user) > 20):
        name_error = "Error: To few or to many characters. Username can only contain 3 - 20 characters."
        user = ""

#----------------------------Password
    if(password == ""):
        pass_error = "Error: Please, input a password."
        password = ""
    elif(" " in password):
        pass_error = "Error: Password can not contain whitespaces."
        password = ""
    elif(len(password) < 3 or len(password) > 20):
        pass_error =  "Error: To few or to many characters. Password can only contain 3 - 20 characters."
        password = ""
    
    if(repassword != password):
        repass_error = "Error: Password does not match."
        repassword = ""

#----------------------------Email
    if(email == ""):
        email = ""
    elif(" " in email):
        email_error = "Error: Email can not contain white spaces."
        email = ""
    elif("@" not in email):
        email_error = "Error: Email does not contain @."
        email = ""
    elif(".com" not in email):
        email_error = "Error: Email does not contain .com"
        email = ""
    elif(len(email) < 3 or len(email) > 20):
        email_error = "Error: To few or to many characters. Email can only contain 3 - 20 characters."
        email = ""


    if(name_error == "" and pass_error == "" and repass_error == "" and email_error == ""):
        return render_template("signup_confirm.html", user=user)
    else:
        return render_template("signup.html", 

        name_error = name_error, 
        pass_error = pass_error,
        repass_error = repass_error,
        email_error = email_error, 

        user = user,
        password = password,
        repassword = repassword,
        email = email)


if __name__ == "__main__":
    app.run()
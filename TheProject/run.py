
from flask import Flask, render_template, request,redirect, url_for,flash,session
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, login_required,login_user,LoginManager,logout_user,current_user
from __init__ import create_app
from __init__ import login_manager
from __init__ import db
app = create_app()
from codemodules.forms import CreateUser, LoginForm,EditUser,addClothing
from codemodules.models import UserModel,ClothingModel,PostModel
from werkzeug.utils import secure_filename
from __init__ import create_app
import uuid as uuid
import os
import json
import shutil

with open("static/outfitStyles.json", "r", encoding='utf-8') as skra: # encoding fyrir sÃ©r Ã­slenska stafi
    outfitStyles = json.load(skra)    
    skra.close()


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))



@app.route("/",methods=["GET"])
def index():
    posts = PostModel.query.all()
    clothing = ClothingModel.query.all()
    image_list = []
    postsDict={}
    return render_template("index.html",posts=posts,clothing=clothing,image_list=image_list,postsDict=postsDict)

@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():
    userClothes = current_user.clothings
    return render_template("userDashboard.html",clothing=userClothes)
@app.route("/userProfile/<int:id>",methods=["GET"])
def userProfile(id):
    user = UserModel.query.get(id)
    userClothes = user.clothings
    userPosts = user.posts
    return render_template("userProfile.html",user=user,clothing=userClothes)
@app.route("/login",methods=["GET","POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = UserModel.query.filter_by(username=loginForm.username.data).first()
        if user:
            if check_password_hash(user.password_hash,loginForm.password.data):
                login_user(user)
                flash("Logged In","success")
                return redirect(url_for("dashboard"))
            else: 
                flash("Incorrect password","negative")
        else:
            flash(f"User {loginForm.username.data} doesn't exist","negative")

    return render_template("login.html",form=loginForm)

@app.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You Have Logged out","blue")
    return redirect(url_for("index"))

@app.route("/delete_current_user",methods=["GET"])
@login_required
def delete_user():
    user_delete = current_user
    shutil.rmtree(app.config["UPLOAD_FOLDER"]+f"{current_user.id}_{current_user.username}")
    db.session.delete(user_delete)
    user_delete_clothing = user_delete.clothings
    for item in user_delete_clothing:  
        db.session.delete(item)
        os.remove(f"static/clothes_images/{item.image_link}")
    db.session.commit()
    flash(f"user: {user_delete.username} deleted","red")
    return redirect(url_for("index"))

@app.route("/create_user",methods=["GET","POST"])
def create_user():
    signUpForm = CreateUser()
    if signUpForm.validate_on_submit():
        userEmail = UserModel.query.filter_by(email=signUpForm.email.data).first() 
        userUsername = UserModel.query.filter_by(username=signUpForm.username.data).first() 
        if userEmail:
            flash("Email in use","yellow")
        if userUsername:
            flash("Username in use","yellow")
        if userUsername  == None and userEmail == None:
            hashed_password = generate_password_hash(signUpForm.password.data,"sha256")
            user = UserModel(   name=signUpForm.name.data,
                                username=signUpForm.username.data,
                                email=signUpForm.email.data,
                                password_hash = hashed_password
                            )
            db.session.add(user)
            db.session.commit()
            path = os.path.join(app.config["UPLOAD_FOLDER"],f"{user.id}_{user.username}")
            os.mkdir(path)
            signUpForm.name.data = ""
            signUpForm.username.data = ""
            signUpForm.email.data = ""

            flash("User added","success")
            login_user(user)

            return redirect("dashboard")

    return render_template("CreateUser.html",form=signUpForm)

@app.route("/editUser",methods=["GET","POST"])
@login_required
def edit_user():
    edit_userForm = EditUser()
    if edit_userForm.validate_on_submit():
        logged_user = UserModel.query.get(current_user.id)
        logged_user.id  = current_user.id
        logged_user.username = edit_userForm.username.data
        logged_user.name = edit_userForm.name.data
        logged_user.email = edit_userForm.email.data
        logged_user.bio = edit_userForm.bio.data
        if edit_userForm.profile_picture != None:
            profile_pic = edit_userForm.profile_picture.data
            pic_filename = secure_filename(profile_pic.filename)
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            profile_pic.save(os.path.join(app.config["UPLOAD_FOLDER"]+str(current_user.id)+"_"+str(current_user.username),pic_name))
            logged_user.profile_picture = pic_name
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("userSettings.html",form=edit_userForm)

@login_required
def logout():
    logout_user()
    flash("You Have Logged out","blue")
    return redirect(url_for("index"))

@app.route("/addClothing",methods=["GET","POST"])
@login_required
def addNewClothing():
    addClothingForm = addClothing()
    if addClothingForm.validate_on_submit():
        picture = addClothingForm.picture.data
        picture_filename = secure_filename(picture.filename)
        picture_name = str(uuid.uuid1()) + "_" + picture_filename
        picture.save(os.path.join(app.config["UPLOAD_CLOTHES_FOLDER"],picture_name))
        
        clothing = ClothingModel(
                                type = addClothingForm.type.data,
                                describtion = addClothingForm.description.data,
                                image_link = picture_name,
                                user_id = current_user.id
                                )
        db.session.add(clothing)
        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("addClothing.html",form=addClothingForm) 
@app.route("/deleteClothing/<int:id>",methods=["GET"])
@login_required
def deleteClothing(id):
    clothing_delete = ClothingModel().query.get(id)
    db.session.delete(clothing_delete)
    db.session.commit()
    return redirect("/dashboard")

@app.route("/postMenu",methods=["GET"])  
@login_required
def postMenu():
    return render_template("postMenu.html")

@app.route("/addPost",methods=["GET","POST"]) 
@login_required 
def addPost():
    if session.get("Post") == None:
        session['Post'] = {"hat":0 ,"shirt":0,"jacket":0,"gloves":0,"pants":0,"shorts":0,"shoes":0,"socks":0}
    types = ["hat","shirt","jacket","gloves","pants","shorts","shoes","socks"]
    clothingDict = {}
    post = session['Post']
    for type,id in post.items():
        if id !=0:
            clothingDict[type] = ClothingModel().query.get(id)
        else:
            clothingDict[type] = 0
    
    return render_template("addPost.html",types=types,post=clothingDict)

@app.route("/publishPost",methods=["GET"])
@login_required
def publishPost():
    nullPostCheck = True
    post = session['Post']
    for type,id in post.items():
        if id != 0:
            nullPostCheck = False
    if nullPostCheck:
        flash("You have to add items to your outfit","negative")
        return redirect("/addPost")
    else:
        newPost = PostModel(user_id  = current_user.id)
        for type,id in post.items():
            setattr(newPost, type, id)
        db.session.add(newPost)
        db.session.commit()
        session['Post'] = {"hat":0 ,"shirt":0,"jacket":0,"gloves":0,"pants":0,"shorts":0,"shoes":0,"socks":0}
        return redirect("/")

@app.route("/selectCloting/<string:clothingtype>",methods=["GET","POST"])  
@login_required
def selectCloting(clothingtype):
    clothes = ClothingModel().query.filter_by(type=clothingtype).all()
    return render_template("selectClothing.html",clothingtype=clothingtype,clothes=clothes)

@app.route("/addClotingToPost/<int:itemId>",methods=["GET","POST"])  
@login_required
def addClotingToPost(itemId):
    clothing = ClothingModel.query.get(itemId)
    post = session['Post']
    post[clothing.type] = clothing.id
    session['Post'] = post
    return redirect('/addPost')

@app.route("/removeClotingToPost/<string:type>",methods=["GET","POST"]) 
@login_required
def removeClotingToPost(type):
    post = session['Post']
    post[type] = 0
    session['Post'] = post
    return redirect('/addPost')

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/") # gera custom page seinna


@app.route("/whatToWear")
def whatToWear():
    
    return render_template("whatShouldWear.html", styles = outfitStyles)


@app.route("/outfitStyle/<string>")
def outfit(string):
    for i in range(len(outfitStyles)):
        if outfitStyles[i]["name"] == string:
            info = outfitStyles[i]
    
    return render_template("outfitStyle.html", gogn = info, name = string)




@app.errorhandler(500)
def page_not_found(e):
    return redirect("/") # gera custom page seinna

@app.errorhandler(401)
def page_not_found(e):
    flash("You Dont have premission to enter this page please log in","negative")
    return redirect("/login") 

if __name__ == "__main__":
    app.run(debug=True)

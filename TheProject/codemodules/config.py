class Config():
    UPLOAD_FOLDER = "static/profile_data/"
    UPLOAD_CLOTHES_FOLDER = "static/clothes_images/"

    SECRET_KEY = "password"

    UPLOAD_FOLDER = UPLOAD_FOLDER
    UPLOAD_CLOTHES_FOLDER = UPLOAD_CLOTHES_FOLDER

    SQLALCHEMY_DATABASE_URI= "sqlite:///database/database.db"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password123@localhost/flask_database"
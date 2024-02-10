from firebase_admin import db
import firebase_admin

def firebase_upload():
    cred_obj = firebase_admin.credentials.Certificate("good-news-5c3d8-firebase-adminsdk-lw5cz-55b84d72bb.json")
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': "https://good-news-5c3d8-default-rtdb.europe-west1.firebasedatabase.app/"
    })
        
    # find database
    ref = db.reference("/")

    # upload data
    ref.set(scraped_article_data)
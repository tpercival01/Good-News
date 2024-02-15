from firebase_admin import db
import firebase_admin
import sentimental_analysis

def firebase_upload():
    cred_obj = firebase_admin.credentials.Certificate("good-news-5c3d8-firebase-adminsdk-lw5cz-13e9ca5761.json")
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': "https://good-news-5c3d8-default-rtdb.europe-west1.firebasedatabase.app/"
    })
        
    # find database
    ref = db.reference("/")

    sentimental_data = sentimental_analysis.main()
    #sentimental_data = sentimental_data.to_dict()

    sentimental_data = sentimental_data.transpose().to_dict()

    # upload data
    ref.set(sentimental_data)


if __name__ == "__main__":
    firebase_upload()
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "林煥杰",
  "mail": "a0909123137@gmail.com",
  "lab": 579
}

doc_ref = db.collection("靜宜資管").document("LIN HUAN-CHIEH")
doc_ref.set(doc)
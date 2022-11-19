from flask import Flask 

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertified=DigiCertGlobalRootCA.crt;UID=hqv31422;PWD=u6kXUYiZPdMxEEvJ",'','')
print(conn)
print("Connection Succesful......")


app = Flask(__name__)

@app.route('/')
def index():
    return "<center><h1>DB Connected Successfully....</h1><p>Team ID: PNT2022TMID48197<br>Amal<br>Aishwarya<br>Thaslima Banu<br>Rabiya Barvin</p></center>"

from flask import Flask
from flask import request
from moralis import auth
from flask_cors import CORS

from datetime import datetime, timedelta, timezone

app = Flask(__name__)
CORS(app,origins=['*'])

api_key = "YOUR_API_KEY"

@app.route('/requestChallenge', methods=["GET"])
def reqChallenge():
    
    args = request.args
    
    present = datetime.now(timezone.utc)
    present_plus_one_m = present + timedelta(minutes=1)
    expirationTime = str(present_plus_one_m.isoformat())
    expirationTime = str(expirationTime[:-6]) + 'Z'

    body = {
        "domain": "my.dapp", 
        "chainId": args.get("chainId"), 
        "address": args.get("address"), 
        "statement": "Please confirm login", 
        "uri": "https://my.dapp/", 
        "expirationTime": expirationTime, 
        "notBefore": "2020-01-01T00:00:00.000Z", 
        "resources": ['https://docs.moralis.io/'], 
        "timeout": 30, 
    }
    

    result = auth.challenge.request_challenge_evm(
        api_key=api_key,
        body=body,
    )
    
    return result


@app.route('/verifyChallenge', methods=["GET"])
def verifyChallenge():

    args = request.args
    
    body={
        "message": args.get("message"), 
        "signature": args.get("signature"),
    }

    result = auth.challenge.verify_challenge_evm(
        api_key=api_key,
        body=body
    )
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
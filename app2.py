from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Response
import requests 
import json 
import random 

app = Flask(__name__,
    static_url_path = '',
    static_folder = 'templates'
)

app.secret_key = "hello"

thisTrxn = {
    "items": [],
    "id": 1234,
    "users": []
}

userProto = {
    "id": "",
    "name": "",
    "consent": False
}

# '/MERCHANT' ROUTES


@app.route('/merchant', methods=['GET'])
def menu():
    print("Inside menu page")
    return render_template('retailer/menu.html')

@app.route('/merchant/new', methods=['GET'])
## Add in all of the items in the cart
def createNew():
    print("imside new")
    return render_template('retailer/merchant.html')
#@app.route('pending')

# POST route
@app.route('/merchant/process', methods=['POST'])
def createNewId():
    d = request.get_json(force=True)
    print(d)
    thisTrxn['items'] = d['items'] 
    thisTrxn['id'] = random.randint(0, 10001)
    return {"id": thisTrxn['id']}, 201  
    # return redirect("/merchant/pending/" + str(thisTrxn['id'])), 201
    # return Response("{'id':{"+str(thisTrxn['id'])+"}", status=201, mimetype='application/json')

@app.route('/merchant/pending/<idn>')
def pendingTrxn(idn):
    print("REDIRECT WORKED")
    # if thisTrxn['id'] != int(idn): return '405'
    return render_template('retailer/Rmockbillsplit.html', id=369823)

#doesn't work!
@app.route('/user/join/<int:idn>')
def userJoin(idn):
    # if thisTrxn['id'] != int(idn): return '405'
    thisTrxn['users'].append(request.get_json(force=True)['user'])
    print("enter session")
    return render_template('user/mockbillsplit.html')

@app.route('/user/update/<idn>', methods=['POST'])
def updateValues(idn):
    # if thisTrxn['id'] != idn: return '405'
    thisTrxn['items'] = request.data.items

@app.route('/fetch/<idn>')
def fetchData(idn):
    #if thisTrxn['id'] != int(idn): return '405'
    return jsonify(thisTrxn)

# Creating order in the ncr system
@app.route('/create_order', methods=['GET', 'POST'])
def create_order():
    if request.method == "POST":
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form['last_name']
        session["amount"] = request.form['amount']

        url = "https://gateway-staging.ncrcloud.com/order/3/orders/1"

        payload = json.dumps({
          "customer": {
            "firstName": session['first_name'],
            "lastName": session['last_name']
          },
          "owner": "Loblaws",
          "payments": [
            {
              "amount": float(session['amount'])
            }
          ]
        })
        headers = {
          'Content-Type': 'application/json',
          'nep-organization': 'test-drive-27b00b4089b94035b0db4',
          'nep-enterprise-unit': '6df343ac26004ee29e027275a7173ed7',
          'Date': 'Sun, 24 Oct 2021 09:01:23 GMT',
          'Authorization': 'Basic MTg2NGZmZDAtYmZjOC00OTg0LTk0NDEtM2Y1NDllNjFlM2M5Ok5pbW1pb21hcjFA'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        session['transaction_id'] = response['id']


        return redirect(url_for('transaction_complete'))
    else:
        return render_template('user/payment.html')


@app.route('/transaction_complete')
def transaction_complete():
    return render_template('user/ordersuccess.html',transaction_id=session['transaction_id'] )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
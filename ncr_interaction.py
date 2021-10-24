from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import requests

app = Flask(__name__,
    static_url_path = '',
    static_folder = 'templates'
)

app.secret_key = "hello"


# Printing/Getting Out an Order with id 
@app.route('/getOrder', methods=['POST', 'GET'])
def get_order():
    if request.method == "POST":
        session["transaction_id"] = request.form["transaction_id"]
        url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/" + session['transaction_id']

        payload={}
        headers = {
          'Content-Type': 'application/json',
          'nep-organization': 'test-drive-27b00b4089b94035b0db4',
          'nep-enterprise-unit': '6df343ac26004ee29e027275a7173ed7',
          'Date': 'Sun, 24 Oct 2021 09:35:00 GMT',
          'Authorization': 'Basic MTg2NGZmZDAtYmZjOC00OTg0LTk0NDEtM2Y1NDllNjFlM2M5Ok5pbW1pb21hcjFA'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

        return response.text
    else:
        return render_template('/retailer/session.html')
        


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


        return redirect(url_for('transaction'))
    else:
        return render_template('user/payment.html')

    

@app.route('/transaction', methods=['GET'])
def transaction():
    print(session['amount'])
    return render_template('retailer/view.html', first_name=session["first_name"], last_name=session["last_name"],
    amount=session["amount"], order_id=session['order_id'], transaction_id=session['transaction_id'])


if __name__ == '__main__':
    
    app.run(debug=True, port=6000)
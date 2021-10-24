from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
import requests
import json

#use request

app = Flask(__name__,
    static_url_path = '',
    static_folder = 'templates'
)

Session(app)
socketio = SocketIO(app, manage_session=False)

#to be converted to a tuple before final send
#sessionObj = [sessionId, [[item1, p1], [item2, p2]]]
sessionObj = ["", []]
defaultOwner = {
    "index": -1,
    "name": "",
    "color": "gray"
}
items = [
            {
                "index": 0,
                "name": "Apples",
                "price": "2.50",
                "quantity": "3",
                "owner": defaultOwner
            },
            {
                "index": 1,
                "name": "Bananas",
                "price": "3.50",
                "quantity": "1",
                "owner": defaultOwner
            },
            {
                "index": 2,
                "name": "Pear",
                "price": "3.10",
                "quantity": "5",
                "owner": defaultOwner
            }
        ]


@app.route('/echo/<name>')
def index(name):
    return render_template('user.html', name="Hi " + name)

@app.route('/getData')
def getItems():
    emit('update values', items, room=session["room"])

@app.route('/')
def index2():
    start_transaction()
    #return render_template('user.html')

@app.route('/start-transaction', methods=['GET', 'POST'])
def start_transaction():
    return render_template('merchant.html')

@app.route("/user")
def user():
    return render_template('user/user.html', items = items)

@app.route("/retailer")
def retailer():
    return render_template('retailer/merchant.html', items = items)

#--START basic room events
@socketio.on('/join/<roomId>')
def join(roomId):
    join_room(roomId)
    getItems()
    return socketio

@socketio.on('left')
def left():
    room = session.get('room')
    leave_room(room)
    session.clear()
#--END basic room events



#--START create and send session
@app.route("/createid/<retailerId>/<orderId>", methods=['GET'])
def dealSession(retailerId, orderId):
    orderItems = request.args.get("orderItems") 
    sessionObj[0] = retailerId + orderId
    for elem in orderItems:
        sessionObj[1].append(elem)
    return json.dumps(sessionObj)
#--END create and send session

#--START update vals
@socketio.on('update values')
def changeVals(objectIndex, newOwner):
    sessionObj[1][objectIndex][0] = newOwner 
#--END update vales


# Getting an order given an order Id
@app.route('/getOrder', methods=['GET'])
def get_order():
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/find"

    payload = json.dumps({
      "enterpriseUnitId": "6df343ac26004ee29e027275a7173ed7"
    })
    headers = {
      'Content-Type': 'application/json',
      'nep-organization': 'test-drive-27b00b4089b94035b0db4',
      'nep-enterprise-unit': '6df343ac26004ee29e027275a7173ed7',
      'Date': 'Sun, 24 Oct 2021 00:15:36 GMT',
      'Authorization': 'Basic MTg2NGZmZDAtYmZjOC00OTg0LTk0NDEtM2Y1NDllNjFlM2M5Ok5pbW1pb21hcjFA'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)

if __name__ == '__main__':
    app.run(debug=True)


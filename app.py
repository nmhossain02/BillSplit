from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import json

#use request

app = Flask(__name__,
    static_url_path = '',
    static_folder = 'templates'
)
socketio = SocketIO(app)

#to be converted to a tuple before final send
#sessionObj = [sessionId, [[item1, p1], [item2, p2]]]
sessionObj = ["", []]



@app.route('/echo/<name>')
def index(name):
    return render_template('user.html', name="Hi " + name)

@app.route('/')
def index2():
    return "Welcome to Bill Splitter Web"

@app.route("/user")
def user():
    return render_template('user/user.html')

@app.route("/retailer")
def retailer():
    return render_template('retailer/merchant.html')

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


### NCR CRUD

# Creating an Order
app.route('/create<')
def createOrder():
        url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/09712019199806283404?order-id=ruben-identification"

        payload={}
        headers = {
          'Authorization': 'AccessKey ad0f88484ff34deaba4463238fc3de58:9p6E2gF6QIfP2dHGKMkN62XA9uXW564igLnnmJXWDkfN/mfKANSxxF3iMN8jwnKLpu1rSwwvwUptFKxbmezXHg==',
          'Content-Type': 'application/json',
          'nep-organization': 'test-drive-27b00b4089b94035b0db4',
          'nep-enterprise-unit': '6df343ac26004ee29e027275a7173ed7',
          'Date': 'Sat, 23 Oct 2021 17:22:37 GMT'
        }

        response = request.request("GET", url, headers=headers, data=payload)

        print(response.text)

if __name__ == '__main__':
    socketio.run(app)

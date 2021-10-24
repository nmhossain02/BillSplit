// join session
// retrieve current data (data = item array)
// click on an item => update data => send updated data
// retrieve and edit until consensus is reached
let items = [];
let id = ''

let thisOwner = {
    index: -1,
    name: "",
    color: "gray"
}

const defaultOwner = {
    index: -1,
    name: "",
    color: "gray"
}


SendData = () => {
    params = JSON.parse(thisOwner)
    fetch('/user/update/1234', {
        method: "POST",
        body: params,
        redirect: "follow"
    })
    //post request here
}

let first = true;
function RetrieveData() {
    print("fetch start")
    let response = fetch('https://127.0.0.1:5000/fetch/1234');
    var data = response.json();
    items = data
    print(items)
    $("#display-purchased-items").empty()
    items.forEach(item => {
        CreateItem(item)
    })
    setTimeout(RetrieveData, 4000);
}

RetrieveData()


CreateItems = ({ index, name, price, quantity, owner }) => {
    $("#display-purchased-items").append(`
        <div class="item-${item.index}">
            <button onclick="UpdateItem(${item.index})" class="item-button" style="background-color: ${item.owner.color}">
                ${item.name}, x${item.quantity}, ${item.price}, ${item.owner.name}
            </button>
        </div>
    `);
}

UpdateItem = (index) => {
    let item = items.filter(_item => _item.index === index)
    if (item.owner == defaultOwner) item.owner = thisOwner
    else if (item.owner == thisOwner) item.owner = defaultOwner
    SendData()
}


{/* <div className="item">
    
</div> */}

// update element

// join session
// retrieve current data (data = item array)
// click on an item => update data => send updated data
// retrieve and edit until consensus is reached


let items = [];

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

$(() => {
    let roomId
    $("#connect").click(() => {
        roomId = $("#search-bar").val()
    })
    fetch('http://' + document.domain + ':' + location.port + '/join/' + roomId).then((sock) => {socket = sock})
    RetrieveData()
    console.log(items)
})

SendData = () => {
    socket.emit("update values", items)
}

let first = true;
RetrieveData = () => {
    socket.on("update values", (items) => {items = items})
    $("#display-purchased-items").empty()
    items.forEach(item => {
        CreateItem(item)
    })
}

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

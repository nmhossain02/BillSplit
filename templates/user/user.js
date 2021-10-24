$(() => {
    var socket;
    socket = io.connect("https://" + document.domain + ':' + location.port + "/user")
    
    //passes itemsClone as pro
    socket.on('connect', function() {
        socket.emit('join', {});
        items = item
    });
        
    //passes ownerIndex, newOwner as prop
    socket.on('update values', (items) => {
        items = items
    })
                      
    let personObj = ["Alex Henly", "red"];
    let items = {}
    $("#connect").on("click", () => {
        // display items
        let root = $("#display-purchased-items")
        items.forEach((item, index) => {
            root.append(
                `<div class="item">
                    <button class="item-button" style="background-color: ${item.color}">
                    ${item.name}, x${item.quantity}, ${item.price}
                    </button>
                </div>`
            )
            $(".item-button").on("click", () => {
                if (typeof item.color === "undefined" ||
                    item.color === "white") item.color = "green"
                else if (item.color === "green") item.color = "white"
            })
        })
    })

    AddEachItem = (name, price, owner ) => {
        $("display-purchased-list").append(
            //someone write the front end 
        )

    }

})

// join session
// retrieve current data (data = item array)
// click on an item => update data => send updated data
// retrieve and edit until consensus is reached
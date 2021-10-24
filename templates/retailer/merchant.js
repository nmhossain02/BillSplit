

$(() => {
    let roomId = "abc123"
    let index = 0
    let totalPrice = 0.0
    $("button.add").on("click", () => {
        CreateItem(
            $("#new-item-name").val(), 
            $("#new-item-price").val(), 
            $("#new-item-q").val(), 
            index
        )
        index++
    })
    $("button.del").on("click", () => {
        console.log("click")
    })
    $(".pay").on("click", () => {
        let output = []
        let items = $(".item-list").children()
        // items.css("color", "red")
        let index = 0
        items.each(function() {
            output.push({
                index: index,
                name: $(this).children("#item-name").val(),
                price: $(this).children("#item-price").val(),
                quantity: $(this).children("#item-q").val(),
                owner: ""
            })
            index++
        })
        let data = {
            items: output
        }
        fetch("/merchant/process", {
            method: "POST",
            body: JSON.stringify(data),
            redirect: "follow"
        })
        .then(function(res){ 
            // console.log(res)
            window.location.href = `/merchant/pending/35642`
        })
    })

    RemoveHandler = (e) => {
        $(e.target).parent().remove()
        CalTotalPrice()
    }

    CalTotalPrice = () => {
        let items = $(".item-list").children()
        totalPrice = 0.0
        items.each(function() {
            totalPrice += parseFloat($(this).children("#item-price").val())
        })
        $(".total-price").html("<b>Total Price:</b> $" + totalPrice)
    }

    CreateItem = (name, price, quantity, index) => {
        $(".item-list").append(
            `<div class="item-${index} my-5">
                <input class="w-3/12 m-2 p-3 rounded" type="text" name="item-name" id="item-name"  value="${name}">
                <input class="w-1/12 m-2 p-3 rounded" type="number" name="item-q" id="item-q"  max="99" min="1" value="${quantity}">
                <input class="w-1/12 m-2 p-3 rounded" type="number" name="item-price" id="item-price"  max="10000.0" min="0.0" step = "0.01" value="${price}">
                <button type="submit" class="remove transition-all rounded text-gray bg-red-600 hover:bg-red-800 hover:text-white font-bold hover:font-black p-3">
                    Remove Item
                </button>
            </div>`
        )
        CalTotalPrice()
        //update totalPrice when an item is deleted

        $(`.item-${index} button.remove`).on("click", RemoveHandler)
    }
   
}) 
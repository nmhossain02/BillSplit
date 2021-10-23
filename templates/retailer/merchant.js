$(() => {
    let index = 0
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
        items.each(function() {
            output.push({
                name: $(this).children("#item-name").val(),
                price: $(this).children("#item-price").val(),
                quantity: $(this).children("#item-q").val()
            })
        })
        console.log(output)
    })
})

RemoveHandler = (e) => {
    $(e.target).parent().remove()
}

CreateItem = (name, price, quantity, index) => {
    $(".item-list").append(
        `<div class="item-${index}">
            <input type="text" name="item-name" id="item-name"  value="${name}">
            <input type="number" name="item-q" id="item-q"  max="99" min="1" value="${quantity}">
            <input type="number" name="item-price" id="item-price"  max="10000.0" min="0.0" step = "0.01" value="${price}">
            <button type="submit" class="remove">
                Remove Item
            </button>
        </div>`
    )
    $(`.item-${index} button.remove`).on("click", RemoveHandler)
}
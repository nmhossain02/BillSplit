//returns a HTML
function eachItem(index, { name, color }, price) {
    let index = index
    let element = $(`<button style="color: ${color} onClick="clickItem(index)">
        <p> ${name}, ${price} </p>
    </button>`) 
    element.data("index", index)
    return element
} 

function clickItem(index) {
    // make request to update purchases to 
    return index
}
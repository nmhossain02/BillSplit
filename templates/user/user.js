//method that gets session ID from user.html and passes it to session.html
function getSessionID() {
    let sessionID = document.getElementById("search-bar").value
    //pass the session id to session.html
}


//method that displays purchased items => write a for loop that iterates over the list 
//and renders it onto the webpage as buttons, along with an option to select and deselect
function displayItems(items) {

    Vue.component('display-items', {

        data: function() {
            for (let i = 0; i < items.length; i++) {
                var _name = JSON.stringify(items[i].name)
                var _q = JSON.stringify(items[i].q)
                var _price = JSON.stringify(items[i].price)
                //access items.name, items.q, items.price
                return {
                    name: _name,
                    q: _q,
                    price: _price,
                    color: red
                }
            }
        },

        template: `
            <div>
                <button style="background-color:{{color}}" v-on:click ="color = green">  {{ name }}, x{{q}}, {{price}} </button>
            </div>
        `
    })

    new Vue({ el: '#display-purchased-items' })

}
const url = window.location.origin
console.log(url)
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (recipe) => {
    $.ajax({
        type: 'POST',
        url: '/search_recipe_list/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'recipe': recipe
        },
        success: (res)=> {
            console.log(res)
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.innerHTML = ""
                console.log(url)
                data.forEach(recipe=> {
                    resultsBox.innerHTML += `
                        <a href="${url}/recipe_list/${recipe.pk}" class="item">
                        
                            <div class="row mt-2 mb-2">
                                <div class="col-10 results">
                                <p>${recipe.title} $${recipe.price}</p>
                                </div>
                            </div>
                        
                        </a>
                    `
                })
            } else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=> {
    console.log(e.target.value)

    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})

const table = document.getElementById('menuItems')
var sumValue = 0
for (var i=0; i < table.rows.length; i++) {
    sumValue = sumValue + parseFloat(table.rows[i].cells[1].innerHTML);
}

document.getElementById('totalPrice').innerHTML = "$" + parseFloat(sumValue).toFixed(2);

let moneyCell = Array.prototype.slice.call(document.querySelectorAll(".currency"));
moneyCell.forEach(function(cell){
    cell.textContext = (+cell.textContext).toLocaleString('en-US', {style: 'currency', currency: 'USD'});
});

$('.carousel').carousel({
    interval: 100
  })
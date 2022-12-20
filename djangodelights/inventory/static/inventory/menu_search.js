const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (recipe) => {
    $.ajax({
        type: 'POST',
        url: 'search_recipe_list/',
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
                        <a href="${url.slice(0, -9)}recipe_list/${recipe.pk}" class="item">
                        
                            <div class="row mt-2 mb-2">
                                <div class="col-10 results">
                                <h5>${recipe.title}</h5> $${recipe.price}
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
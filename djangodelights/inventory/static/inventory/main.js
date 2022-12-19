const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (menuItem) => {
    $.ajax({
        type: 'POST',
        url: 'search_purchases/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'menuItem': menuItem
        },
        success: (res)=> {
            console.log(res)
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.innerHTML = ""
                data.forEach(menuItem=> {
                    resultsBox.innerHTML += `
                        <a href="#" class="item">
                            <div class="row mt-2 mb-2">
                                <div class="col-10 results">
                                <h5>${menuItem.title}</h5> $${menuItem.price}: ${menuItem.date}
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
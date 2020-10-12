const token = 'bsngj7nrh5r9m81e0chg'

document.addEventListener('DOMContentLoaded', () => {

    // Use menu links to toggle sections
    document.querySelector('#search-link').addEventListener('click', () => load_section('search-section'));
    document.querySelector('#dashboard-link').addEventListener('click', () => load_section('dashboard-section'));
    document.querySelector('#transactions-link').addEventListener('click', () => load_section('transactions-section'));
    
    // Update balance
    document.querySelector('#refresh').addEventListener('click', balance_update);

    // Load search section by default
    load_section('search-section');
    document.querySelector('#search-btn').addEventListener('click', search_stock);
});
   
function load_section(section) {
    balance_update();

    // Hide all sections
    document.querySelector('#search-section').style.display = 'none';
    document.querySelector('#dashboard-section').style.display = 'none';
    document.querySelector('#transactions-section').style.display = 'none';

    // Show desired section
    document.querySelector(`#${section}`).style.display = 'block';

    // Update sections when shown
    // if secttion == dash , if sections == tran

}

function search_stock() {
    let symbol = document.querySelector('#search-input').value.toUpperCase();
    const invalid = document.querySelector('.invalid-search');
    const valid = document.querySelectorAll('.valid-search');
    fetch(`https://finnhub.io/api/v1/stock/profile2?symbol=${symbol}&token=${token}`)
    .then(res => res.json())
    .then(data => {

        if (data.name) {
            invalid.style.display = 'none'
            document.querySelector('#symbol-heading').innerHTML = symbol;
            document.querySelector('#company-heading').innerHTML = data.name;

            // Show results
            valid.forEach (element => {
                element.style.display = 'block';
            })

        } else {
            invalid.style.display = 'block';
            
            valid.forEach (element => {
                element.style.display = 'none';
            })
        }
    })
}

async function stock_price(symbol) {
    symbol = symbol.toUpperCase()
    let response = await fetch(`https://finnhub.io/api/v1/quote?symbol=${symbol}&token=${token}`);
    let data = await response.json()
    return data.c
}

function balance_update() {
    fetch('/api/stocks')
    .then(response => response.json())
    .then(stocks => {
        total_investing(stocks)
        .then(totals => {
            let investingTotal = 0;
            setTimeout(() => {
                totals.forEach(element => {
                    investingTotal += element;
                });
                // update both updatefunds and update investing in views to post request.
                // update investing amount with api
            }, 500);
            
            // request user details and update funds and investing on screen with that
            

        });
    })
}

async function total_investing(stocks) {
    // List of stocks symbols as input

    let totals = [];
    stocks.forEach(async element => {
        let price = await stock_price(element.symbol);
        let total = price * element.quantity;
        totals.push(total);
    });
    return totals
}

function formatNumber(num) {
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}
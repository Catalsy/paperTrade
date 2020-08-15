const token = 'bsngj7nrh5r9m81e0chg'

document.addEventListener('DOMContentLoaded', () => {

    // Use menu links to toggle sections
    document.querySelector('#search-link').addEventListener('click', () => load_section('search-section'));
    document.querySelector('#dashboard-link').addEventListener('click', () => load_section('dashboard-section'));
    document.querySelector('#transactions-link').addEventListener('click', () => load_section('transactions-section'));
    
    // Load search section by default
    load_section('search-section');
    document.querySelector('#search-btn').addEventListener('click', search_stock);
});
   
function load_section(section) {
    
    // Hide all sections
    document.querySelector('#search-section').style.display = 'none';
    document.querySelector('#dashboard-section').style.display = 'none';
    document.querySelector('#transactions-section').style.display = 'none';

    // Show desired section
    document.querySelector(`#${section}`).style.display = 'block';

    // Update sections when shown
    // Update balance when changing sections
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
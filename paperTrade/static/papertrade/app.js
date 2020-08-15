document.addEventListener('DOMContentLoaded', () => {

    // Use menu links to toggle sections
    document.querySelector('#search-link').addEventListener('click', () => load_section('search-section'));
    document.querySelector('#dashboard-link').addEventListener('click', () => load_section('dashboard-section'));
    document.querySelector('#transactions-link').addEventListener('click', () => load_section('transactions-section'));
    
    // Load search section by default
    load_section('search-section')


    


});
   
function load_section(section) {
    
    // Hide all sections
    document.querySelector('#search-section').style.display = 'none';
    document.querySelector('#dashboard-section').style.display = 'none';
    document.querySelector('#transactions-section').style.display = 'none';

    // Show desired section
    document.querySelector(`#${section}`).style.display = 'block';

    // Update sections when shown
    // if secttion == dash , if sections == tran

}

// APIs Quote and company Profile2
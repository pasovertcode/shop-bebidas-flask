/*!
* Start Bootstrap - Simple Sidebar v6.0.3 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 


var table = new DataTable('#dataTableProduct', {
    // options
});
$('#dataTableProduct tbody').on( 'click', 'tr', function () {
    console.log( table.row( this ).data() );
    var datarow = table.row( this ).data();
    datarow[0] = 100;
    table.row(this).data(datarow).draw();
} );


window.addEventListener('DOMContentLoaded', event => {
    
    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    const a_user = document.body.querySelector('#form-user');
    const a_product = document.body.querySelector('#form-product');
    const form_user = document.body.querySelector('#user-control-form');
    const form_product = document.body.querySelector('#product-control-form');
    if (a_user)
    {
        a_user.addEventListener('click', event => {
            event.preventDefault();
            form_product.style.display = "none";
            form_user.style.display = "block";

        });
    }
    if (a_product)
    {
        a_product.addEventListener('click', event => {
            event.preventDefault();
            form_user.style.display = "none";
            form_product.style.display = "block";
        });

    }


});






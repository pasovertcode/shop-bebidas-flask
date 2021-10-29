/*!
* Start Bootstrap - Simple Sidebar v6.0.3 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 





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
    const a_users = document.body.querySelector('#form-users');

    const form_users = document.body.querySelector('#users-control-form');
    const form_user = document.body.querySelector('#user-control-form');
    const form_product = document.body.querySelector('#product-control-form');
    if (a_user)
    {
        a_user.addEventListener('click', event => {
            event.preventDefault();
            if (a_product) form_product.style.display = "none";
            if (a_users) form_users.style.display = "none";
            form_user.style.display = "block";
            
        });
    }
    if (a_product)
    {
        a_product.addEventListener('click', event => {
            event.preventDefault();
            
            form_user.style.display = "none";
            if (a_users) form_users.style.display = "none";
            form_product.style.display = "block";
        });
        
        var product_table = new DataTable('#dataTableProduct', {
            // options
        });
        $('#dataTableProduct tbody').on( 'click', 'tr', function () {
            console.log( product_table.row( this ).data() );    
            var datarow = product_table.row( this ).data();
            $('#product-id').val(datarow[0]);
            $('#product-name').val(datarow[1]);
            $('#product-code').val(datarow[2]);
            $('#product-info').val(datarow[3]);
            $('#product-price').val(datarow[4]);
            if (datarow[5] == 'active')
            {
                $("#modal-form-select option[value='active']").attr('selected', true);
            }
            else
            {
                $("#modal-form-select option[value='deactive']").attr('selected', true);
            }
            
            $('#exampleModal').modal('show');
            
        } );
    }
    
    if (a_users)
    {
        
        a_users.addEventListener('click', event => {
        event.preventDefault();
        
        form_user.style.display = "none";
        form_users.style.display = "block";
        form_product.style.display = "none";
    });
    
    var user_table = new DataTable('#dataTableUsers', {
        // options
    });
    
    $('#dataTableUsers tbody').on( 'click', 'tr', function () {
        var datarow = user_table.row( this ).data();
        $('#user-name').val(datarow[2]);
        if (datarow[4] == 'activo')
        {
            $("#user-state option[value='active']").attr('selected', true);
        }
        else
        {
            $("#user-state option[value='deactive']").attr('selected', true);
        }
        $('#user-email').val(datarow[5]);
        if (datarow[1] == '0'){
            $("#user-type option[value='0']").attr('selected', true);
        } else if (datarow[1] == '1'){
            $("#user-type option[value='1']").attr('selected', true);
        } else{
            $("#user-type option[value='2']").attr('selected', true);
        }
        $('#UserModal').modal('show');
        
    });
}


});






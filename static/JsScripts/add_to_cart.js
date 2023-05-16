function add_to_cart(pk, quantity){
    
    let int_pk = parseInt(pk)
    let int_quantity = parseInt(quantity)
    
    $.ajax({
        
        url: '/add_to_cart/',
        data: { 'pk': int_pk, 'quantity': int_quantity },
        success: function (data){
            console.log('added');
        }
        
    })
    
}
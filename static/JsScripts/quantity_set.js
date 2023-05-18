function set_quantity(pk, quantity){
    
    let int_pk = parseInt(pk);
    let int_quantity = parseInt(quantity);
    
    $.ajax({
        url: '/change_quantity/',
        data: {'pk': pk, 'quantity': int_quantity},
        success: function(data){
        }
    })
    
}
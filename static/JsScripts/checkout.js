function checkout(){

    $.ajax({

        url: '/checkout/',
        data: {},
        success: function(data){
            console.log(data.message);
        }

    })

}
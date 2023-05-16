function wishlist(self, pk){
    
    $.ajax({
        url: '/wishlist/',
        data: {'pk':parseInt(pk)},
        success: function(data){
           
            if( data.status ){
                self.style.color = 'red';
            }
            else{
                self.style.color = 'black';
            }
        }
    })
    
}
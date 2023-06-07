
function add_to_cart(pk, quantity){
    
    let int_pk = parseInt(pk)
    let int_quantity = parseInt(quantity)
    
    $.ajax({
        
        url: '/add_to_cart/',
        data: { 'pk': int_pk, 'quantity': int_quantity },
        
        success: function (data){

            let main_container = document.querySelector('body');

            let added_notification = `<div class="notification">
            <i style="color: #2196f3" class="fa-solid fa-cart-arrow-down"></i>
            <p>لقد تم اضافة المنتج لسلتك</p>
            </div>`;

            main_container.innerHTML += added_notification;
            let notification_boxes = document.querySelectorAll('.notification');

            notification_boxes.forEach(function(notification_box){

                setTimeout(function(){

                    notification_box.style.top = '-10%';

                    }, 1000)

                setTimeout(function(){

                    notification_box.remove()

                }, 2000)
            })

        },
        
    })
    
}
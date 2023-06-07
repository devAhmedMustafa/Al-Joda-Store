$('#id_email').change( function(){
    var email = $(this).val();

    $.ajax({
        url:'/ajax/user_validate/', 
        data:{
            'email':email
        },
        dataType: 'json', 
        success: function(data){

            email_field = document.querySelector('#id_email');

            if (data.is_taken){

                register = document.querySelector('#register');

                email_field.style.borderColor = 'rgb(192, 0, 0)';

                register.setAttribute('disabled', 'true');

            }
            else{

                email_field.style.borderColor = 'navajowhite';
                register.removeAttribute('disabled');

            }
        }
    });
} )
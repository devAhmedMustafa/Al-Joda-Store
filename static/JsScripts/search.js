$("#search").change(function(){

    var val = $(this).val();

    $.ajax({

        url: '/search/',
        type: 'GET',
        data: {'search_value': val},
        success: function(data){

            products = JSON.parse(data.products)

            const content = document.querySelector('.content')
            
            content.innerHTML = `<div class="page">
            
            <div class="p-container"></div></div>`;
        
            for ( let i = 0; i < products.length; i++ )
            {

                url =  `../../media/${products[i].image}`;

                console.log(products[i])
                products_container = document.querySelector('.p-container');
                products_container.innerHTML += `<a href="{% url '' ${products[i].slug}" %}>  <div class="box">
                <img decoding="async" src="${url}" alt="" />
                <div class="p-content">
                  <h3>${products[i].name}</h3>
                  <p>
                    ${products[i].description}
                  </p>
                </div>
                <button class="info" onclick="add_to_cart(${products[i].pk}, 1)">
                  <a href="">Add cart</a>
                  <i class="fa-solid fa-plus"></i>
                </button>
              </div> </a>`
            }
            
        }

    })

})
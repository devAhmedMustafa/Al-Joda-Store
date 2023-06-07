products = document.querySelectorAll('.box');


function uptoPrice(price) {
    
    products.forEach((product) => {

        let productPrice = product.querySelector('.price').innerText;
        productPrice = parseFloat(productPrice.replace('EGP', ''));
        
        if (productPrice > price) {
            product.style.display = 'none';
        }
        else {
            product.style.display = 'block';
        }

    });

};

function fromPrice(price) {
        
        products.forEach((product) => {
    
            let productPrice = product.querySelector('.price').innerText;
            productPrice = parseFloat(productPrice.replace('EGP', ''));
            
            if (productPrice < price) {
                product.style.display = 'none';
            }
            else {
                product.style.display = 'block';
            }
    
        });
    
}
$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var price = submit_btn.data("price") // data-атрибуты добавляем в product.html 
        console.log(product_id);
        console.log(name);
    })

    $('.basket-container').on('click', function(e){
    	e.preventDefault();
    	$('.basket-items').removeClass('hidden');
    })

    $('.basket-container').mouseover(function(){
    	$('.basket-items').removeClass('hidden');
    })

    $('.basket-container').mouseout(function(){
    	$('.basket-items').addClass('hidden');
    })

});
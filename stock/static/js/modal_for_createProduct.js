$(function(){
   
    $('.new_supplier_items').hide()
    $('.form').submit(function(e){
        e.preventDefault();
      
    })
    $('#new_supplier').click(function(){
        $('.new_supplier_items').show()
       
    })
  
    
})

    
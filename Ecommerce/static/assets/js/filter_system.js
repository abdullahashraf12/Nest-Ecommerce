$(document).ready(function(){
    var elements = $('[name="product_card"]');
    var checkboxes = $('input[name="checkbox_categ"]');
    var numberOfShownItems = 0;
    
    checkboxes.change(function(){
        var checkedIds_categs = [];
        numberOfShownItems = 0; // Reset the count
        
        checkboxes.each(function(){
            if ($(this).is(':checked')) {
                checkedIds_categs.push($(this).attr('id'));
            }
        });
        
        if (checkedIds_categs.length === 0) {
            elements.show(); // Show all products if no checkboxes are checked
            numberOfShownItems = elements.length; // Update count
        } else {
            elements.hide(); // Hide all products by default when checkboxes are checked
            elements.each(function(){
                var categIdValue = $(this).data('categ_id'); 
                if (checkedIds_categs.includes(categIdValue)) {
                    $(this).show(); // Show products corresponding to checked categories
                    numberOfShownItems++; // Increment count
                }
            });
        }
        console.log("Number of shown items: " + numberOfShownItems);
        $("#number_of_all_showed_products").html(numberOfShownItems)

    });
});

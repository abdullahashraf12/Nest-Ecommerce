document.addEventListener('DOMContentLoaded', function() {
    // Find all elements with the name attribute set to "change_me_changed_qty"
    var elements = document.querySelectorAll('h4[name="change_me_changed_qty"]');

    // Iterate over each element
    elements.forEach(function(element) {
        // Find the closest parent element containing the quantity input
        var parent = element.closest('.pt-30').querySelector('.qty-val');
        
        // Check if the parent element is found before attaching the event listener
        if (parent) {
            // Add an event listener to the input to detect changes
            parent.addEventListener('input', function() {
                // Update the content of the h4 element with the new quantity multiplied by the price
                var quantity = parseInt(this.value);
                var priceElement = element.parentElement.nextElementSibling.querySelector('.text-body');
                if (priceElement) {
                    var price = parseFloat(priceElement.textContent.replace('$', ''));
                    var totalPrice = quantity * price;
                    element.textContent = '$' + totalPrice.toFixed(2);
                } else {
                    console.error('Price element not found.');
                }
            });
        } else {
            console.error('Parent element not found.');
        }
    });
});

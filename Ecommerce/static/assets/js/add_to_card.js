$(document).ready(function() {
    var email = $("#email_exist").val(); // Function to get the CSRF token from the cookie

    $("#prod_ven").on("click", function(event) {

        event.preventDefault(); // Prevent the default behavior of the button click event

        if (!email || !email.trim() || !email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
            {
                alert("You Cannot Add To Card Please LogIn First");
            }
        } else {

            var csrftoken = getCookie('csrftoken');
            // Get the list of options
            var sizeList = document.querySelector('.size-filter');

            // Find the active option
            var activeOption = sizeList.querySelector('li.active');

            // Get the text content of the active option
            var activatedOption = activeOption.querySelector('a').textContent;

            // Log the activated option
            console.log("Activated option:", activatedOption);
            $.ajax({
                url: "/add_to_card/", // Make sure the URL is correct
                method: "POST", // Specify the request method
                data: {
                    pid: $('[name="product_pid_to_card"]').val(),
                    qty: $('[name="prod_quantity_n"]').val(),
                    size:activatedOption
                },
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken); // Set the CSRF token in the request header
                    console.log("Adding Products to Card")
                },
                success: function(response2) {
          console.log("product added or modified")






                    // $.ajax({
                    //     url: "/add_to_card/", // Make sure the URL is correct
                    //     method: "GET", // Specify the request method
                    //     data: {}, // You can pass any data here if needed
                    //     dataType: 'json',
                    //     beforeSend: function(xhr) {
                    //         // Code to run before the request is sent
                    //     },
                    //     success: function(response2) {
                    //         // Code to run if the request succeeds
                    //         var userOrderCards = JSON.parse(response2.prod_card);
                    //         $("#Shopping_card").empty();

                    //         for (var i = 0; i < userOrderCards.length; i++) {
                    //             var userOrderCard = userOrderCards[i];
                    //             console.log(userOrderCard)
                    //             console.log(userOrderCard.uoc_prod__image.url)
                    //             // Create the HTML for the li tag
                    //             var liHtml = '<li>' +
                    //             '<div class="shopping-cart-img">' +
                    //             '<a href="/get_products/' + userOrderCard.uoc_prod__pid + '"><img alt="Nest" src="/media/' + userOrderCard.uoc_prod__image + '" /></a>' +
                    //             '</div>' +
                    //             '<div class="shopping-cart-title">' +
                    //             '<h4><a href="/get_products/' + userOrderCard.uoc_prod__pid + '">' + userOrderCard.uoc_prod__title + '</a></h4>' +
                    //             '<h4><span>' + userOrderCard.qty + ' × </span>' + userOrderCard.weight + '</h4>' +
                    //             '</div>' +
                    //             '<div class="shopping-cart-delete">' +
                    //             '<form class="delete-form" data-pid="' + userOrderCard.uoc_prod__pid + '">' +
                    //             '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrftoken + '">' +
        
                    //             '<button type="submit" style="background-color: red; ' +
                    //             'border: 1px solid red; ' +
                    //             'color: #fff; ' +
                    //             'padding: 10px 20px; ' +
                    //             'font-size: 16px; ' +
                    //             'cursor: pointer; ' +
                    //             'border-radius: 4px; ' +
                    //             'transition: background-color 0.3s ease;">X</button>' +
        
                    //             '</form>' +
                    //             '</div>' +
                    //             '</li>';
                    //             // Append the liHtml to the ul element with ID "Shopping_card"
                    //             $('#Shopping_card').append(liHtml);
                    //         }
                    //     },
                    //     error: function(xhr, textStatus, errorThrown) {
                    //         // Code to run if the request fails
                    //         // Log the specific error message from the response
                    //         if (xhr.responseText) {
                    //             alert(xhr.responseText); // Display the error message
                    //         } else {
                    //             console.error("Error:", textStatus, errorThrown);
                    //         }
                    //     }
                    // });
                    





                    
                    
                },
                error: function(xhr, textStatus, errorThrown) {
                    // console.error("Error:", textStatus, errorThrown);
                    var errorResponse = JSON.parse(xhr.responseText);
                    alert(errorResponse.error); // Log the specific error message
                               
                }
            });





        }
    });
});

// Function to retrieve CSRF token from the cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

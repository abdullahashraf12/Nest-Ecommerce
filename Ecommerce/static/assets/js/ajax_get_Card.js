function myFunction() {
    $.ajax({
        url: "/add_to_card/",
        method: "GET",
        data: {},
        dataType: 'json',
        beforeSend: function(xhr) {
            // Code to run before the request is sent
        },
        success: function(response2) {
            try {
                var userOrderCards = JSON.parse(response2.prod_card);
                $("#Shopping_card").empty();
                $("#number_of_products_in_card").html(userOrderCards.length);
                for (var i = 0; i < userOrderCards.length; i++) {
                    var userOrderCard = userOrderCards[i];
                    console.log(userOrderCard);
                    console.log(userOrderCard.uoc_prod__image.url);
                    var liHtml = '<li>' +
                        '<div class="shopping-cart-img">' +
                        '<a href="shop-product-right.html"><img alt="Nest" src="/media/' + userOrderCard.uoc_prod__image + '" /></a>' +
                        '</div>' +
                        '<div class="shopping-cart-title">' +
                        '<h4><a href="/get_products/' + userOrderCard.uoc_prod__pid + '">' + userOrderCard.uoc_prod__title + '</a></h4>' +
                        '<h4><span>' + userOrderCard.qty + ' × </span>' + userOrderCard.weight + '</h4>' +
                        '</div>' +
                        '<div class="shopping-cart-delete">' +
                        '<a href="#"><i class="fi-rs-cross-small"></i></a>' +
                        '</div>' +
                        '</li>';
                    $('#Shopping_card').append(liHtml);
                }
            } catch (error) {
                console.error("Error parsing response:", error);
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error("Error:", textStatus, errorThrown);
            if (xhr.responseText) {
                alert(xhr.responseText);
            }
        }
    });
}

setInterval(myFunction, 1000);

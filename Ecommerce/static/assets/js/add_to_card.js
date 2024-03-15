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

            $.ajax({
                url: "/add_to_card/", // Make sure the URL is correct
                method: "POST", // Specify the request method
                data: {
                    pid: $('[name="product_pid_to_card"]').val()
                },
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken); // Set the CSRF token in the request header
                    console.log("Adding Products to Card")
                },
                success: function(response) {
                    console.log(response)
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

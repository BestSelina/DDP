function showSearchResult(data) {
    var searchResult = document.getElementById('searchResult')
    var str = '';
    for (var i = 0; i < data.length; i++) {
        if (data[i][7] == null) {
            str += '<div class="col">' +
                '<div class="card bg-dark text-white">' +
                '<img src="' + data[i][3] + '"' + 'class="card-img-top" alt="Menu Item">' +
                '<div class="card-body">' +
                '<h5 class="card-title">' + data[i][1] + '</h5>' +
                '<p class="card-text">£' + data[i][6] + '</p>' +
                '</div>' +
                '</div>' +
                '</div>'
        }
        else {
            str += '<div class="col">' +
                '<div class="card bg-dark text-white">' +
                '<a href="' + data[i][7] + '">' +
                '<img src="' + data[i][3] + '"' + 'class="card-img-top" alt="Menu Item">' +
                '</a>' +
                '<div class="card-body">' +
                '<h5 class="card-title">' + data[i][1] + '</h5>' +
                '<p class="card-text">£' + data[i][6] + '</p>' +
                '</div>' +
                '</div>' +
                '</div>'
        }
    }
    searchResult.innerHTML = str;
}

function search(event) {
    event.preventDefault();
    var searchMenu = document.getElementById("searchMenu").value;
    console.log(searchMenu)
    $.ajax({
        type: "POST",
        url: "http://localhost:8899/goose",
        dataType: "json",
        data: JSON.stringify({
            searchInput: $("#searchMenu").val(),
        }),
        success: function (res) {
            console.log(res);
            if (res == '') {
                alert("cannot find any relevant food")
                window.location.href = "/templates/goose.html"
            }
            else {
                showSearchResult(res);
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function orderFishAndChips(event) {
    event.preventDefault();
    var quantity = document.getElementById("quantity").value;
    console.log("order " + quantity + " items successfully!")
    $.ajax({
        type: "POST",
        url: "http://localhost:8899/order",
        dataType: "json",
        data: JSON.stringify({
            quantity: $("#quantity").val(),
        }),
        success: function (msg) {
            console.log(msg);
            if (msg['status'] == 'success') {
                alert("your order id is " + msg['order_id'])
            }
            else {
                alert(msg['info'])
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function login(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://localhost:8899/login",
        dataType: "json",
        data: JSON.stringify({
            loginEmail: $("#loginEmail").val(),
            loginPassword: $('#loginPass').val(),
        }),
        success: function (msg) {
            console.log(msg);
            if (msg['status'] == 'success') {
                window.location.href = "/templates/goose.html"
            }
            else {
                alert(msg['info'])
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function signup(event) {
    event.preventDefault();
    var password1 = document.getElementById("regPass1").value;
    var password2 = document.getElementById("regPass2").value;
    var email = document.getElementById("regEmail").value;
    if (email == "") {
        alert("email address cannot be empty!")
    }
    else if (password1 == "" || password2 == "") {
        alert("password cannot be empty!")
    }
    else {
        if (password1 != password2) {
            alert("The two passwords are not same. Please try again!")
        }
        else {
            $.ajax({
                type: "POST",
                url: "http://localhost:8899/signup",
                dataType: "json",
                data: JSON.stringify({
                    regEmail: $("#regEmail").val(),
                    regPassword: $('#regPass1').val(),
                }),
                success: function (msg) {
                    console.log(msg);
                    if (msg['status'] == 'success') {
                        window.location.href = "/templates/login.html"
                    }
                    else {
                        alert(msg['info'])
                    }
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    }
}

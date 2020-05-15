$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="SingleItem">
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span class="Caption">${ d.name }</span>
                                </a>
                                <p class="ItemPrice">${d.price}</p>
                                <div class="CartButton" id=${d.id}>
                                    <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
                                </div>
                            </div>`;
                });
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            }
        });
    });
});
$(document).on('click','.CartButton', function(e) {
    e.preventDefault();
    let cart_item_id = e.target.parentElement.id;
    let cart_id = "some_cart_key";
    let item_storage = localStorage.getItem(cart_id);
    $.ajax({
        url: '/cart/items',
        type: 'GET',
        success: function(resp) {
            let item_list = JSON.parse(resp);
            // find the cart item object from the list of items we got from the server
            let cart_item_object = item_list.find(function (item){
                return item.pk == cart_item_id;
            });
            //if the cart does not exist, then init cart and add item to it
            if (item_storage == null){
                item_storage = [];
                cart_item_object.fields.quantity = 1;
                item_storage.push(cart_item_object);
                item_storage = JSON.stringify(item_storage);
                localStorage.setItem(cart_id, item_storage);
            }
            else{
                item_storage = JSON.parse(item_storage);
                let not_in_storage = true;
                let i;
                for (i = 0; i < item_storage.length; i++) {
                    if (item_storage[i].pk == cart_item_object.pk){
                        let new_item_object = item_storage[i];
                        new_item_object.fields.quantity++;
                        not_in_storage = false;
                        item_storage.splice(i, 1, new_item_object);
                        item_storage = JSON.stringify(item_storage);
                        localStorage.setItem(cart_id, item_storage);
                    }
                }

                // if the cart exists and the item is not in the cart, then create instance in cart
                if (not_in_storage === true){
                    cart_item_object.fields.quantity = 1;
                    item_storage.push(cart_item_object);
                    item_storage = JSON.stringify(item_storage);
                    localStorage.setItem(cart_id, item_storage);
                }
                alert("item added to cart");
            }
        }
    });
});

$(document).on('click','.increase_amount_button', function(e) {
    let item_id = e.target.parentElement.id;
    let cart_array = localStorage.getItem("some_cart_key");
    cart_array = JSON.parse(cart_array);

    let i;
    //find item in cart and increase amount if id match and then push back on local storage
    for (i = 0; i < cart_array.length; i++) {
        if (cart_array[i].pk == item_id){
            let new_item_object = cart_array[i];
            new_item_object.fields.quantity++;
            cart_array.splice(i, 1, new_item_object);
            cart_array = JSON.stringify(cart_array);
            localStorage.setItem("some_cart_key", cart_array);

        }
    }
    location.reload();
});

    $(document).on('click','.decrease_amount_button', function(e) {
        let item_id = e.target.parentElement.id;
        let cart_array = localStorage.getItem("some_cart_key");
        cart_array = JSON.parse(cart_array);
        let i;
        //find item in cart and decrease amount if id match and then push back on local storage
        for (i = 0; i < cart_array.length; i++) {
            if (cart_array[i].pk == item_id){
                let new_item_object = cart_array[i];
                new_item_object.fields.quantity--;
                if (new_item_object.fields.quantity === 0){
                    cart_array.splice(i, 1);
                    cart_array = JSON.stringify(cart_array);
                    localStorage.setItem("some_cart_key", cart_array);
                }
                else{
                    cart_array.splice(i, 1, new_item_object);
                    cart_array = JSON.stringify(cart_array);
                    localStorage.setItem("some_cart_key", cart_array);
                }
            }
        }
        location.reload();
    });

    $(document).on('click','.delete_item_button', function(e) {
        let item_id = e.target.parentElement.id;
        let cart_array = localStorage.getItem("some_cart_key");
        cart_array = JSON.parse(cart_array);
        let i;
        //find item in cart and decrease amount if id match and then push back on local storage
        for (i = 0; i < cart_array.length; i++) {
            if (cart_array[i].pk == item_id){
                cart_array.splice(i, 1);
                cart_array = JSON.stringify(cart_array);
                localStorage.setItem("some_cart_key", cart_array);

            }
        }
        location.reload();
    });

    $(document).ready(function() {
        let $filters = $('.FilterButtons [data-filter]'),
            $items = $('.items [item-category]');

        $filters.on('click', function(e) {
          e.preventDefault();
          let $this = $(this);

          $filters.removeClass('active');
          $this.addClass('active');

          let $filterCat = $this.attr('data-filter');

          if ($filterCat === 'all') {
            $items.removeClass('is-animated')

              .hide().promise().done(function() {
                $items.addClass('is-animated').fadeIn(50);
              });
          } else {
            $items.removeClass('is-animated')
              .fadeOut(50).promise().done(function() {
                $items.filter('[item-category = "' + $filterCat + '"]')
                  .addClass('is-animated').fadeIn(50);
              });
          }
        });
    });

$(document).ready(function() {
    // let search_filter = document.getElementById("search-box").value;
    let input = document.getElementById("search-box");
        if (input !== null){
    input.addEventListener("keyup", function (event) {
        if (event.which == 13) {
            event.preventDefault();
            document.getElementById("search-btn").click();
        }
        return false;});
    }
});

$(document).ready(function() {

    $('#namebtn').on('click', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/items?sort_filter=' + 'name',
            type: 'GET',
            success: function (resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="SingleItem">
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span class="Caption">${ d.name }</span>
                                </a>
                                <p class="ItemPrice">${d.price}</p>
                                <div class="CartButton" id=${d.id}>
                                    <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
                                </div>
                            </div>`;
                });
                $('.items').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });
});

$(document).ready(function() {

    $('#pricelhbtn').on('click', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/items?sort_filter=' + 'price',
            type: 'GET',
            success: function (resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="SingleItem">
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span class="Caption">${ d.name }</span>
                                </a>
                                <p class="ItemPrice">${d.price}</p>
                                <div class="CartButton" id=${d.id}>
                                    <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
                                </div>
                            </div>`;
                });
                $('.items').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });
});

$(document).ready(function() {

    $('#pricehlbtn').on('click', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/items?sort_filter=' + '-price',
            type: 'GET',
            success: function (resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="SingleItem">
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span class="Caption">${ d.name }</span>
                                </a>
                                <p class="ItemPrice">${d.price}</p>
                                <div class="CartButton" id=${d.id}>
                                    <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
                                </div>
                            </div>`;
                });
                $('.items').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });
});


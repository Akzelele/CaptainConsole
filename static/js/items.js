$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {

                    return `<div class="SingleItem" item-category = ${d.category}>
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span class="Caption">${ d.name }</span>
                                </a>
                                <p class="ItemPrice">${d.price}</p>
                                <div class="CartButton" id=${d.id}>
                                    <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
                                </div>
                            </div>`

                    //TODO:order by name
                })
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr,status,error) {
                console.error();
            }
        })
    });

    $(document).on('click','.CartButton', function(e) {
        e.preventDefault();
        var cart_item_id = e.target.parentElement.id
        var cart_id = "some_cart_key"
        var item_storage = localStorage.getItem(cart_id)
        $.ajax({
            url: '/cart/items',
            type: 'GET',
            success: function(resp) {
                var item_list = JSON.parse(resp);

                // find the cart item object from the list of items we got from the server
                var cart_item_object = item_list.find(function (item){
                    return item.pk == cart_item_id;
                })
                //if the cart does not exist, then init cart and add item to it
                if (item_storage === null){
                    item_storage = []
                    cart_item_object.fields.quantity = 1;
                    item_storage.push(cart_item_object)
                    item_storage = JSON.stringify(item_storage);
                    localStorage.setItem(cart_id, item_storage);
                }
                else{
                    item_storage = JSON.parse(item_storage);
                    var not_in_storage = true
                    var i;
                    for (i = 0; i < item_storage.length; i++) {
                        if (item_storage[i].pk == cart_item_object.pk){
                            var new_item_object = item_storage[i];
                            new_item_object.fields.quantity++;
                            not_in_storage = false
                            item_storage.splice(i, 1, new_item_object)
                            item_storage = JSON.stringify(item_storage);
                            localStorage.setItem(cart_id, item_storage);
                            }
                        }

                    // if the cart exists and the item is not in the cart, then create instance in cart
                    if (not_in_storage == true){
                        cart_item_object.fields.quantity = 1;
                        item_storage.push(cart_item_object)
                        item_storage = JSON.stringify(item_storage);
                        localStorage.setItem(cart_id, item_storage);
                        }
                    }

                alert("item added to cart")
            },
            error: function(xhr,status,error) {
                console.error();
            }
        })
    });


    $(document).ready(function(e) {
        var $filters = $('.FilterButtons [data-filter]'),
            $items = $('.items [item-category]');


        $filters.on('click', function(e) {
          e.preventDefault();
          var $this = $(this);

          $filters.removeClass('active');
          $this.addClass('active');

          var $filterColor = $this.attr('data-filter');

          if ($filterColor == 'all') {
            $items.removeClass('is-animated')

              .hide().promise().done(function() {
                $items.addClass('is-animated').fadeIn(50);
              });
          } else {
            $items.removeClass('is-animated')
              .fadeOut(50).promise().done(function() {
                $items.filter('[item-category = "' + $filterColor + '"]')
                  .addClass('is-animated').fadeIn(50);
              });
          }
        })(jQuery);
    });

});
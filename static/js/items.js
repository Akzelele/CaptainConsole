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

                    return `<div class="SingleItem">
                                <a href="/items/${d.id}">
                                    <img class="ItemImg" src="${d.firstImage}" alt="${d.name } image"/>
                                    <span id="Caption">${ d.name }</span>
                                </a>
                                <p id="ItemPrice">${d.price}</p>
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
        var item_storage = localStorage.getItem(cart_item_id)

        if (item_storage === null){
            localStorage.setItem(cart_item_id, 1)
        }
        else{
            item_storage++;
            localStorage.setItem(cart_item_id,item_storage)
        }
        alert("item added to cart")
    });

    $(document).on('click','#Cart', function(e) {
        e.preventDefault();
        var item_storage = Object.entries(localStorage)
        console.log(item_storage)
        console.log(item_storage)

        var i;
        for (i = 0; i<item_storage.length; i++){
            console.log(item_storage[i])
        }

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
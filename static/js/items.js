$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
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
                                <button type="button" id = "AddToCartButton" class="btn btn-outline-primary">Add to Cart</button>
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
});
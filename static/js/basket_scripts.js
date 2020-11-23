"use strict";

window.onload = function () {
    console.log("DOM ready");
    // $('.product_price').on('click', function (event) {
    //     console.log("target:", event.target)
    // })
    // $('.basket_record').on('click', '.category_name',
    //     function (event) {
    //         console.log("target:", event.target);
    //         // .val()
    //     })
    // let categoryNames = document.querySelectorAll('.category_name');
    let categoryNames = document.querySelectorAll('input[type=number]');
    categoryNames.forEach(function (item) {
        item.onchange = function (event) {
            let qty = event.target.value
            let pk = event.target.name
            console.log("qty:" + qty + ", pk " + pk);
            $.ajax({
                url:"/basket/set/" + pk + "/" + qty + "/",
                success: function (answer) {
                    console.log("answer", answer);
                    document.querySelector('.basket_list').innerHTML = answer.basket_list;
                }
            })
        }
    })
}

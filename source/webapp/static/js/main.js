function onCreateSuccess(response, status) {
    console.log(response);
    console.log(status);

    let newFoodLi = $('<li></li>');

    let foodNameSpan = $('<span></span>')
        .attr('id', 'order_food_name_' + response.pk)
        .data('food_pk', response.food_pk)
        .text(response.food_name);

    let foodAmountSpan = $('<span></span>')
        .attr('id', 'order_food_amount_' + response.pk)
        .text(response.amount);

    let editLink = $('<a></a>')
        .addClass('edit_link')
        .attr('href', response.edit_url)
        .data('pk', response.pk)
        .text('Изменить')
        .click(onOrderFoodUpdate);

    let deleteLink = $('<a></a>')
        .addClass('order_food_delete')
        .attr('href', response.delete_url)
        .data('pk', response.pk)
        .text('Удалить')
        .click(onOrderFoodDelete);

    newFoodLi
        .attr('id', 'order_food_' + response.pk)
        .append(foodNameSpan)
        .append(document.createTextNode(': '))
        .append(foodAmountSpan)
        .append(document.createTextNode('шт. ('))
        .append(editLink)
        .append(document.createTextNode('/'))
        .append(deleteLink)
        .append(document.createTextNode(')'));

    $('#order_food_list').append(newFoodLi);

    $('#food_edit_modal').modal('hide');
}


function onUpdateSuccess(response, status) {
    console.log(response);
    console.log(status);

    let pk = response['pk'];
    let food_name_span = $('#order_food_name_' + pk);
    food_name_span.text(response.food_name);
    food_name_span.data('food_pk', response.food_pk);
    $('#order_food_amount_' + pk).text(response.amount);

    $('#food_edit_modal').modal('hide');
}


function onFormSubmitError(response, status) {
    console.log(response);
    console.log(status);

    if (response.errors) {
        $('#food_form_errors').text(response.errors.toString());
    }
}


function orderFoodFormSubmit(success) {
    let url = $('#food_form').attr('action');

    let data = {
        food: $('#id_food').val(),
        amount: $('#id_amount').val(),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
    };

    $.ajax({
        url: url,
        method: 'POST',
        data: data,
        success: success,
        error: onFormSubmitError
    });
}


function onOrderFoodCreate(event) {
    event.preventDefault();

    $("#food_edit_modal .modal-title").text('Добавить блюдо');
    $("#food_submit").text('Добавить');

    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));

    $('#id_food').val('');
    $('#id_amount').val('');

    foodForm.off('submit');

    foodForm.on('submit', function (e) {
        e.preventDefault();

        orderFoodFormSubmit(onCreateSuccess);
    });

    $('#food_edit_modal').modal('show');
}


function onOrderFoodUpdate(event) {
    event.preventDefault();

    $("#food_edit_modal .modal-title").text('Изменить блюдо');
    $("#food_submit").text('Изменить');

    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));

    let foodPk = $(this).data('pk');
    let foodName = $('#order_food_name_' + foodPk);
    let foodAmount = $('#order_food_amount_' + foodPk);

    $('#id_food').val(foodName.data('food_pk'));
    $('#id_amount').val(foodAmount.text());

    foodForm.off('submit');

    foodForm.submit(function (event) {
        event.preventDefault();

        orderFoodFormSubmit(onUpdateSuccess);
    });

    $('#food_edit_modal').modal('show');
}

function onOrderFoodDelete() {
    event.preventDefault();
    let url = $(this).attr('href');

    $.ajax({
        url: url,
        method: 'get',
        success: function (response, status) {
            console.log(response);
            console.log(status);
            let del = document.getElementById('order_food_' + response.pk);
            del.remove();
        },

        error: function (response, status) {
            console.log(response);
            console.log(status);
        }
    });
}


window.addEventListener('load', function () {
    $('#food_submit').on('click', function (e) {
        $('#food_form').submit();
    });

    $("#order_food_add_link").click(onOrderFoodCreate);
    $('#order_food_list .edit_link').click(onOrderFoodUpdate);
    $('.order_food_delete').click(onOrderFoodDelete);
});
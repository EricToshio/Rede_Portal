$(function() {

    /* Functions */
    var updateColor = function() {
        var highlights = {
            "pendente": "red",
            "autorizado": "green",
        }
        $(".js-problem-card__status").each(function() {
            $(this).css("color", highlights[$(this).html()]);
        });
    };

    var positiveRequest = function() {
        var button = $(this);
        var url_t = "/redecasd/membros/reservas/autorizar/1".replace('1', button.attr("data-number"));
        $.ajax({
            url: url_t,
            dataType: 'json',
            success: function(data) {
                $("#reservation_request_list").html(data.html_reservation_list);
                updateColor();
            }
        });
        return false;
    };

    $("#reservation_request_list").on("click", ".js-reservation-positive", positiveRequest);

    updateColor();
});
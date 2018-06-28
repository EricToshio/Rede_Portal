var updateColor = function() {
    var highlights = {
        "Enviado": "red",
        "Em avaliação": "blue",
        "Resolvido": "green",
    }

    $(".js-problem-card__status").each(function() {
        $(this).css('color', highlights[$(this).html()]);
    });
};
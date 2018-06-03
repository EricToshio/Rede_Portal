var updateColor = function() {
    var highlights = {
        "enviado": "red",
        "avaliacao": "blue",
        "resolvido": "green",
    }

    $(".js-problem-card__status").each(function() {
        $(this).css('color', highlights[$(this).html()]);
    });
};
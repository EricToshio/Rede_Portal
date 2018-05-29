var highlights = {
    "Pendente": "status-color--red",
    "Em avaliação": "status-color--blue",
    "Resolvido": "status-color--green",
    }

    $(".js-problem-card__status").each(function() {
        $(this).addClass(highlights[$(this).html()]);
    });
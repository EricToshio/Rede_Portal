$(function() {


    var searchMember = function() {
        email = document.getElementById('js-search-user-email').value;
        var url_t = "/redecasd/membros/gerenciar-membros/pesquisar-usuario/1".replace('1', email);
        $.ajax({
            url: url_t,
            dataType: 'json',
            success: function(data) {
                $("#member_search_result").html(data.html_results);
            }
        });
        return false;
    };

    var removeMember = function() {
        var button = $(this);
        var url_t = "/redecasd/membros/gerenciar-membros/remover/1".replace('1', button.attr("data-number"));
        $.ajax({
            url: url_t,
            dataType: 'json',
            success: function(data) {
                $("#member_list").html(data.html_member_list);
            }
        });
        return false;
    };

    var addMember = function() {
        var input_field = document.getElementById('js-search-user-email');
        var button = $(this);
        var url_t = "/redecasd/membros/gerenciar-membros/adicionar/1".replace('1', button.attr("data-number"));
        $.ajax({
            url: url_t,
            dataType: 'json',
            success: function(data) {
                $("#member_search_result").html(data.html_results);
                $("#member_list").html(data.html_member_list);
                input_field.value = '';
            }
        });
        return false;
    };

    $("#member_search").on("click", ".js-button-search-email", searchMember);
    $("#member_search").on("click", ".js-button-add-member", addMember);
    $("#member_list").on("click", ".js-member-remove", removeMember);

});
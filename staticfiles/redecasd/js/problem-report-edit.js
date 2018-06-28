
$(function (){

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#problem-report-modal .modal-content").html("");
        $('#problem-report-modal').modal('show');
        $('#problem-report-modal').addClass("show");
        $('#problem-report-modal').css("background-color","rgba(0,0,0,0.8)");
      },
      success: function (data) {
        $("#problem-report-modal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#problem-report-section").html(data.html_problem_list);
          $("#problem-report-modal").modal("hide");
          updateColor();
        }
        else {
          $("#problem-report-modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Update problem report record
  $("#problem-report-section").on("click", ".js-update", loadForm);
  $("#problem-report-modal").on("submit", ".js-update-form", saveForm);

  updateColor();

});
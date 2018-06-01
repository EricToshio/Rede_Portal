$(function() {

// events: [
//   // all day event
//   {
//     title  : 'Meeting',
//     start  : '2015-11-12'
//   },
//   // long-term event 
//   {
//     title  : 'Conference',
//     start  : '2015-11-13',
//     end    : '2015-11-15'
//   },
//   // short term event 
//   {
//     title  : 'Dentist',
//     start  : '2015-11-09T11:30:00',
//     end  : '2015-11-09T012:30:00'
//     allDay : false // will make the time show
//   }
// ]

 

  /* Functions */
  var day;
  var loadForm = function (date) {
    var url_t = "/redecasd/reservas/create/1".replace('1', date);
    $.ajax({
      url: url_t,
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#problem-report-modal .modal-content").html("");
        $('#problem-report-modal').modal("show");
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
          // $("#problem-report-section").html(data.html_problem_list);
          $("#problem-report-modal").modal("hide");
          $('#calendar').fullCalendar( "refetchEvents" );
          day.css("background-color","red");
        }
        else {
          $("#problem-report-modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  $("#problem-report-modal").on("submit", ".js-reservation-create-form", saveForm);

  $('#calendar').fullCalendar({
    themeSystem: 'jquery-ui',
    monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    dayNames: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'],
    dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
    // editable: true,
    // eventStartEditable: true,
    header: {
      left: 'prev,next today',
      center: 'title',
      right: ''
    },
    eventLimit: true,
    events: "/redecasd/reservas/events/",
    locale: 'pt',
    dayClick: function(date, jsEvent, view) {
      day = $(this);
      loadForm(date.format());
  }
  });

});

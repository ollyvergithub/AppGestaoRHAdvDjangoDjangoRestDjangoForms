var $ = jQuery;
function utilizouHoraExtra(id) {
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    //let token = id;

    console.log("AJAX ", id);

    $.ajax({
        type: "POST",
        url: 'utilizou-hora-extra-ajax/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (result) {
            console.log("Sucesso AJAX")
            $("#mensagem").text('Hora extra marcada como utilizada')
        },

    });

}
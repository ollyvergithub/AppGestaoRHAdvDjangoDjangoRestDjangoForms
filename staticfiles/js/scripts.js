var $ = jQuery;
function utilizouHoraExtra(id) {
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    //let token = id;

    console.log("AJAX ", id);

    $.ajax({
        type: "POST",
        url: '/horas-extras/utilizou-hora-extra-ajax/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (result) {
            console.log("Sucesso AJAX ", result);
            if (result.utilizada){
                $("#label_botao_horas_extras").text('Marcar como NÃO utilizado')
            }else {
                $("#label_botao_horas_extras").text('Marcar como utilizado')
            }
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text("Saldo do Banco: " + result.horas)

        },

    });

}
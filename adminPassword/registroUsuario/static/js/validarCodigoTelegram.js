(function() {
    window.onload = function() {
    console.log("HOLA")
    $("#divError").hide();
    $("#formularioAcceso").submit(function(event) {
    var usernameToken = document.getElementById("usernameToken").value;
	n = usernameToken.length
    if (n < 8) {
        $("#divError").show();
        $("#contenidoError").text("El nombre es demasiado corto, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}
    if (usernameToken == "") {
        $("#divError").show();
        $("#contenidoError").text("El nombre usuario de Telegram esta vacío");
        event.preventDefault();

	}

});//Cierre del evento submit

}//Cierre Window.onload

})();//Cierre de la función anónima.
(function() {
    window.onload = function() {
    console.log("HOLA")
    $("#divError").hide();
    $("#formularioLogin").submit(function(event) {
    var username = document.getElementById("username").value;
	n = username.length
    if (n < 8) {
        $("#divError").show();
        $("#contenidoError").text("El nombre de usuario es demasiado corto, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}
    if (username == "") {
        $("#divError").show();
        $("#contenidoError").text("El nombre usuario de Telegram esta vacío");
        event.preventDefault();

	}
    var password = document.getElementById("pwd").value;
    n2 = password.length
	if (password == "") {
        $("#divError").show();
        $("#contenidoError").text("Contraseña vacía");
        event.preventDefault();
	}
    if (n2 < 8) {
        $("#divError").show();
        $("#contenidoError").text("Contraseña demasiado corta, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}
    var codigo = document.getElementById("codigoAcceso").value;
    n3 = codigo.length
    if (codigo == "") {
        $("#divError").show();
        $("#contenidoError").text("Código vacío");
        event.preventDefault();
    }
    if (n3 < 5) {
        $("#divError").show();
        $("#contenidoError").text("Codigo demasiado corto, se requieren 5 carácteres mínimos.");
        event.preventDefault();
    }

});//Cierre del evento submit

}//Cierre Window.onload

})();//Cierre de la función anónima.
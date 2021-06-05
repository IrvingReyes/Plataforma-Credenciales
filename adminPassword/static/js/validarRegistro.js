(function() {
    window.onload = function() {
    console.log("HOLA")
    $("#divError").hide();
    $("#formularioUsuario").submit(function(event) {
    var nombre = document.getElementById("nombre").value;
	if (nombre == "") {
        $("#divError").show();
        $("#contenidoError").text("Nombre de usuario vacío");
        event.preventDefault();

	}
	n = nombre.length
    if (n < 8) {
        $("#divError").show();
        $("#contenidoError").text("Nombre demasiado corto, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}

	var username = document.getElementById("username").value;
	if (username == "") {
        $("#divError").show();
        $("#contenidoError").text("Username vacío");
        event.preventDefault();
	}

	n2 = username.length
    if (n2 < 8) {
        $("#divError").show();
        $("#contenidoError").text("Nombre de usuario demasiado corto, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}

	var contrasena = document.getElementById("password").value;

    n3 = contrasena.length
    if (n3 < 8) {
        $("#divError").show();
        $("#contenidoError").text("Contraseña demasiado corta, se requieren 8 carácteres mínimos.");
        event.preventDefault();
	}

	if (contrasena == "") {
        $("#divError").show();
        $("#contenidoError").text("Contraseña vacía");
        event.preventDefault();
	}

	var Ccontrasena = document.getElementById("cpassword").value;
	if (Ccontrasena != contrasena) {
        $("#divError").show();
        $("#contenidoError").text("Las contraseñas no coinciden.");
        event.preventDefault();
	}

	var correo = document.getElementById("correo").value;
	if (correo == "") {
        $("#divError").show();
        $("#contenidoError").text("El correo esta vacio.");
        event.preventDefault();
	}

    var telefono = document.getElementById("telefono").value;
	if (telefono == "") {
        $("#divError").show();
        $("#contenidoError").text("El teléfono está vacio.");
        event.preventDefault();
    }
    
    var tokenTelegram = document.getElementById("tokenTelegram").value;
	if (tokenTelegram == "") {
        $("#divError").show();
        $("#contenidoError").text("El token de Telegram está vacio.");
        event.preventDefault();
    }
    
    var chatId = document.getElementById("chatId").value;
	if (chatId == "") {
        $("#divError").show();
        $("#contenidoError").text("El chatId está vacio.");
        event.preventDefault();
	}

}); //Cierre del evento submit


} //Cierre Window.onload

})(); //Cierre de la función anónima.

//https://www.pythonanywhere.com/user/proy/files/home/proy/proyectoDjango/web2020/static/js/validacionRegistro.js?edit
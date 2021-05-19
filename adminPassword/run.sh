#!/bin/bash
function modouso() {
echo "Este es el script para inicializar el archivo manage.py con variables de entorno para la configuración sensible."
echo "Las variables de entorno se obtienen de un archivo .env"
echo "MODO DE USO:"
echo "run.sh <archivo.env> <parametro-manage.py>"
}


[[ "$#" == 2 ]] || { echo "Numero de parametros incorrecto"; modouso; exit 1;}
[[ -f "$1" ]] || { echo "se esperaba como primer parámetro un archivo env"; exit 1; }


for linea in $(ccdecrypt -c "$1"); do
	export $linea
done

python3 manage.py $2

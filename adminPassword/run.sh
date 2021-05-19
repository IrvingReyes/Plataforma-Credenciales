#! /bin/bash

[[ -f "$1" ]] || { echo "se esperaba como primer parámetro un archivo env"; exit 1; }

for linea in $(ccdecrypt -c "$1"); do
	echo "export $linea"
done

python manage.py runserver
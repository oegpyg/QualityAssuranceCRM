# QualityAssuranceCRM

Para generar cambios en las tablas:
> python manage.py makemigrations

Para aplicar los cambios en la base de datos
> python manage.py migrate

Para ejecutar en ambiente local
> python manage.py runserver


Para generar el DER
> python3 manage.py graph_models -a -g -o DER.png
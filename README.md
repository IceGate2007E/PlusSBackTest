# PlusSBackTest

Pasos para usar:

1. Clonar el repositorio
2. Escribir en la consola: cd plusS


Para usar la base de datos en postreSQL
1. Descargar postreSQL desde: https://www.postgresql.org/download/.
3. Entrar a pgAdmin y crear una nueva base de datos llamada plusSBackTest
4. En el caso de no tener un usuario, pdAdmin pedira la creacion de uno. Usar como nombre de usuario postgres y como contraseña postgres. En el caso de tenerlo, en plusS/basic/settings.py poner su nombre de usuario y contraseña dentro de databases

5. Escribir en la consola: python manage.py makemigrations
6. Escribir en la consola: python manage.py migrate
7..Escribir en la consola: python manage.py runserver

Listo! La app esta lista para usar
Entrar a http://localhost:8000/docs/ para ver los endpoints
    

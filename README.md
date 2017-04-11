# EmulaSIP 
Desarrollamos un Emulador de Sistemas de Post, que se puede correr online en 
http://otroyo.pythonanywhere.com/

**Ello, para apoyar un cursillo orientado a alumnos de colegios, interesados en 
comprender: lo que és la Computación**


Si a alguien le interesa, por favor comuníquese conmigo:
Andreas Polymeris, andreaspolymeris@gmail.com


**Como crear un virtual environment y server local:**
crear directorios web (se deberan crear estos directorios, con por ejemplo: mkdir):
```
/var/www/uploads/
/var/www/temporal/
```
dar permisos necesarios a los directorios:
```
sudo chmod 777 www/
sudo chmod 777 uploads/
sudo chmod 777 temporal/

```
clonar el repositorio
```
git clone https://github.com/Otroyo/EmulaSIP
```
```
cd EmulaSIP
``` 
intalar Virtualenv:
```
sudo apt-get install virtualenv
o
sudo apt-get install python-virtualenv
```
instalar pip y Flask:
```
sudo apt-get install python-pip
sudo pip install flask
```
Crear un virtualenv con flask (debe crearce en la carpeta EmulaSIP, junto a flask_app.py, templates y el resto de archivos):
```
virtualenv flask
```
Añadir las librearias necesarias: (copiar y pegar todo junto en la consola, quizas sea necesario el comando sudo)
```
flask/bin/pip install flask && flask/bin/pip install flask-login && flask/bin/pip install flask-openid && flask/bin/pip install flask-mail && flask/bin/pip install flask-sqlalchemy && flask/bin/pip install sqlalchemy-migrate && flask/bin/pip install flask-whooshalchemy && flask/bin/pip install flask-whooshalchemy && flask/bin/pip install flask-wtf && flask/bin/pip install flask-babel && flask/bin/pip install guess_language && flask/bin/pip install flipflop && flask/bin/pip install coverage
```
correr pagina web(se debe estar dentro de EmulaSIP:
```
flask/bin/python2.7 flask_app.py
```
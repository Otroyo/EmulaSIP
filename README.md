# EmulaSIP

Desarrollamos un Emulador de Sistemas de Post, que se puede correr online en
[http://otroyo.pythonanywhere.com/](http://otroyo.pythonanywhere.com/)

**Ello, para apoyar un cursillo orientado a alumnos de colegios, interesados en
comprender: lo que es la Computación.**


Si a alguien le interesa, por favor comuníquese conmigo:
Andreas Polymeris, andreaspolymeris@gmail.com


**Como crear un virtual environment y server local:**

Instalar virtualenv:
```
sudo apt-get install virtualenv
o
sudo apt-get install python-virtualenv
o
sudo apt-get install python-pip
sudo pip install virtualenv
```

crear directorios web (se deberán crear estos directorios, con por ejemplo: mkdir):
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
crear carpetda de proyecto Flask:

```
mkdir EmulaSIP-flask
cd EmulaSIP-flask
virtualenv flask
```
copiar este graaaan comando en la terminal!!(dentro de su carpeta de proyecto Flask):
```
flask/bin/pip install flask && flask/bin/pip install flask-login && flask/bin/pip install flask-openid && flask/bin/pip install flask-mail && flask/bin/pip install flask-sqlalchemy && flask/bin/pip install sqlalchemy-migrate && flask/bin/pip install flask-whooshalchemy && flask/bin/pip install flask-whooshalchemy && flask/bin/pip install flask-wtf && flask/bin/pip install flask-babel && flask/bin/pip install guess_language && flask/bin/pip install flipflop && flask/bin/pip install coverage
```
Clonar repositorio(Dentro de su carpeta de proyecto Flask):
```
//si no tiene git:

sudo apt-get install git

//después:

git clone https://github.com/otroyo/EmulaSIP
```
Correr en localhost:

_Dentro de su carpeta de proyecto Flask:_

```
flask/bin/python2.7 EmulaSIP/flask_app.py
```

### Attribution

[post logo](https://github.com/Otroyo/EmulaSIP/blob/master/static/post-line.png) from
[OpenLogicProject](https://github.com/OpenLogicProject/portraits) is licensed
under [CC-BY-4.0](https://creativecommons.org/licenses/by-nc/4.0/) / Desaturated
from original

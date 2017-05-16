# -*- coding: utf-8 -*-

import time
import os
from flask import Flask, request, render_template, redirect, url_for, \
                  send_from_directory
from werkzeug.utils import secure_filename
from urlparse import urljoin
from random import randint

# la proxima linea es la unica adaptacion cuando se cambia de Host;
# mas, eventualmente, el quitar las ultimas dos lineas de este codigo
uhost = "http://0.0.0.0:5000"
cpuesta = "siu<=p"  # si se cambia, cambiar base.html
uborrasip = urljoin(uhost, 'borrasip/'+cpuesta)
usubesip = urljoin(uhost, 'subesip/'+cpuesta)
ucorresip = urljoin(uhost, 'corresip/'+cpuesta)
usale = urljoin(uhost, '')

UPLOAD_FOLDER = '/var/www/uploads'
TEMPORAL_FOLDER = '/var/www/temporal'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sip']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPORAL_FOLDER'] = TEMPORAL_FOLDER
# Presenta lo que hay en UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def preinicio():
    return render_template('clave.html')


@app.route('/clave', methods=['GET', 'POST'])
def clave():
    clave = request.form['clave']
    if clave == cpuesta:
        return redirect(url_for('inicio', clave=clave))
    return redirect('')


@app.route('/inicio/<clave>',  methods=['GET', 'POST'])
def inicio(clave):
    if not clave == cpuesta:
        return redirect('')
    return render_template("inicio.html")


# Archivos---------------------------------------------------------------------
@app.route('/archivos/<clave>', methods=['GET', 'POST'])
def archivos(clave):
    if not clave == cpuesta:
        return redirect('')
    sips = [f for f in os.listdir('/var/www/uploads') if f.endswith('txt')]
    pdfs = [f for f in os.listdir('/var/www/uploads') if not f.endswith('txt')]
    numsips = len(sips)
    numpdfs = len(pdfs)
    randn = str(randint(9000, 99999))
    return render_template("Archivos.html",
                           numsips=numsips,
                           numpdfs=numpdfs,
                           sips=sips,
                           pdfs=pdfs,
                           randn=randn)


# about------------------------------------------------------------------------
@app.route('/about/<clave>', methods=['GET', 'POST'])
def about(clave):
    if not clave == cpuesta:
        return redirect('')
    return render_template("about.html")


# sube ------------------------------------------------------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/subesip/<clave>', methods=['GET', 'POST'])
def subesip(clave):
    warning = ""
    if not clave == cpuesta:
        return redirect('')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            sips = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('txt')]
            if filename not in sips:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                warning = "Archivo subido correctamente."
            else:
                # print filename
                warning = "Ya existe un archivo con nombre "+str(filename)
            # return redirect(url_for('inicio', clave = cpuesta))
    return render_template("upload.html", title='Subir', warning=warning)


@app.route('/<filename>')
def uploaded_file(filename):
    filecontent = send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return filecontent
# -----------------------------------------------------------------------------


# borra------------------------------------------------------------------------
@app.route('/borrasip/<clave>', methods=['GET', 'POST'])
def borrasip(clave):
    if not clave == cpuesta:
        return redirect('')
    return render_template(
        'delsip.html', title='Borrar',
        data=[{'name': f} for f in os.listdir(UPLOAD_FOLDER)])


@app.route("/borra", methods=['GET', 'POST'])
def borra():
    sipdel = request.form.get('comp_select')
    os.remove((UPLOAD_FOLDER+'/'+sipdel))
    return redirect(url_for('inicio', clave=cpuesta))
# -----------------------------------------------------------------------------


# corre -----------------------------------------------------------------------
@app.route('/corresip/<clave>', methods=['GET', 'POST'])
def corresip(clave):
    if not clave == cpuesta:
        return redirect('')
    return render_template('selectsip.html',
                           title='Seleccion',
                           data=[{'name': f} for f in os.listdir(UPLOAD_FOLDER)
                                 if f.endswith('txt')])


@app.route("/seguir", methods=['GET', 'POST'])
def seguir():
    sipsele = request.form.get('comp_select')
    fl = archivo(UPLOAD_FOLDER+'/'+sipsele)
    if not fl[0]:
        warning = fl[1]
        bad_line = fl[2]
        numeroR = str(randint(9000, 9999))
        upr = urljoin('/', sipsele)
        return render_template('syntax_error.html',
                               warning=warning,
                               bad_line=bad_line,
                               sipsele=sipsele,
                               upr=upr,
                               numeroR=numeroR)
    else:
        return redirect(url_for('corre', sipsele=sipsele, clave=cpuesta,))


@app.route("/syntax_error", methods=['GET', 'POST'])
def syntax_error(warning, bad_line):
    return render_template('syntax_error.html',
                           warning=warning,
                           bad_line=bad_line)


@app.route("/corre/<sipsele>/<clave>", methods=['GET', 'POST'])
def corre(sipsele, clave):
    if not clave == cpuesta:
        return redirect('')
    ues = url_for('ejecuta', sipsele=sipsele, clave=cpuesta)
    upr = urljoin('/', sipsele)
    numeroR = "1"#str(randint(9000, 9999))
    return render_template('pinicial.html',
                           title='Ingreso',
                           sipsele=sipsele,
                           ues=ues, upr=upr,
                           numeroR=numeroR)


# Funciones del emulador que se emplean en ejecuta(sipsele)

@app.route('/palabras.txt')
def palabras():
    filecontent2 = send_from_directory(app.config['TEMPORAL_FOLDER'],
                                       'palabras.txt')
    return filecontent2


def archivo(u):
    """
    lee el archivo de post y lo transforma a la lista de pares
    """
    def leer_linea(line, li):
        Ll = list(line.strip())
        yes = True
        if Ll == [] or Ll[0] == "/" and Ll[1] == "/":
            yes = False
        if yes:
            p, q = line.split(",")
            p = p.strip()
            q = q.strip()
            q = q.strip(";")
            p = list(p)
            q = list(q)
            par = [p, q]
            li.append(par)
        return li

    def syntax_error(text):
        tli = []
        count = 1
        for line in text:
            ll = list(line)
            if ll != [] and len(ll) != 1 and ll[0:2] != ['/', '/']:
                tli.append((ll, count))
            count += 1

        essential = []
        for line in tli:
            lline = ([x for x in line[0] if x == "," or x == ";"], line[1])
            essential.append(lline)

        errors = []
        for x in essential:
            if not x[0] == [',', ';']:
                errors.append(x)

        if errors != []:
            return (True, errors[0][1])
        return (False, None)

    li = []
    infile = open(u, 'r')
    text = infile.readlines()
    tli = syntax_error(text)

    if tli[0]:
        return (False, "Error de syntaxis en linea "+str(tli[1])+"!",
                str(text[tli[1]-1]))

    for l in text:
        li = leer_linea(l, li)

    return (True, li)


def revision(p, q, word):
    """
    reisa si el "p" de li calsa con "word", retorna la palabra y end
    dependiendo si es la palabra correcta o no
    """
    z, end, word2, count = len(p), 0, [], 0

    for i in word:
        count += 1
        if z < count:
            break

    if count >= z:
        for el in range(0, z):
            word2.append(word[el])

        if p == word2:
            end = 1
            for el in range(0, z):
                word.pop(0)
            word.extend(q)
    return end, word


def recorre_li(li, word):
    """
    usando la funcion de revision busca los P correspondientes a cada word
    hasta encontrarse con "%", retorna la ultima "word" usada
    """
    fin = 0
    k = 0
    while True:
        p = li[k][0]
        q = li[k][1]
        end, word = revision(p, q, word)
        if end == 1:
            break
        k = k+1
        if li[k-1] == li[-1]:
            fin = 1
            break
    return fin, word


@app.route('/ejecuta/<sipsele>/<clave>', methods=['POST', 'GET'])
def ejecuta(sipsele, clave):
    if not clave == cpuesta:
        return redirect('')
    if request.method == 'POST':
        pinicial = request.form['pinicial']
        u = urljoin('/var/www/uploads/', sipsele)
        if not request.form['tope'] == 'None':
            tope = int(request.form['tope'])
        else:
            tope = 0
        print "URL : ", u

        # programa
        filepreventivo = open('/var/www/temporal/palabras.txt', 'w')
        os.remove('/var/www/temporal/palabras.txt')
        start = time.clock()
        fin = 0
        fl = archivo(u)
        word = pinicial
        word = list(word)
        file = open('/var/www/temporal/palabras.txt', 'w')
        file.write("SE ESCRIBIRAN MAXIMO 100000 PALABRAS \n \n")
        file.write("".join(word)+"   - entrada\n")
        iteraciones = 0

        if fin == 0:
            li = fl[1]

        while fin == 0:
            fin, word = recorre_li(li, word)
            iteraciones += 1
            if not iteraciones > 100000 and not fin == 1:
                file.write(("".join(word)+"  -"+str(iteraciones)))
                file.write("\n")
            if iteraciones == tope:
                word = ['Llego al limite']
                break

        Time = time.clock()-start
        pfinal = "".join(word)
        upr = urljoin('/', sipsele)
        uco = urljoin('/corre/', sipsele+'/'+cpuesta)
        numeroR = str(randint(9000, 9999))
        uinicio = uhost+'/inicio/'+cpuesta
        iteraciones -= 1
        return render_template("resultadoCS.html",
                               title='Detencion',
                               sipsele=sipsele,
                               pinicial=pinicial,
                               pfinal=pfinal,
                               uco=uco, upr=upr,
                               uinicio=uinicio,
                               ucorresip=ucorresip,
                               usale=usale,
                               iteraciones=iteraciones,
                               Time=Time,
                               numeroR=numeroR)


# solo para testeo local:
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

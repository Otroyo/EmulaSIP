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
            p, q = p.strip(), q.strip()
            q = q.strip(";")
            p, q = list(p), list(q)
            par = (p, q)
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


def revisa(u, v, w):
    """
    si p <= w, devuelve (True, (p\u)v) sino (False, (p\u))
    """
    if not u:
        return (True, w+v)
    elif not w:
        return (False, [])
    elif w[0] == u[0]:
        return revisa(u[1:], v, w[1:])
    else:
        return (False, [])


def recorre_li(li, word):
    """
    Hace un cambio en word.
    """
    end = False
    for pair in li:
        u = pair[0]
        v = pair[1]
        end, w = revisa(u, v, word)
        if end:
            word = w
            break
    return (not end), word

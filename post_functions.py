#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def revicion(u,v,w):
    trash = []
    if len(w) < len(u):
        return w, False
    for x in range(len(u)):
        u0 = u[x]
        if u0 == w[0]:
            trash.append(u0)
            w.pop(0)
        else:
            trash.extend(w)
            return trash, False
    w.extend(v)
    return w, True


def recorre_li(sip, w):
    for (u,v) in sip:
        w, b = revicion(u, v, w)
        if b:
            return False, w
    return True, w

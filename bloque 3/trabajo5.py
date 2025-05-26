def saludo(lang):
    if lang=="es":
        return "Hola"
    elif lang == "fr":
        return"Bonjour"
    else:
        return"Hello"

print(saludo ("en"))

print(saludo ("es"))

print(saludo ("fr"))
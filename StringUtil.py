def output(texto):
    print("Texto: ",texto)

def tamanho(texto):
    tamanhoTexto = len(texto)
    print("Tamanho: ", tamanhoTexto)
    return tamanhoTexto

def maiusculo(texto):
    maiuscula = texto.upper()
    print("Maiuscula: ", maiuscula)
    return maiuscula

def minuscula(texto):
    minuscula = texto.lower()
    print("Minuscula: ", minuscula)
    return minuscula

def letra(texto):
    letra = input("Digite a letra que deseja encontrar: ")
    texto = texto.upper()
    enc = 0
    for aux in texto:
        if (letra == aux):
            enc += 1

    print("A letra foi encontrada %i vezes"%enc )
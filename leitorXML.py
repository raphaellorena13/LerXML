from xml.dom.minidom import parse

doc = parse('ArquivoXLM.xml')

xml = doc.documentElement


def ler(primeiro_nivel, final_nivel):
    primeiro = xml.getElementsByTagName(primeiro_nivel)

    for p in primeiro:
        
        print(p.getElementsByTagName(final_nivel)[0].childNodes[0].data)


print('---- Emissor ----')
ler('emit','xNome')

print('---- Destinatario----')
ler('dest', 'xNome')
ler('dest','fone')

print('---- produtos ----')
ler('det', 'xProd')


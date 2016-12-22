from xml.dom import minidom

def get_substitutions():
    xmldoc = minidom.parse('substitutions.xml')
    itemlist = xmldoc.getElementsByTagName('substitute')

    return itemlist


def apply_substitutions(sentence, substs):
    sentence = sentence.lower()
    n = len(substs)
    for i in range(n):
        find = substs[i].attributes['find'].value
        repl = substs[i].attributes['replace'].value
        if (len(find)):
            sentence = sentence.replace(find, repl)

    return sentence.strip()

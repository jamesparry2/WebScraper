def getContentFromHtmlViaDomNode(domNone, html):
    content = []
    for element in html.select(domNone):
        content.append(str(element))
    return content

def getContentFromHtmlViaAttribute(domNone, html, htmlAttribute):
    content = []
    for element in html.select(domNone):
        content.append(element[htmlAttribute])
    return content

def getContentFromHtmlViaPredicate(domNode, html, htmlAttribute, predicate):
    content = []
    for element in html.select(domNode):
        if element[htmlAttribute] == predicate:
            content.append(element)
    return content
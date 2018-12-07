def getContentFromHtmlViaAttribute(domNone, html, htmlAttribute):
    content = []
    for element in html.select(domNone):
        content.append(element[htmlAttribute])
    return content

def getContentFromHtmlViaIde(domNode, html, htmlAttribute, predicate):
    content = []
    for element in html.select(domNode):
        if element[htmlAttribute] == predicate:
            content.append(element)
    return content
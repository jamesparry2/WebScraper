class WebScrapedObject:
    def __init__(self, propertyName, propertyContent):
        self.PropertyName = propertyName
        self.PropertyContent = propertyContent
    def getPropertyName(self):
        return self.PropertyName
    def getPropertyContent(self):
        return self.PropertyContent

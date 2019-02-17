class TextObject:
    def __init__(self , text , font , color):
        self.textSurface = font.render(text, True, color)
    
    
    def get(self):
        return self.textSurface, self.textSurface.get_rect()
# Factory pattern in python

class Button(object):
    text = "This is Button"
    def get_text(self):
        return self.text

# Image class extends Button
class Image(Button):
    text = "This is an Image!"
    def get_text(self):
        return self.text
# Input class extends Button
class Input(Button):
    text = "This is an Input!"
    def get_text(self):
        return self.text
# Flash class extends Button
class Flash(Button):
    text = "This is a Flash!"
    def get_text(self):
        return self.text
        
# Factory class to generate objects of the class
class ButtonFactory():
    def create_button(self, typeOfButton):
        if typeOfButton == 'Image':
            return Image()
        if typeOfButton == 'Flash':
            return Flash()
        if typeOfButton == 'Input':
            return Input()


buttonObj = ButtonFactory()
button = ['Image', 'Input','Flash']
for b in button:
    print(buttonObj.create_button(b).get_text())
        
    
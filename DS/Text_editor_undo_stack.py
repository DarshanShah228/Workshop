'''
You're building a lightweight text editor for a startup. Every time a user types a character it gets recorded. When they press Ctrl+Z (Undo), the last action must be reversed. The editor must support

type(char)-records a character

undo removes the last typed character]f

getText() retums the current text.
'''
class TextEditor:
    def __init__(self):
        self.text = []

    def type(self, ch):
        self.text.append(ch)

    def undo(self):
        if self.text:
            removed = self.text.pop()
            print("Removed Character:", removed)
        else:
            print("Nothing to Undo!")

    def getText(self):
        return " ".join(self.text)

editor = TextEditor()

n = int(input("Enter number of characters: "))

for i in range(n):
    ch = input(f"Enter character {i+1}: ")
    editor.type(ch)

print("Current Text:", editor.getText())

choice = input("Do you want to Undo? (yes/no): ")

if choice.lower() == "yes":
    editor.undo()

print("Final Text:", editor.getText())
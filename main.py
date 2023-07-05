from note_repository import NoteRepository
from note_service import NoteService
from menu import Menu

NOTES_FILE = "notes.json"

class Main:
    def __init__(self):
        repository = NoteRepository(NOTES_FILE)
        service = NoteService(repository)
        self.menu = Menu(service)

    def run(self):
        self.menu.run()

if __name__ == "__main__":
    app = Main()
    app.run()

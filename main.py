import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from models.vote_model import VoteModel
from services.file_handler import FileHandler


class MainWindow(QMainWindow):
    """Main GUI window."""

    def __init__(self) -> None:
        super().__init__()

        loadUi("gui/main_window.ui", self)

        self.model = VoteModel()

        john, jane = FileHandler.load()
        self.model.set_votes(john, jane)

        self.voteJohnBtn.clicked.connect(self.vote_john)
        self.voteJaneBtn.clicked.connect(self.vote_jane)
        self.resetBtn.clicked.connect(self.reset_votes)

        self.update_label()

    def vote_john(self) -> None:
        """Handle vote for John."""
        self.model.vote_john()
        self.save_and_update()

    def vote_jane(self) -> None:
        """Handle vote for Jane."""
        self.model.vote_jane()
        self.save_and_update()

    def reset_votes(self) -> None:
        """Reset all votes."""
        self.model.reset_votes()
        self.save_and_update()

    def save_and_update(self) -> None:
        """Save votes and update label."""
        john, jane, _ = self.model.get_results()
        FileHandler.save(john, jane)
        self.update_label()

    def update_label(self) -> None:
        """Update result label text."""
        john, jane, total = self.model.get_results()
        self.resultLabel.setText(
            f"John – {john}, Jane – {jane}, Total – {total}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
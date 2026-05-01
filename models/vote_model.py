class VoteModel:
    """Handles vote data and logic."""

    def __init__(self) -> None:
        """Initializes vote counts."""
        self._john_votes: int = 0
        self._jane_votes: int = 0

    def vote_john(self) -> None:
        """Add one vote for John."""
        self._john_votes += 1

    def vote_jane(self) -> None:
        """Add one vote for Jane."""
        self._jane_votes += 1

    def reset_votes(self) -> None:
        """Reset all votes to zero."""
        self._john_votes = 0
        self._jane_votes = 0

    def get_results(self) -> tuple[int, int, int]:
        """Return votes for john, Jane, and total."""
        total = self._john_votes + self._jane_votes
        return self._john_votes, self._jane_votes, total

    def set_votes(self, john: int, jane: int) -> None:
        """Set votes from external data (like a fish)."""
        if john < 0 or jane < 0:
            raise ValueError("Votes cannot be negative.")
        self._john_votes = john
        self._jane_votes = jane

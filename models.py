from django.db import models # type: ignore


class BoardGame(models.Model):
    boardgame_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    available = models.BooleanField(default=True, help_text="Is this boardgame available to borrow?")

    def __str__(self):
        return f"{self.boardgame_name} (Owner: {self.owner_name})"


class GameComment(models.Model):
    boardgame = models.ForeignKey(BoardGame, related_name='comments', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], help_text="Rate the game 1 - 5 stars")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.boardgame.boardgame_name} - {self.rating} stars"


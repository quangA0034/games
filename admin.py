from django.contrib import admin

from .models import BoardGame, GameComment

@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('boardgame_name', 'owner_name', 'min_players', 'max_players', 'available')


@admin.register(GameComment)
class GameCommentAdmin(admin.ModelAdmin):
    list_display = ('boardgame', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('boardgame__boardgame_name', 'comment')
# Register your models here.

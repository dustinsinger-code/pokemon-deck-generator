from django.contrib import admin
from .models import Card, Deck, DeckCard


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'card_id', 'type']


admin.site.register(Card, CardAdmin)


class DeckAdmin(admin.ModelAdmin):
    pass


admin.site.register(Deck, DeckAdmin)


class DeckCardAdmin(admin.ModelAdmin):
    list_display = ['deck_id', 'card_id', 'get_card_name', 'count']

    def get_card_name(self, obj):
        return obj.card.name


admin.site.register(DeckCard, DeckCardAdmin)

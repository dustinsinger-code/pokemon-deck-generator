from django.core.management import BaseCommand
from deck.models import Deck, DeckCard


class Command(BaseCommand):

    def handle(self, *args, **options):
        latest_deck = Deck.objects.latest('id')
        deck_cards = DeckCard.objects.filter(deck=latest_deck)

        for deck_card in deck_cards:
            for i in range(deck_card.count):
                print("_________________________________")
                print(deck_card.card.name)

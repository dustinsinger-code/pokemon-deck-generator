The code that you'd probably be most interested in seeing is located in deck/management/commands.
I've create two commands, one called generate_deck, and another called view_previous_deck.
The output of the deck is simply printed to the console with the card names.<br /><br />


**The database schema is as follows:**


There are 3 models:

Card, Deck, DeckCard <br /><br />


Card contains: 

**name**, **type**, **card_id** - all of which come from the pokemon API <br /><br />


Deck contains:

**cards** - which is a manytomany field with a custom intermediate model <br /><br />


DeckCard - This is the intermediate model which contains:

**deck** - foreign key to Deck

**card** - foreign key to Card

**count** - This field is used to count how many of the specific card are in the deck. Defaults to 1.

# Barter
 
This is a Discord bot to be used as a store. Specifically, this was made for a DND 5e game. In addition to the files here, you'll also need an items.txt and regularitems.txt. These hold info about magic items that the bot will choose a selection of to be available and the standard items that should always be available, respectively. These files can't be shared due to them containing copywritten material. This is written primarily for a personal game, so it's not made to be super customizable. That said, it maybe might may be useful as a starting point if nothing else.
 
 # Item Files Formatting
 Both files can handle as many items as you want.

 items.txt follows this formatting:
 
 item name of however many words, rarity
 
 Rarity can be common, uncommon, rare, very rare, or legendary.
 
 regularitems.txt has items separated by categories and follows this formatting:
 /category
 item name of however many words, cost in gold as a number
 
 Category should be Armor, Simple, Martial, Foci, Regular Items, Packs, Tools, Gaming & Instruments, and Mounts & Vehicles. 
 This categories can be changed, but you'll also have to edit their references in Barter.py file to do so.

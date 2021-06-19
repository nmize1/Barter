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
 
 # Settings
 
 storesettings.txt contains some info about the stock and price of the magic items. 
 Aside from the first line, each line follows this formatting:
 rarity num_of_this_rarity_to_stock base_price_of_this_rarity
 
 The base price is later modified by a random multiplier. This currently can't be configured. 
 
 # Commands
 
 $list - Shows a list of characters currently registered by the bot and their current balance.
 
![image](https://user-images.githubusercontent.com/50761210/122330422-281f7800-cf01-11eb-9ace-626316714b56.png)

$add_character char_name starting_balance - Registers a new character with the bot named 'char_name' and initialized with starting_balance gold. starting_balance must be a number.

![image](https://user-images.githubusercontent.com/50761210/122330489-484f3700-cf01-11eb-822e-a509eed13682.png)

$remove_character char_name - Removes the character from the bot's register list

![image](https://user-images.githubusercontent.com/50761210/122330574-72085e00-cf01-11eb-97e5-6d0ae8c180f9.png)

$add money char_name amount_to_add - Adds amount_to_add gold to char_name

![image](https://user-images.githubusercontent.com/50761210/122330635-919f8680-cf01-11eb-8798-15cca714daf0.png)

$remove money char_name amount_to_sub - Removes amount_to_sub gold from char_name

![image](https://user-images.githubusercontent.com/50761210/122330690-a4b25680-cf01-11eb-829a-d4e67381f0b1.png)

$stock magic - displays the current stock of magic items and their costs

![image](https://user-images.githubusercontent.com/50761210/122330917-fbb82b80-cf01-11eb-9e0a-c9c619e6f4b6.png) 

(beautiful cya censoring)

$stock category - category is armor, simple, martial, foci, items, packs, tools, gaming, instruments, mounts, or vehicles - displays stock in the chosen category.

![image](https://user-images.githubusercontent.com/50761210/122331095-42a62100-cf02-11eb-9992-b14d502e2ae3.png)

$buy char_name category item_name - char_name buys item_name from specified category

![image](https://user-images.githubusercontent.com/50761210/122332740-ee507080-cf04-11eb-9bc0-3c72209cc33d.png)

$restock - restocks the magic item stock

![image](https://user-images.githubusercontent.com/50761210/122331415-c6f8a400-cf02-11eb-8d98-9ba1bc22b0b8.png)

$help - shows this list

![image](https://user-images.githubusercontent.com/50761210/122508803-94b57800-cfd0-11eb-8124-789b6d4e5dde.png)


# TODO
- ~~Add multiplier config into storesettings.txt~~ Done
- Add restock timer so magic item stock changes naturally 
- ~~Fix characters.txt so that it doesn't have multiple empty lines after removing characters (maybe just convert to json and forget it)~~ Characters are now stored in json file
- ~~Fix float overflow deleting the character~~ Storing characters in json removed the need to rewrite the text file, which failed to readd characters after float overflow
- Fix adding characters with over 2000 characters in their name or balance breaking the $add_character and $list commands until that character is removed.
- Maybe more?

Possible updates if I decide to keep working on this:
- Allow for custom item categories 
- Allow for more or less categories
- Optimizations
- Maybe more?

Possible but very very unlikely updates:
- dndbeyond scraper to automatically create items.txt and regularitems.txt 

This is technically possible, but would be very complicated for me so probably won't happen anytime soon.


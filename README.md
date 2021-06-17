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

![image](https://user-images.githubusercontent.com/50761210/122331382-b811f180-cf02-11eb-97c0-9b9a6d54951f.png)

$restock - restocks the magic item stock

![image](https://user-images.githubusercontent.com/50761210/122331415-c6f8a400-cf02-11eb-8d98-9ba1bc22b0b8.png)





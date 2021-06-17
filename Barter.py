import discord
import os
import random


client = discord.Client()

#define characters as a dictionary to store characters and current money
characters = {}

#define items in categories
common = {}
uncommon = {}
rare = {}
very_rare = {}
legendary = {}

#import items from items.txt
print("Loading Items")
with open("items.txt") as items:
    for line in items:
        (key, val) = line.split(',')
        val = val.strip()
        if(val == "common"):
            common[key] = val
        elif(val == "uncommon"):
            uncommon[key] = val
        elif(val == "rare"):
            rare[key] = val
        elif(val == "very rare"):
            very_rare[key] = val
        elif(val == "legendary"):
            legendary[key] = val
        else:
            print("Item didn't have a rarity")

print("Items Loaded")

#For Magic Items#
#choose a number of each rarity of items
#generate random prices based on those items
#create the stock list
stock = {}
rarities = []
amounts = []
prices = []
price_multipliers = [.01, .25, .25, .5, .5, .5, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 10]
def StockStore():
    #get stock settings
    with open("storesettings.txt") as settings:
        for line in settings:
            if line.startswith("#"):
                print("#")
            else:
                (rarity, amount, price) = line.split()
                rarities.append(rarity)
                a = int(amount)
                amounts.append(a)
                p = int(price)
                prices.append(p)
    #choose items and apply prices
    #put them in the stock
    i = 0
    while(i != amounts[0]):
        item = random.choice(list(common.keys()))
        stock[item] = prices[0] * random.choice(price_multipliers)
        i = i + 1
        print(item)
    i = 0
    while(i != amounts[1]):
        item = random.choice(list(uncommon.keys()))
        stock[item] = prices[1] * random.choice(price_multipliers)
        i = i + 1
        print(item)
    i = 0
    while(i != amounts[2]):
        item = random.choice(list(rare.keys()))
        stock[item] = prices[2] * random.choice(price_multipliers)
        i = i + 1
        print(item)
    i = 0
    while(i != amounts[3]):
        item = random.choice(list(very_rare.keys()))
        stock[item] = prices[3] * random.choice(price_multipliers)
        i = i + 1
        print(item)
    i = 0
    while(i != amounts[4]):
        item = random.choice(list(legendary.keys()))
        stock[item] = prices[4] * random.choice(price_multipliers)
        i = i + 1
        print(item)
StockStore()

#For Regular Items that should always be available#
armor = {}
simple = {}
martial = {}
foci = {}
nitems = {}
packs = {}
tools = {}
gandm = {}
mounts = {}

with open("regularitems.txt") as items:
    for line in items:
        if line.startswith("/"):
            type = line[1:len(line) - 1]
            type.strip()
        else:
            (item, cost) = line.split(",")
            cost = cost.strip()
            if(type == "Armor"):
                armor[item] = float(cost)
            if(type == "Simple"):
                simple[item] = float(cost)
            if(type == "Martial"):
                martial[item] = float(cost)
            if(type == "Foci"):
                foci[item] = float(cost)
            if(type == "Regular Items"):
                nitems[item] = float(cost)
            if(type == "Packs"):
                packs[item] = float(cost)
            if(type == "Tools"):
                tools[item] = float(cost)
            if(type == "Gaming Sets & Instruments"):
                gandm[item] = float(cost)
            if(type == "Mounts & Vehicles"):
                mounts[item] = float(cost)

#open the local character data and create characters with it
with open("characters.txt") as dic:
    #create a list of lines skipping any blank lines
    lines = list(line for line in (l.strip() for l in dic) if line)
    for line in lines:
        (name, gold) = line.split()
        characters[name] = gold

def AddChar(name):
    if len(name) >= 3:
        if name[2].isdigit():
            characters[name[1]] = name[2]
            with open("characters.txt", "a") as dic:
                dic.write("\n" + name[1] + " " + name[2])
            return ("Added " + name[1] + " with " + name[2] + " gold.")
        else:
            return ('Second argument must be a number')
    else:
        return('Amount required as second argument')


def RemoveChar(name):
    gold = characters[name[1]]
    with open("characters.txt", "r") as f:
        lines = f.readlines()
    with open("characters.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != name[1] + " " + gold:
                f.write(line)
    del characters[name[1]]
    return ("Removed " + name[1])


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #### Character Manipulations ####
    #return a list of characters and their money in character
    msg = ""
    if message.content.startswith('$list'):
        chars = list(characters.keys())
        msg = "These are my current customers and their bank balance:\n"
        for char in chars:
            msg = msg + char + " has " + characters[char] + ' gp\n'
        await message.channel.send(msg)

    #add a character to the dictionary and update the local storage
    if message.content.startswith('$add_character'):
        name = []
        name = message.content.split()
        await message.channel.send(AddChar(name))

    #remove a character from the dictionary and update the local storage
    if message.content.startswith('$remove_character'):
        name = []
        name = message.content.split()
        await message.channel.send(RemoveChar(name))

    #add money to an existing character
    if message.content.startswith('$add money'):
        msg = ""
        name = []
        name = message.content.split()
        if name[3].isdigit():
            if name[2] in characters:
                bal = float(characters[name[2]])
                newbal = bal + float(name[3])
                n = ("null", name[2], bal)
                RemoveChar(n)
                n = ("null", name[2], str(int(newbal)))
                AddChar(n)
                msg = "Thank you for your deposit! " + name[2] + " now has " + str(newbal) + " gp."
            else:
                msg = "Sorry, I don't have an account for " + name[2] + "."
        else:
            msg = "Sorry, I can't add " + name[3] + " to your account. It must be an amount."
        await message.channel.send(msg)

    #remove money from an existing character
    if message.content.startswith('$remove money'):
        msg = ""
        name = []
        name = message.content.split()
        if name[3].isdigit():
            if name[2] in characters:
                bal = float(characters[name[2]])
                newbal = bal - float(name[3])
                n = ("null", name[2], bal)
                RemoveChar(n)
                n = ("null", name[2], str(int(newbal)))
                AddChar(n)
                msg = "I've removed " + name[3] + " from " + name[2] + "'s account. They now have " + str(newbal) + " gp."
            else:
                msg = "Sorry, I don't have an account for " + name[2] + "."
        else:
            msg = "Sorry, I can't remove " + name[3] + " from your account. It must be an amount."
        await message.channel.send(msg)

    #restock magic items
    if message.content.startswith('$restock'):
        stock.clear()
        StockStore()
        await message.channel.send("Restocked Magic Items.")

    #### STOCK PRINTERS ####
    msg = ""
    #print store stock of magic items
    if message.content.startswith('$stock magic'):
        store = list(stock.keys())
        for item in store:
            msg = msg + item + " | " + str(stock[item]) + "gp\n"
        await message.channel.send(msg)

    #print regular stocks
    if message.content.startswith('$stock armor'):
        store = list(armor.keys())
        for item in store:
            msg = msg + item + " | " + str(armor[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock simple weapons'):
        store = list(simple.keys())
        for item in store:
            msg = msg + item + " | " + str(simple[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock martial weapons'):
        store = list(martial.keys())
        for item in store:
            msg = msg + item + " | " + str(martial[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock foci'):
        store = list(foci.keys())
        for item in store:
            msg = msg + item + " | " + str(foci[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock items'):
        store = list(nitems.keys())
        for item in store:
            msg = msg + item + " | " + str(nitems[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock packs'):
        store = list(packs.keys())
        for item in store:
            msg = msg + item + " | " + str(packs[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock tools'):
        store = list(tools.keys())
        for item in store:
            msg = msg + item + " | " + str(tools[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock gaming sets'):
        store = list(gandm.keys())
        for item in store:
            msg = msg + item + " | " + str(gandm[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock instruments'):
        store = list(gandm.keys())
        for item in store:
            msg = msg + item + " | " + str(gandm[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock mounts'):
        store = list(mounts.keys())
        for item in store:
            msg = msg + item + " | " + str(mounts[item]) + "gp\n"
        await message.channel.send(msg)
    if message.content.startswith('$stock vehicles'):
        store = list(mounts.keys())
        for item in store:
            msg = msg + item + " | " + str(mounts[item]) + "gp\n"
        await message.channel.send(msg)


    #### Purchasing ####
    #Check if character has enough gold
    #Deduct gold if so
    #If magic item, remove from stock

    if message.content.startswith('$buy'):
        msg = ""
        name = []
        name = message.content.split()
        char = name[1]
        if char in characters:
            type = name[2]
            i = 0
            for n in name:
                if(i == 3):
                    item = n
                if(i > 3):
                    item = item + " " + n
                i = i + 1
            if(type == "magic"):
                if item in stock:
                    cost = stock[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        del stock[item]
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "armor"):
                if item in armor:
                    cost = armor[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "simple"):
                if item in simple:
                    cost = simple[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "martial"):
                if item in martial:
                    cost = martial[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "foci"):
                if item in foci:
                    cost = foci[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "items"):
                if item in nitems:
                    cost = nitems[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "packs"):
                if item in packs:
                    cost = packs[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "tools"):
                if item in tools:
                    cost = tools[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "gaming" or type == "instruments"):
                if item in gaming:
                    cost = gaming[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            elif(type == "mounts" or type == "vehicles"):
                if item in mounts:
                    cost = mounts[item]
                    bal = float(characters[char])
                    if(bal >= cost):
                        newbal = bal - cost
                        n = ("null", char, bal)
                        RemoveChar(n)
                        n = ("null", char, str(int(newbal)))
                        AddChar(n)
                        msg = "Thank you, " + char + ", for your purchase of " + item + ". You now have " + str(newbal) + " gp"
                    else:
                        msg = "Hey! " + char + " can't afford " + item + "."
                else:
                    msg = "Sorry, I don't have any " + item + " right now. Check back later."
            else:
                msg = "Sorry, I don't carry anything in the " + type + " category."
        else:
            msg = "Character not found."
        await message.channel.send(msg)





client.run('XXXX')

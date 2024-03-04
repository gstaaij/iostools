#!/usr/bin/env python3

import sqlite3

def printTable(table, padding):
    for i in range(len(table)):
        for j in range(len(table[i])):
            value = str(table[i][j])
            print(value + " " * (padding - len(value)), end="")
            if (j != len(table[i]) - 1):
                print(" | ", end="")
        print()

def main():

    print("Mr. Crab Savefile Patcher")
    print("Copyright \u00a9 2024 gstaaij")
    print("Licensed under the MIT License")
    print()

    connection = sqlite3.connect("./registry.db")

    cursor = connection.cursor()

    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    res = res.fetchall()
    try:
        res.index(("integerdata",))
    except ValueError:
        print("Please provide a valid registry.db")
        return 1

    res = cursor.execute("SELECT * FROM integerdata")
    res = res.fetchall()
    print("This is the state of the table before patching it:")
    printTable(res, 25)
    print()
    
    res = cursor.execute("SELECT value FROM integerdata WHERE key='LEVELPACK_8'")
    if (res.fetchone() != None):
        print("You have already patched this registry.db file")
        ans = input("Do you want to continue? [y/N] ")
        if (not ans.lower().startswith("y")):
            return 0
        print()

    # Set packs-locked to 0, so the first two packs are unlocked
    cursor.execute("UPDATE integerdata SET value=0 WHERE key='packs-locked';")

    for i in range(1, 9):
        res = cursor.execute("SELECT value FROM integerdata WHERE key='LEVELPACK_" + str(i) + "';")
        res = res.fetchone()        
        if (res != None):
            # If the entry already exists, set the value to 1 instead of making a new one
            cursor.execute("UPDATE integerdata SET value=1 WHERE key='LEVELPACK_" + str(i) + "';")
            continue
        
        # Add the ('LEVELPACK_{i}', 1) key-value pair to the table to unlock that level pack
        cursor.execute("INSERT INTO integerdata VALUES('LEVELPACK_" + str(i) + "', 1);")
    
    shownStarCostumeMessage = False
    starCostumes = { 1: "Leapy", 6: "Stinky" }
    for i in range(1, 9):
        res = cursor.execute("SELECT value FROM integerdata WHERE key='COSTUME_" + str(i) + "';")
        res = res.fetchone()
        if (res != None and res[0] == 1):
            # If the entry already exists, and the value is already set to 1, skip this one
            continue
        
        if (i in starCostumes.keys()):
            if (not shownStarCostumeMessage):
                shownStarCostumeMessage = True
                print()
                print("Leapy and Stinky are the only two crab costumes that can be unlocked without microtransactions.")
                print("Leapy can be bought for 12 stars. Stinky can be bought for 55 stars.")
                print("Each level gives you a maximum of 3 stars.")
            ans = input(f"Do you want to unlock {starCostumes[i]} now? [y/N] ")
            if (not ans.lower().startswith("y")):
                continue
        
        if (res != None):
            # If the entry already exists, set the value to 1 instead of making a new one
            cursor.execute("UPDATE integerdata SET value=1 WHERE key='COSTUME_" + str(i) + "';")
            continue

        # Add the ('COSTUME_{i}', 1) key-value pair to the table to unlock that crab costume
        cursor.execute("INSERT INTO integerdata VALUES('COSTUME_" + str(i) + "', 1);")

    print()
    print()

    res = cursor.execute("SELECT * FROM integerdata")
    res = res.fetchall()
    print("This is the state of the table after patching it:")
    printTable(res, 25)
    print()
    ans = input("Do you want to write these changes to registry.db? [Y/n] ")
    if (not ans.lower().startswith("n")):
        connection.commit()
    connection.close()
    return 0

if (__name__ == "__main__"):
    exit(main())

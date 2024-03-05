from .utilities.items import FindItem

class RuneBook:
    # Change the names / order in the array below to match the rune order in your runebook
    existing_rune_names = ['House', 'New Haven', 'Britian', 'Coventous', 'Destard']

    # Have either to True. Magery = Recall and Chivalry = Sacred Journey
    # magery = False
    # chivalry = True

    # Or use it like this if you want to make it more dynamic
    magery = Player.GetSkillValue('Magery') > 40
    chivalry = Player.GetSkillValue('Chivalry') > 40

    # Do not change the code below
    # ----------------------------
    runeNames = existing_rune_names + ['Empty'] * (8 - len(existing_rune_names))

    def __init__(self):
        self.rune_book = FindItem(0x22C5, Player.Backpack)

    def useRuneBook(self):
        Items.UseItem(self.rune_book)
        Gumps.WaitForGump(89, 10000)

    # Generate up to 8 useRune methods
    if chivalry:
        for i in range(1, 9):
            exec(f"def useRune{i}(self):" +
                f"\n    self.useRuneBook()" +
                f"\n    Misc.SendMessage('Ready yourself for your descent to {runeNames[i-1]}', 44)" +
                f"\n    Gumps.SendAction(89, {74 + i})")
    if magery:
        for i in range(1, 9):
            exec(f"def useRune{i}(self):" +
                f"\n    self.useRuneBook()" +
                f"\n    Misc.SendMessage('Ready yourself for your descent to {runeNames[i-1]}', 44)" +
                f"\n    Gumps.SendAction(89, {50 + i})")

        for i in range(1, 9):
            exec(f"def useGate{i}(self):" +
                f"\n    self.useRuneBook()" +
                f"\n    Misc.SendMessage('Prepare for gate travel to {runeNames[i]-1}', 44)" +
                f"\n    Gumps.SendAction(89, {100 + i})")

from Scripts.runebook_companion import RuneBook

mg = 500002
mk = 500003
state = True
btnID = 1
y_values = [40, 60, 80, 100, 120, 140, 160, 180]  # Distance between travel locations
bookOpen = False

runeBook = RuneBook()

def createRuneLocations(gd, y, BtnID, RuneName):
    if not RuneName == 'Empty':
        if runeBook.chivalry:
            Gumps.AddButton(gd, 40, y, 2224, 2224, BtnID, 1, 0)
            Gumps.AddLabel(gd, 65, y-3, 1150, RuneName)
        if runeBook.magery:
            Gumps.AddButton(gd, 40, y, 2224, 2224, BtnID, 1, 0)
            Gumps.AddButton(gd, 65, y, 2118, 2118, BtnID + 10, 1, 0)
            Gumps.AddLabel(gd, 85, y-3, 1150, RuneName)

def createBook():
    dimX = 80
    dimY = 80
    bk = Gumps.CreateGump(movable=True, closable=False)
    Gumps.AddPage(bk, 0)
    Gumps.AddBackground(bk, 0, 0, dimX, dimY, 9200)
    Gumps.AddHtml(bk, 30, 30, dimX - 40, dimY - 37, "", True, False)
    Gumps.AddButton(bk, 1, 1, 11056, 11056, 11, 1, 0)
    return bk

def createGump():
    gd = Gumps.CreateGump(movable=True, closable=False)
    Gumps.AddPage(gd, 0)

    if bookOpen:
        Gumps.AddBackground(gd, 0, 0, 65, 80, 9200)
        Gumps.AddAlphaRegion(gd, 0, 0, 65, 80)
        Gumps.AddButton(gd, 10, 15, 11056, 11056, 99, 1, 0)
    else:
        dimX = 200
        min_height = 130
        non_empty_rune_names = [name for name in runeBook.runeNames if name != 'Empty']
        dimY = max(len(non_empty_rune_names) * 30, min_height)
        Gumps.AddBackground(gd, 0, 0, dimX, dimY, 9200)
        Gumps.AddAlphaRegion(gd, 0, 0, dimX, dimY)
        Gumps.AddImage(gd, 3, 7, 30079)
        Gumps.AddHtml(gd, 30, 30, dimX - 40, dimY - 37, "", True, False)
        Gumps.AddButton(gd, dimX - 44, 10, 2435, 2435, 99, 1, 0)
        Gumps.AddButton(gd, dimX - 25, 10, 10006, 10006, 0, 1, 0)  # Close button
    return gd

def addTravelLocations(gd):
    for index, (runeName, y) in enumerate(zip(runeBook.runeNames, y_values)):
        createRuneLocations(gd, y, btnID + index, runeName)

def executeButtonAction(button_id):
    actions = {
        1: runeBook.useRune1,
        2: runeBook.useRune2,
        3: runeBook.useRune3,
        4: runeBook.useRune4,
        5: runeBook.useRune5,
        6: runeBook.useRune6,
        7: runeBook.useRune7,
        8: runeBook.useRune8,
        99: toggleGump,
        0: exit_gump
    }
    if runeBook.magery:
        actions[11] = runeBook.useGate1
        actions[12] = runeBook.useGate2
        actions[13] = runeBook.useGate3
        actions[14] = runeBook.useGate4
        actions[15] = runeBook.useGate5
        actions[16] = runeBook.useGate6
        actions[17] = runeBook.useGate7
        actions[18] = runeBook.useGate8

    action = actions.get(button_id)
    if action:
        action()


def starter():
    global state
    global bookOpen
    gd = createGump()
    if not bookOpen:
        addTravelLocations(gd)
    Gumps.SendGump(mg, Player.Serial, 50, 50, gd.gumpDefinition, gd.gumpStrings)
    Gumps.WaitForGump(mg, 700)
    gd = Gumps.GetGumpData(mg)
    executeButtonAction(gd.buttonid)


def exit_gump():
    global state
    state = False
    Gumps.CloseGump(mg)

def toggleGump():
    global bookOpen
    bookOpen = not bookOpen

while state:
    starter()

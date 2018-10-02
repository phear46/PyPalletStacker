# Pallet Calc Project

import math
import csv

# *******************************************************************************
# Define Class & Functions
# *******************************************************************************


class load:
    def __init__(self, idStr, length, width, height, weight, qty):
        self.id = idStr
        self.length = length
        self.width = width
        self.height = height
        self.weight = float(weight)
        self.qty = int(qty)


class pallet(load):  # REWRITE - DO NOT EXTEND LOAD
    pallet_count = 1

    def __init__(self, idStr, length, width, height, weight, qty):
        super().__init__(idStr, length, width, height, weight, qty)
        self.id = str(self.pallet_count)
        pallet.pallet_count += 1
        self.itemList = {}


def buildPallets():
    # Define and set the total number of items listed in the CSV
    # itemLeft is the counter for the while loop, loadTotalItems is a set number
    itemLeft = 0
    for line in loadList:
        itemLeft += line.qty
    loadTotalItems = itemLeft

    # Define & Set total weight of everything from the CSV
    loadTotalWeight = 0
    print('DEBUG: Just set loadTotalWeight to 0')
    for line in loadList:
        loadTotalWeight += line.weight * line.qty

    print('Total load weight is: ' + str(loadTotalWeight))
    print('Total items: ' + str(loadTotalItems))
    print()

    while itemLeft > 0:
        for line in loadList:

            emptyspace = 1200 - palletlist[-1].weight
            print('Empty weight on current pallet is: ' + str(emptyspace))

            if itemLeft > math.floor(emptyspace / line.weight):
                # print('DEBUG: IF called')
                # add what will fit on pallet
                emptyspace = 1200 - palletlist[-1].weight
                # need to say qtyTo use can only be UPTO the max availble fromt the actual line
                if line.qty < math.floor(emptyspace / line.weight):
                    qtyToUse = line.qty
                else:
                    qtyToUse = math.floor(emptyspace / line.weight)

                itemLeft -= qtyToUse
                line.qty -= qtyToUse

                palletlist[-1].itemList[line.id] = qtyToUse
                palletlist[-1].weight += line.weight * qtyToUse
            else:
                # print('DEBUG: Else called')
                # More space on this pallet than i can fill with the current line, put it all on

                palletlist[-1].itemList[line.id] = line.qty
                palletlist[-1].weight += line.weight * line.qty

                itemLeft -= line.qty
                line.qty -= line.qty

        print('Current pallet number: {}, itemList: {}, weight:{}'.format(len(palletlist), palletlist[-1].itemList, palletlist[-1].weight))

        print()
        print('Items left = ' + str(itemLeft))
        if itemLeft > 0:
            print('Create a new pallet')
            palletlist.append(pallet('id', 1220, 1220, 100, 0, 1))
        print()


# Open CSV and load items into a list
with open('load.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    loadList = []
    for line in csv_reader:
        loadList.append(load(line['id'], line['length'], line['width'], line['height'], line['weight'], line['qty']))
        print(line)
    print()

# Define the pallet list + create the first new pallet
    # this probably lives inside buildPallet()
palletlist = []
palletlist.append(pallet('id', 1220, 1220, 100, 0, 1))


buildPallets()

if palletlist[-1].weight == 0:
    palletlist.pop()

# Summarise pallets
for pal in palletlist:
    print('Pal#: ' + pal.id + ', Items:' + str(pal.itemList) + '   \t\tWeight: ' + str(pal.weight))


'''
TODO:
Re-write pallet class.
'''

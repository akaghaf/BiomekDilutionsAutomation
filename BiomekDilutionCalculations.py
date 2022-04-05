import random
import csv
from tkinter import E
import itertools
from os.path import exists
import os
import readline
from dilutions_lib import(
    yes_or_no,
    set_source_well,
    set_dest_well)
from time import sleep
from tqdm import tqdm

# Dictionary Keys
RES = 'Buffer'
SECTION = 1
SAMPLES = 'Samples'
DESTP = 'AssayPlate'

# Dependent Files
SOURCEWELL_FILE = './dependent_files/source_well.csv'
DESTWELL_FILE = './dependent_files/dest_well.csv'

# List initialization
# can we have more specific names for variables here?
# should be very descriptive of what all the variables are so anyone can understand
TRANSFER_VOLUME = []
BUFFER_VOLUME = []
ABSORBTION = []
DILUTION = []
DILUTION_NEW = []

def main():
    #main logic used to calculate dilutions

    sourcewell = set_source_well(SOURCEWELL_FILE)
    destwell = set_dest_well(DESTWELL_FILE)


    # function to tab complete the file names
    readline.set_completer_delims(' \t\n=')
    readline.parse_and_bind("tab: complete")

    valid_input = False
    while not valid_input:
        filenameinp = input("Enter the name of the input file exactly as it's written: ")

        valid_input  = exists(os.path.join(os.path.dirname(__file__),filenameinp))

        if not valid_input:
            if not yes_or_no("File not found, do you want to pick a different one? "):
                return


    valid_input = False
    output_specified = False
    while not output_specified:

        filenameoutp = input("Enter the name of the output file: ")

        valid_input  = exists(filenameinp)
        if filenameoutp == 'exit':
            return
        if not valid_input:
            print("File exists, you will overwrite this value if you continue ('exit' for termination)")
            if yes_or_no("Confirm"):
                output_specified = True
        else:
            output_specified = True

    with open(filenameinp) as f:
        f = f.read()
        f = f.replace("\n", ",")
        f = f.replace("\ufeff", "")
        f = f.split(",")

        for item in f:
            if item.startswith("0"):
                ABSORBTION.append(item)
            else:
                DILUTION.append(item)


        for position in range(0 ,len(ABSORBTION)):
            "use if/elif/else structure here its faster so you are not checking"
            " This does nothing if value is .3 or .6 decide where to be inclusive"
            if float(ABSORBTION[position]) <= 0.3:
                DILUTION_NEW.insert(position, int(DILUTION[position]) / 2)
            elif float(ABSORBTION[position]) >= 0.6:
                DILUTION_NEW.insert(position, (int(DILUTION[position]) * 2))
            elif (0.3 < float(ABSORBTION[position]) < 0.6):
                DILUTION_NEW.insert( position,(DILUTION[position]))


    for i in range(0,len(DILUTION_NEW)):
        TRANSFER_VOLUME.insert(i, ((100)/ float(DILUTION_NEW[i])))
    for itv in range(0, len(TRANSFER_VOLUME)):
        BUFFER_VOLUME.insert(itv, abs(100-float(TRANSFER_VOLUME[itv])))

    TVR = [round(num, 1) for num in TRANSFER_VOLUME]
    BVR = [round(num, 1) for num in BUFFER_VOLUME]


    TVI = [TVR[i:i+12] for i in range(0,len(TVR),12)]
    BVI = [BVR[i:i+12] for i in range(0,len(BVR),12)]
    TVF, BVF = [], []

    for element in range(0,12):
        TVF.extend([el[element] for el in TVI])
        BVF.extend([itm[element] for itm in TVI])

    with open(filenameoutp, 'w', newline = "") as csvofile:
        fieldnames = ['Reservoir', 'Section','SourcePlate', 'Source Well', 'DestPlate', 'Dest Well' ,'Transfer Volume', 'Buffer Volume']
        thewriter = csv.DictWriter(csvofile, fieldnames=fieldnames)
        thewriter.writeheader()
        #will need to change TVF if you change to the other way
        for val in range(0,len(TVF)):
            thewriter.writerow({'Reservoir': RES, 'Section' : SECTION, 'SourcePlate': SAMPLES,
                                'Source Well': sourcewell[val], 'DestPlate' : DESTP , 'Dest Well': destwell[val],
                                'Transfer Volume': TVF[val], 'Buffer Volume' : BVF[val] })

    # Progress bar to warn users of the progress of the program
    for i in tqdm(range(100)):
        sleep(.02 + random.randrange(0, 100)/1000 )

if __name__ == "__main__":
    main() 
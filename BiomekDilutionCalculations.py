
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

# Dictionary Keys
RES = 'Buffer'
SECTION = 1
SAMPLES = 'Samples'
DESTP = 'AssayPlate'

# Dependent Files
SOURCEWELL_FILE = './dependent_files/source_well.csv'
DESTWELL_FILE = './dependent_files/dest_well.csv'

# List initialization
TV = []
BV = []
ABSOLUTE = []
D = []
DN = []

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
                ABSOLUTE.append(item)
            else:
                D.append(item)


        for position in range(0 ,len(ABSOLUTE)):
            "use if/elif/else structure here its faster so you are not checking"
            " This does nothing if value is .3 or .6 decide where to be inclusive"
            if float(ABSOLUTE[position]) < 0.3:
                DN.insert(position, int(D[position]) / 2)
            elif float(ABSOLUTE[position]) > 0.6:
                DN.insert(position, (int(D[position]) * 2))
            elif (0.3 < float(ABSOLUTE[position]) < 0.6):
                DN.insert( position,(D[position]))


    for i in range(0,len(DN)):
        TV.insert(i, ((100)/ float(DN[i])))
    for itv in range(0, len(TV)):
        BV.insert(itv, abs(100-float(TV[itv])))

    TVR = [round(num, 1) for num in TV]
    BVR = [round(num, 1) for num in BV]



    #reordering everything because we did it wrong the first time
    # do it right the first time?
    At =TVR[:12]
    Bt =TVR[12:24]
    Ct =TVR[24:36]
    Dt =TVR[36:48]
    Et =TVR[48:60]
    Ft =TVR[60:72]
    Gt =TVR[72:84]
    Ht =TVR[84:96]
    Ab =BVR [:12]
    Bb =BVR [12:24]
    Cb =BVR [24:36]
    Db =BVR [36:48]
    Eb =BVR [48:60]
    Fb =BVR [60:72]
    Gb =BVR [72:84]
    Hb =BVR [84:96]

    TVI = [At, Bt, Ct, Dt, Et, Ft, Gt, Ht]
    BVI = [Ab, Bb, Cb, Db, Eb, Fb, Gb, Hb]
    TVF = []
    BVF = [] 
    for element in range(0,12):
        TVF.extend([el[element] for el in TVI])
        BVF.extend([itm[element] for itm in TVI])

    #counter that can be used to make sure right output of values
    counter = 0

    with open(filenameoutp, 'w', newline = "") as csvofile:
        fieldnames = ['Reservoir', 'Section','SourcePlate', 'Source Well', 'DestPlate', 'Dest Well' ,'Transfer Volume', 'Buffer Volume']
        thewriter = csv.DictWriter(csvofile, fieldnames=fieldnames)
        thewriter.writeheader()
        #will need to change TVF if you change to the other way
        for val in range(0,len(TVF)):
            counter += 1
            thewriter.writerow({'Reservoir': RES, 'Section' : SECTION, 'SourcePlate': SAMPLES,
                                'Source Well': sourcewell[val], 'DestPlate' : DESTP , 'Dest Well': destwell[val],
                                'Transfer Volume': TVF[val], 'Buffer Volume' : BVF[val] })


if __name__ == "__main__":
    main()
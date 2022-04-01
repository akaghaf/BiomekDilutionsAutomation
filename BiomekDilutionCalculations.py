
import csv
from tkinter import E
import itertools
from os.path import exists
import os



SOURCEWELL = ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
              'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
              'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
              'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
              'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
              'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
              'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
              'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
              'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
              'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
              'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
              'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5']

DESTWELL = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
           'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
           'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
           'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
           'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
           'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
           'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
           'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
           'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9',
           'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10',
           'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11',
           'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12']



def yes_or_no(question):
    # Brief: Used to ask a user a yes or no question
    # param question: question to ask the user
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False


def main():
    #main logic used to calculate dilutions

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

        Abs = []
        D = []
        DN = []
        for item in f:
            if item.startswith("0"):
                Abs.append(item)
            else:
                D.append(item)


        for position in range(0 ,len(Abs)):
            "use if/elif/else structure here its faster so you are not checking"
            " This does nothing if value is .3 or .6 decide where to be inclusive"
            if float(Abs[position]) < 0.3:
                DN.insert(position, int(D[position]) / 2)
            if float(Abs[position]) > 0.6:
                DN.insert(position, (int(D[position]) * 2))
            if (0.3 < float(Abs[position]) < 0.6):
                DN.insert( position,(D[position]))

    TV = []
    BV = []
    for i in range(0,len(DN)):
        TV.insert(i, ((100)/ float(DN[i])))
    for itv in range(0, len(TV)):
        BV.insert(itv, abs(100-float(TV[itv])))

    TVR = [round(num, 1) for num in TV]
    BVR = [round(num, 1) for num in BV]

    #counter that can be used to make sure right output of values
    countr = 0

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

    res = 'Buffer'
    section = 1
    samples = 'Samples'
    destp = 'AssayPlate'

    with open(filenameoutp, 'w', newline = "") as csvofile:
        fieldnames = ['Reservoir', 'Section','SourcePlate', 'Source Well', 'DestPlate', 'Dest Well' ,'Transfer Volume', 'Buffer Volume']
        thewriter = csv.DictWriter(csvofile, fieldnames=fieldnames)
        thewriter.writeheader()
        #will need to change TVF if you change to the other way
        print(len(TVF))
        for val in range(0,len(TVF)):
            countr += 1
            thewriter.writerow({'Reservoir': res, 'Section' : section, 'SourcePlate': samples,
                                'Source Well': SOURCEWELL[val], 'DestPlate' : destp , 'Dest Well': DESTWELL[val],
                                'Transfer Volume': TVF[val], 'Buffer Volume' : BVF[val] })


if __name__ == "__main__":
    main()
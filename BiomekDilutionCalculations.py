import csv
from tkinter import E
import itertools
filenameinp = input("Enter the name of the file exactly as it's written")
filenameoutp = input("Enter the output name of the file you want with .csv at the end")
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

countr = 0

#reordering everything because we did it wrong the first time
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
for p in range(len(TVI)):
    TV1 = [el[0] for el in TVI]
    BV1 = [itm[0] for itm in BVI]
    TV2 = [el[1] for el in TVI]
    BV2 = [itm[1] for itm in BVI]
    TV3 = [el[2] for el in TVI]
    BV3 = [itm[2] for itm in BVI]
    TV4 = [el[3] for el in TVI]
    BV4 = [itm[3] for itm in BVI]
    TV5 = [el[4] for el in TVI]
    BV5 = [itm[4] for itm in BVI]
    TV6 = [el[5] for el in TVI]
    BV6 = [itm[5] for itm in BVI]
    TV7 = [el[6] for el in TVI]
    BV7 = [itm[6] for itm in BVI]
    TV8 = [el[7] for el in TVI]
    BV8 = [itm[7] for itm in BVI]
    TV9 = [el[8] for el in TVI]
    BV9 = [itm[8] for itm in BVI]
    TV10 = [el[9] for el in TVI]
    BV10 = [itm[9] for itm in BVI]
    TV11 = [el[10] for el in TVI]
    BV11 = [itm[10] for itm in BVI]
    TV12 = [el[11] for el in TVI]
    BV12 = [itm[11] for itm in BVI]

TV1.extend(TV2)
TV1.extend(TV3)
TV1.extend(TV4)
TV1.extend(TV5)
TV1.extend(TV6)
TV1.extend(TV7)
TV1.extend(TV8)
TV1.extend(TV9)
TV1.extend(TV10)
TV1.extend(TV11)
TV1.extend(TV12)

BV1.extend(BV2)
BV1.extend(BV3)
BV1.extend(BV4)
BV1.extend(BV5)
BV1.extend(BV6)
BV1.extend(BV7)
BV1.extend(BV8)
BV1.extend(BV9)
BV1.extend(BV10)
BV1.extend(BV11)
BV1.extend(BV12)

res = 'Buffer'
section = 1
samples = 'Samples'
destp = 'AssayPlate'
destwell = []
sourcewell = ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5']
destwel = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12']



with open(filenameoutp, 'w', newline = "") as csvofile:
    fieldnames = ['Reservoir', 'Section','SourcePlate', 'Source Well', 'DestPlate', 'Dest Well' ,'Transfer Volume', 'Buffer Volume']
    thewriter = csv.DictWriter(csvofile, fieldnames=fieldnames)
    thewriter.writeheader()
    for val in range(0,len(TV1)):
        countr += 1
        thewriter.writerow({'Reservoir': res, 'Section' : section, 'SourcePlate': samples, 'Source Well': sourcewell[val], 'DestPlate' : destp , 'Dest Well': destwel[val],'Transfer Volume': TV1[val], 'Buffer Volume' : BV1[val] })


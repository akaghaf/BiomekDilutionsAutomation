# BiomekDilutionsAutomation
## About the program

This program takes two 8 by 12 csv's and outputs an instructional csv for the Biomek machine.
The first csv must be the absorbance rates of each well in decimal places, with empty wells having placeholders.
There should be no column headers or row titles. Just numerical values organized in a 8 by 12 csv, and placeholders for empty csv's.
The absorbance values must start with a "0." to differentiate them from other data types.
The second csv should have the dilution values with empty wells having placeholders. 

## How to Run

Program is easily run:
```python
python3 BiomekDilutionCalculations.py
```
### Choosing files for input/output

The program takes a csv as an input, the input is validated that the file can be found.
Additionally we have included the option to autocomplete the file names:
```
Enter the name of the input file exactly as it's written: <tab> <tab>
  dependent_files/               input.csv                      tester.py
BiomekDilutionCalculations.py    dilutions_lib.py               output                         
Enter the name of the input file exactly as it's written: in<tab>
Enter the name of the input file exactly as it's written: input.csv
```
This holds true for the output as well.


## Result/Purpose

Sample of output:

```bash
Reservoir,Section,SourcePlate,Source Well,DestPlate,Dest Well,Transfer Volume,Buffer Volume
Buffer,1,Samples,A6,AssayPlate,A1,50.0,50.0
Buffer,1,Samples, B6,AssayPlate, B1,50.0,50.0
Buffer,1,Samples, C6,AssayPlate, C1,100.0,100.0
```
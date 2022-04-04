# BiomekDilutionsAutomation
## About the program

Describe the program here

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

## Sample of Input
The input is in the form of a csv:

```csv
0.732,0.7401,0.3293,0.3245,0.4275,0.4281,0.4736,0.4688,0.4755,0.4772,0.4987,0.5078
0.6318,0.5255,0.3172,0.3164,0.4351,0.4471,0.4309,0.4439,0.3274,0.324,0.4021,0.4008
0.5506,0.3949,0.3161,0.3167,0.4685,0.4696,0.4088,0.4112,0.6426,0.6663,0.637,0.637
```


## Result/Purpose

Sample of output:

Reservoir|Section|SourcePlate|Source Well|DestPlate|Dest Well|Transfer Volume|Buffer Volume
---------|-------|-----------|-----------|---------|---------|----------------|------------
Buffer|1|Samples|A6|AssayPlate|A1|50.0|50.0|
Buffer|1|Samples| B6|AssayPlate| B1|50.0|50.0
Buffer|1|Samples| C6|AssayPlate| C1|100.0|100.0

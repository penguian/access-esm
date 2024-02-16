#!/bin/env python3
import argparse
import mule

parser = argparse.ArgumentParser(
        prog='fix_esm15_restart',
        description='Remove corrupted fields from restart files')

parser.add_argument('input_filename')
parser.add_argument('output_filename')
args = parser.parse_args()

in_data = mule.load_umfile(args.input_filename)

out_data = in_data.copy()
'''
Fields to be removed as per ~access/umdir/vn7.3/ctldata/STASHmaster/STASHmaster_A
 |Model |Sectn | Item |Name                                |
1|    1 |    0 |  151 |RIVER SEQUENCE                      |
1|    1 |    0 |  152 |RIVER DIRECTION                     |
1|    1 |    0 |  153 |RIVER WATER STORAGE               M2|
1|    1 |    0 |  155 |ACCUMULATED SURFACE RUNOFF     KG/M2|
1|    1 |    0 |  156 |ACCUMULATED SUB-SURFACE RUNOFF KG/M2|
1|    1 |    3 |  100 |FLUX OF TRACER 1 IN BL              |
1|    1 |    3 |  101 |FLUX OF TRACER 2 IN BL              |
1|    1 |    3 |  326 |CO2 LAND SURFACE FLUX     KG/M**2/S |
1|    1 |   33 |    1 |ATM TRACER  1               AFTER TS|
1|    1 |   33 |    2 |ATM TRACER  2               AFTER TS|
'''
for f in in_data.fields:
    if f.lbuser4 not in [151,152,153,155,156,3100,3101,3326,33001,33002]:
        out_data.fields.append(f)

out_data.validate = lambda *args, **kwargs: True
out_data.to_file(args.output_filename)


%
O10064;
(Program: Gearbox Plate)
(Date: 2016-04-07)
(Drawing Number: CNMC1005-L6)
(Revision Number: 0)
(Machine: )
(Material: 6061 T6 Al 1/2" x 4" x 6")
(Material Hardness: 100Bhn)
(Operation: 1 of 1)
(Programmer: Stephane Drouin-Moreland)
G54 G00 G17 G20 G40 G49 G90 G94 G98;

G28;

(Operation: End Mill First End)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 1/2 x 1/2 HSS 2fl End Mill)
(RPM: 7500)
(IPM: 61.5)

T05 M06;
S7500 M03;

G00 G54 X5.0 Y-1.0;
G43 H05 Z1.0;

Z-0.75 M08;
G01 G41 D05 Y0 F61.5;

X-0.5;

G40 Y-1.0 M09;
G00 Z1.0 M05;

G53 Z0;
G53 Y0;

M00;
T13 M06;

(Remove part from vice)

G00 X2.0 Y6.187; (6.0 + Dowel pin radius)
G43 H09 Z-0.5;

M00;

(Flip part and return to vice)

Y6.5;
G53 Z0;

M01;
T6 M06;

(Operation: End Mill Second End)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 1/2 x 1/2 HSS 2fl End Mill)
(RPM: 7500)
(IPM: 61.5) 

T05 M06;
S7500 M03;

G00 X5.0 Y-1.0;
G43 H05 Z1.0;

Z-0.75 M08;
G01 G41 D05 Y0 F61.5;

X-0.5;

G40 Y-1.0 M09;
G00 Z1.0 M05;

G53 Z0;
G53 Y0;

M01;
T3 M06;

(Operation: Face Part)
(Holder: C-Style Arbor)
(Cutting Unit: 3.0 CoroMill 245 6fl)
(RPM: 3247)
(IPM: 175.33)

S3247 M03;

G00 X3.0 Y-1.52;
G43 H07 Z1.0;
Z0;

G01 X2.0 F175.33;
G02 R1.5 X0.5 Y-0.02;
G01 Y4.0;
G02 R1.5 X3.5;
G01 Y-5.0;

G00 G53 Z0;
G53 Y0;

M00;
T13 M06;

(Remove part from vice)

G00 X2.0 Y-0.187; (- Dowel pin radius)
G43 H09 Z-0.5;

M00;

(Datum A down, Datum C against the fixed jaw, Datum B against the pin)

Y-0.5;
G53 Z0;

M01;
T06 M06;

(Operation: Spot Drill)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 3/4 90° Spot Drill)

S499 M03;

G00 X2.0 Y4.5;
G43 H06 Z1.0 M08;

G82 G98 Z-0.345 P0.25 R0.1 F4.24;
G80;

S1348;
G82 Z-0.14 P0.25 R0.1 F5.47 L0;
G70 I0.75 J60.0 L3

S874;
G82 X0.75 Y0.75 Z-0.215 P0.25 R0.1 F4.45;
X3.25;
Y5.25;
X0.75;
G80;

S998;
G82 X1.0 Y1.5 Z-0.175 P0.25 R0.1 F5.49;
X3.0 Y2.63;
G80 M09;

G53 Z0;

M01;

(Operation: Drill Various)
(Holder: Precision Drill Chuck)
(Cutting Unit: 5/8 Jobber Drill)
(RPM: 599)
(IPM: 7.55)
(Cutting Unit: "C" Jobber Drill)
(RPM: 1547)
(IPM: 10.52)
(Cutting Unit: 5/16 Jobber Drill)
(RPM: 1198)
(IPM: 10.42)

T07 M06;
S599 M03;
G00 X2.0 Y4.5;
G43 H07 Z1.0 M08;
G81 G98 Z-0.7878 R0.1 F7.55;
G80 M09;

T08 M06;
S1547 M03;
G00 X2.0 Y4.5;
G43 H07 Z1.0 M08;
G81 Z-0.6727 R0.1 F10.52 L0;
G70 I0.75 J60.0 L3
G80 M09;

T10 M06;
S1198 M03;
G00 X0.75 Y0.75;
G43 H10 Z1.0 M08;
G81 Z-0.6939 R0.1 F10.42;
X3.25;
Y5.25;
X0.75;
X1.0 Y1.5;
X3.0 Y2.63;
G80 M09;

G53 Z0;

M01;
T11 M06;

(Operation: Tap Holes)
(Holder: Rigid Tapping Head)
(Cutting Unit: 3/8-16UNC-2B Tap)
(RPM: 1171)
(IPM: 73.21)

G00 X2.0 Y4.5;
G43 H11 Z1.0 M08;
G84 Z-0.600 R0.1 F73.21 S1171 L0;
G70 I0.75 J60.0 L3
G80 M09;

G53 Z0;

M00;
T13 M06;

(Remove part from vice)

G00 X2.0 Y6.187; (- Dowel pin radius)
G43 H09 Z-0.5;

M00;

(Datum A up, Datum C against the fixed jaw, Datum B against the pin)

Y6.5;
G53 Z0;

M01;

(Operation: Drill Square Pocket Start)
(Holder: Precision Drill Chuck)
(Cutting Unit: 5/8 Jobber Drill)
(RPM: 599)
(IPM: 7.55)

T07 M06;
S599 M03;

(Y|G55| = Y|G54| + 6.0)
G00 G55 X2.0 Y-2.0625;
G43 H07 Z1.0 M08;

G81 G98 Z-0.37 R0.1 F4.24;

G53 Z0;

M01;

(Operation: Mill Circular Pocket)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 1/2 x 1/2 HSS 2fl End Mill)
(RPM: 7500)
(IPM: 61.5)

T05 M06;
S7500 M03;

G00 X2.0 Y-5.8;
G43 H05 Z1.0 M08;

G13 D05 I0.56 K1.0625 Q0.25 Z0.2 F61.5;

(Operation: Mill Square Pocket)

G00 X2.0 Y-2.0625;

G83 Z-0.38 R-0.19 Q0.05 P0.25 F61.5;

Z0.1;
G01 Z-0.25 F61.5;

M98 P10065 L1;



O10065;

(Square Pocket Mill Rough)

G91;

G03 I0.125 J0 X0.25 F61.5;
G03 I-0.25 J0 X-0.25 Y-0.25;



















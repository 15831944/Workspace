%
O20061
(Program: Adapter Flange) 
(Date: 2016-04-21) 
(Drawing Number: CNMC1006-PE1) 
(Revision Number: 1) 
(Machine: ) 
(Material: 6061 T6 Al 1/2" x 4" x 6") 
(Material Hardness: 100Bhn) 
(Operation: 1 of 1) 
(Programmer: Stephane Drouin-Moreland) 

G54 G00 G17 G20 G40 G49 G90 G94 G98;

G28;

T03 M06;

(Operation: Face Part)
(Holder: C-Style Arbor)
(Cutting Unit: 3.0 CoroMill 245 6fl)
(RPM: 3247)
(IPM: 175.33)

S3247 M03;

G00 G54 X3.2 Y-1.52;
G43 H03 Z1.0;
Z0;

G01 X2.2 F175.33;
G02 R1.5 X0.7 Y-0.02;
G01 Y2.0;
G02 R1.4 X3.5;
G01 Y-2.0;

G00 G53 Z0;

M01;
T06 M06;

(Operation: Spot Drill)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 3/4 90B0 Spot Drill)
(RPM: 832)
(IPM: 4.74)

S832 M03;

G00 X2.0 Y2.0;
G43 H06 Z0.5 M08;

G82 G98 Z-0.225 P0.25 R0.1 F4.74;
G70 I1.5 J15.0 L6;
G80;

G00 G53 Z0 M09;
G53 Y0;

M01;
T07 M06;

(Operation: 37/64 Drill)
(Holder: Precision Drill Chuck)
(Cutting Unit: 37/64 Jobber Drill)
(RPM: 648)
(IPM: 7.55)

S648 M03;

G00 X2.0 Y2.0;
G43 H07 Z0.5 M08;

G81 G98 Z-0.7878 R0.1 F7.55;
G80;

G00 G53 Z0 M09;
G53 Y0;

M01;
T10 M06;

(Operation: 5/16 Drill)
(Holder: Precision Drill Chuck)
(Cutting Unit: 5/16 Jobber Drill) 
(RPM: 1198) 
(IPM: 10.42) 

S1198 M03;

G00 X2.0 Y2.0;
G43 H10 Z0.5 M08;

G81 G98 Z-0.6939 R0.1 F10.42 L0;
G70 I1.5 J15.0 L6;
G80;

G00 G53 Z0 M09;

M01;
T11 M06;

(Operation: Tap Holes) 
(Holder: Rigid Tapping Head) 
(Cutting Unit: 3/8-16UNC-2B Tap) 
(RPM: 1171) 
(IPM: 73.21)

G00 X2.0 Y2.0;
G43 H11 Z0.5 M08;

G84 Z-0.9 R0.1 F73.21 S1171 L0;
G70 I1.5 J195.0 L3;
G80;

G00 G53 Z0 M09;

M01;
T05 M06;

(Operation: End Mill Operations)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 1/2 x 1/2 HSS 2fl End Mill)
(RPM: 7500)
(IPM: 61.5)

(Bore 1.98 Hole)

S7500 M03;

G00 X2.0 Y2.0;
G43 H05 Z0.5 M08;

G13 G98 D05 I0.56 K0.97 Q0.15 Z-0.5 F61.5;

G00 Y3.0;
G01 G41 D05 Y2.0;

G00 Z-0.5;
G03 I-0.495 J0 X1.01;
G03 I0.99 J0;
G03 I0.495 J0 X2.0;

G00 Z0.5;

(Mill Contour)

X1.75 Y4.082;
Z-0.118;
G03 I0.25 J0 X2.0 Y3.832 F61.5;
G01 X3.622;
G02 I0 J-0.21 X3.832 Y3.642;
G01 Y0.378;
G02 I-0.21 J0 X3.642 Y0.168;
G01 X0.378
G02 I0 J0.21 X0.168 Y0.358;
G01 Y3.622;
G02 I0.21 J0 X0.378 Y3.832;
G01 X2.1;
G03 I0 J0.25 X2.35 Y4.082;

G00 Y4.5;
X1.75;
Y4.082;

G01 Y4.062;
G03 I0.25 J0 X2.0 Y3.812 F61.5;
G01 X3.622;
G02 I0 J-0.19 X3.812 Y3.622;
G01 Y0.378;
G02 I-0.19 J0 X3.642 Y0.188;
G01 X0.378
G02 I0 J0.19 X0.188 Y0.378;
G01 Y3.622;
G02 I0.19 J0 X0.378 Y3.812;
G01 X2.1;
G03 I0 J0.25 X2.35 Y4.062;
G01 Y4.062;

G01 G40 Y5.0;
G00 G53 Z0 M09;

M01;
T12 M06;

(Operation: Chamfer Edges)
(Holder: Short ER32 Collet Chuck)
(Cutting Unit: 8mm CoroMill Plura Chamfering End Mill)
(RPM: 7500)
(IPM: 30.0)
(-0.050 - Chamfer Width - Depth)
(Set tool diameter offset to 0.1)

S7500 M03;

G00 X2.0 Y3.0;
G43 H12 Z0.5 M08;
G01 G41 D12 Y2.0 F30.0;

G00 Z-0.09;
G03 I-0.495 J0 X1.01;
G03 I0.99 J0;
G03 I0.495 J0 X2.0;

G00 Z0.5;

X2.25 Y4.5;

Z-0.0656;
X1.75;
Y4.062
G03 I0.25 J0 X2.0 Y3.812 F30.0;
G01 X3.622;
G02 I0 J-0.19 X3.812 Y3.622;
G01 Y0.378;
G02 I-0.19 J0 X3.642 Y0.188;
G01 X0.378
G02 I0 J0.19 X0.188 Y0.378;
G01 Y3.622;
G02 I0.19 J0 X0.378 Y3.812;
G01 X2.1;
G03 I0 J0.25 X2.35 Y4.062;

G01 G40 Y5.0;
G00 G53 Z0 M09;

M30;
%
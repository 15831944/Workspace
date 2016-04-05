%
O10063
(Program: Weld-On Thread Adapter)
(Date: 2016-03-17)
(Drawing Number: CNMC1005-D7)
(Revision Number: A)
(Machine: )
(Material: Pre-machined part)
(Material MC Code: P1.2.Z.AN)
(Material Hardness: 150Bhn)
(Fixturing: Soft jaws)
(Operation: 4 of 4)
(Setup Instructions:)
(Programmer: Stephane Drouin-Moreland)

G20 G40 G80 G99;

G50 S4000;

G28;
T0101;

(Operation: Rough Face and OD)
(Clamping Unit ID: )
(Cutting Unit ID: C4-DCLNR 27050-12)
(Insert ID: CNMG-432 PM 4325)
(Vc: 990sfm)
(Fn: 0.05-0.0118in/rev)

(Rough face)
G96 S990 M03;
G00 G54 X2.1 Z1.0;
Z0.5 M08;
G72 P01 Q02 D0.079 W0.0156 F0.0118;	
	N01;
	G00 Z0;
	G01 X1.05  F0.004;
	Z0.1
	N02;

(Rough OD)
G00 X2.1 Z0.1;
G71 P03 Q04 D0.079 U0.0313 F0.0118;
	N03;
	G01 G42 X1.6322 W0 F0.004;
	Z0;
	X1.7522 Z-0.06;
	Z-0.7068;
	X1.6 Z-0.87;
	Z-1.12;
	X1.9 Z-1.4417;
	G40 X2.1;
	N04;

G28 X2.1 M09;
G28;
M01;

G28;
T0303;

(Operation: Finish Face and OD)
(Clamping Unit ID: )
(Cutting Unit ID: C4-DDJNR-27050-11)
(Insert ID: DNMG-331 PF 4325)
(Vc: 990)
(Fn: 0.004)

(Finish Face and OD cycles)
G96 S990 M03;
G00 G54 X2.1 Z1.0;
Z0.1 M08;
(Finish cycle facing)
G70 P01 Q02;

X2.1 Z0.1;
(Finish cycle OD)
G70 P03 Q04;

G28 X3.0 M09;
G28;
M01;

G28;
T0505;

(Operation: Finish ID)
(Clamping Unit ID: )
(Cutting Unit ID: C4-SCLCR-13080-09)
(Insert ID: CCMT 3|2.5|1 PF4225)
(Vc: 990)
(Fn: 0.0043)

(Finish ID)
G96 S990 M03;
G00 G54 X2.1 Z1.0;
Z0.1 M08;
(Finish cycle ID)
X1.24;
G01 G41 Z0 F0.004;
X1.16 Z-0.04;
Z-1.91;
X1.0;
G00 G40 Z0.1;

G28 X3.0 M09;
G28;
M01;

G28;
T0707;

(Operation: Thread)
(Clamping Unit ID: )
(Cutting Unit ID: C4-266RFG-27050-16)
(Insert ID: 266RG-16UN01C120M)
(Vc: 640)
(RPM: 1397)
(Fn: 0.083333)

(Thread)
G97 S1397 M03;
G00 G54 X2.1 Z1.0;
Z0.2492 M08;

G92 X1.7258 Z-1.0 F0.083333;
X1.7073;
X1.6903;
X1.6773;
X1.6664;
X1.6567;
X1.6480;

G80;

G28 X3.0 M09;
G28;
M01;

G28;
T0909;

(Operation: Clip thread)
(Clamping Unit ID: )
(Cutting Unit ID: C4-RF123G20-27060B)
(Insert ID: N123G2-0310-0002-GF 1125)
(Vc: 620)
(RPM: 1353)
(Fn: 0.083333)

(Clip Thread)
G97 S1353 M03;
G00 G54 X2.1 Z1.0;
Z0.3042 M08;

(Front)
X1.7140;
G32 Z-0.0283 F0.083333;
X1.8 Z-0.0713;
G00 Z0.3042;

X1.6857;
G32 Z-0.0283 F0.083333;
X1.8 Z-0.0855;
G00 Z0.3042;

X1.6598;
G32 Z-0.0283 F0.083333;
X1.8 Z-0.0984;
G00 Z0.3042;

X1.6400;
G32 Z-0.0283 F0.083333;
X1.8 Z-0.1084;
G80;

(Back)
G00 X1.8 Z-0.7444;
X1.7482;
G32 X1.7140 Z-0.7811 F0.083333;
Z-1.0;
G00 X1.8;

Z-0.7141;
X1.7482;
G32 X1.6857 Z-0.7811 F0.083333;
Z-1.0;
G00 X1.8;

Z-0.6863;
X1.7482;
G32 X1.6598 Z-0.7811 F0.083333;
Z-1.0;
G00 X1.8;

Z-0.6650;
X1.7482;
G32 X1.6400 Z-0.7811 F0.083333;
Z-1.0;
G00 X1.8;

G28 X3.0 M09;
G28;
M01;

G28;
T0707;

(Operation: Thread - final pass)
(Clamping Unit ID: )
(Cutting Unit ID: C4-266RFG-27050-16)
(Insert ID: 266RG-16UN01C120M)
(Vc: 640)
(RPM: 1397)
(Fn: 0.083333)

(Thread - final pass)
G97 S1397 M03;
G00 G54 X2.1 Z1.0;
Z0.2492 M08;

G92 X1.64 Z-1.0 F0.083333;

G28 X3.0 M09;
G28;
M30;
%
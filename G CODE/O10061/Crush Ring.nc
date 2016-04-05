%
O10061
(Program: Weld-On Thread Adapter)
(Date: 04/03/2016)
(Drawing Number: CNMC1005-D7)
(Revision Number: A)
(Machine: )
(Material: 1045 T&G, 2" Diameter x Bar)
(Material MC Code: P1.2.Z.AN)
(Material Hardness: 150Bhn)
(Fixturing: Hard Jaws)
(Operation: 2 of 4)
(Setup Instructions: )
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
G00 G54 X3.0 Z1.0;
X2.1 Z0.1 M08;
G72 P01 Q02 D0.05 W0.0156 F0.0118;	
	N01;
	G00 Z0;
	G01 X-0.0625;
	N02;

(Rough OD)
G71 P03 Q04 D0.118 U0.0313 F0.0118;
	N03;
	G00 G42 X1.51;
	G01 Z0;
	G03 R0.045 X1.600 Z-0.045;
	G01 Z-.60
	X2.0;
	G40 X2.1;
	N04;
G28 X3.0 W0 M09;
M01;

G28;
T0303;

(Operation: Drill and Rough ID)
(Clamping Unit ID: )
(Cutting Unit ID: 880-D2600C4-03)
(Insert ID: 880-05 03 05H-C-LM 1044, 880-05 03 W08H-P-LM 4044)
(Vc: 493)
(Fn: 0.0045)

(Drill)
G97 S1720 M03;
G00 X3.0 Z1.0 M08;
G81 X0.0708 Z-0.60 R0.1 F0.0045;
G80;
G28 X3.0 W0 M09;
M01;

G28;
T0303;

(Rough ID)
G96 S493 M03;
G00 G54 X3.0 Z1.0;
X0 M08;
G71 P05 Q06 D0.088 U-0.04 F0.0045;	(Fix DOC)
	N05;
	G00 G41  Z0.1
	X1.235;
	G01 Z0;
	X1.175 Z-0.030;
	Z-.60
	G40 X1.175;
	N06;
G28 X3.0 W0 M09;
M01;

G28;
T0505;

(Operation: Finish Face and OD)
(Clamping Unit ID: )
(Cutting Unit ID: C4-DDJNR-27050-11)
(Insert ID: DNMG-331 PF 4325)
(Vc: 990)
(Fn: 0.0040)

(Finish Face and OD cycles)
G96 S990 M03;	(Bump up SFM?)
G00 G54 X3.0 Z1.0;
X2.1 Z0.1 M08;

(Finish cycle facing)
G70 P01 Q02 F0.0040;

(Finish cycle OD)
G70 P03 Q04 F0.0040;
G28 X3.0 W0 M09;
M01;

G28;
T0101;

(Operation: Finish ID)
(Clamping Unit ID: )
(Cutting Unit ID: 880-D2600C4-03)
(Insert ID: 880-05 03 05H-C-LM 1044, 880-05 03 W08H-P-LM 4044)
(Vc: 493)
(Fn: 0.0045)

(Finish ID cycle)
G97 S1618 M03;
G00 G54 X3.0 Z1.0;
X2.1 Z0.1 M08;

(Finish cycle ID)
G70 P05 Q06 F0.007;
G28 X3.0 W0 M09;
M01;

G28;
T0707;

(Operation: Part Off)
(Clamping Unit ID: )
(Cutting Unit ID: C4-RF123G20-27060B)
(Insert ID: N123G1-0300-0002-CM 2135)
(Vc: 438)
(Fn: 0.004)

(Part off)
G96 S438 M03;
G00 G54 X3.0 Z1.0;
G42 X2.1 Z-0.51 M08;
G01 X1.55 F0.0040;
G00 X1.7;
Z-0.48;
G01 X1.6;
X1.54 Z-0.51;
X1.175;
G00 G40 X2.1;
G28 X3.0 W0 M09;
M30;
%
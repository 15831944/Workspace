%
O10065;

(Lathe Practical)
(Drawing Number CNCM1006-PE3)
(Revision Number: 1)
(Programmer: Stephane Drouin-Moreland)

G20 G40 G80 G99;

G50 S4000

G28;
T0101;

(Operation: Rough Face and OD)
(Cutting Unit ID: C4-DDJNR-207050-12)
(Insert ID: DNMG-332 PM4325)
(Vc: 1150sfm)
(Fn: 0.0118in/rev)

(Rough Face)
G96 S1150 M03;
G00 G54 Z1.0;
X3.6;

Z0.05 M08;
G72 P01 Q02 D0.0313 W0.0156 F0.0118;
	N01;
	G00 Z0;
	G01 X2.0 F0.004
	Z0.05;
	N02;

(Rough OD)
G71 P03 Q04 D0.079 U0.0313 F0.0118;
	N03;
	G01 G42 X2.761 W0 F0.004;
	Z0;
	G03 R0.02 X2.801 Z-0.02;
	G01 Z-0.3916;
	G02 R0.0313 X2.8094 Z-0.4073;
	G01 X3.004 Z-0.5758;
	Z-1.3938;
	X2.9109 Z-1.4937;
	G02 R0.0313 X2.905 Z-1.5069;
	G01 Z-1.9187;
	G02 R0.0313 X2.9676 Z-1.95;
	G01 X3.093;
	X3.125 Z-1.966;
	Z-2.9687;
	G02 R0.0313 X3.1876 Z-3.0;
	G01 X3.4688;
	G03 R0.0156 X3.5 Z-3.0156;
	G00 X3.6;
	N04;

G28 G40 X3.6 M09;
G28;
M01;

G28;
T0707;

(Operation: Rough ID)
(Cutting Unit ID: C4-SCLCR-13080-09)
(Insert ID: CCMT 3|2.5|2 PF4225)
(Vc: 1150sfm)
(Fn: 0.0059in/rev)

G96 S1150 M03;
G00 Z1.0;
X2.0 M08;
G71 P05 Q06 D0.06 U-0.0626 F0.0059;
	N05;
	G00 G41 X2.47;
	G01 Z0 F0.0056;
	G02 R.035 X2.4 Z-.035;
	G01 Z-.375;
	X2.2622;
	G02 R.0156 X2.2299 Z-.3901;
	G01 X2.1265 Z-1.8711;
	X2.0;
	N06;

G00 G40 Z1.0;
G28 X3.6 M09;
G28;
M01;

G28;
T0303;

(Operation: Finish Face and OD)
(Cutting Unit ID: C4-DDJNR-207050-12)
(Insert ID: DNMG-332 PM4325)
(Vc: 1150sfm)
(Fn: 0.055in/rev)

G96 S1150 M03;
G00 G54 Z1.0;
X3.6;
Z0.1 M08;

(Finish Face)
G70 P01 Q02;

G00 X3.6 Z1.0;

(Finish OD)
G70 P03 Q04;

G28 G40 X3.6 M09;
G28;
M01;

G28
T0707

(Operation: Finish ID)
(Cutting Unit ID: C4-SCLCR-13080-09)
(Insert ID: CCMT 3|2.5|2 PF4225)
(Vc: 1150sfm)
(Fn: 0.0056in/rev)

G96 S1150 M03;
G00 Z1.0;
X2.0 M08;

(Finish ID)
G70 P05 Q06;

G00 G40 Z1.0;
G28 X3.6 M09;
G28;
M01;

G28;
T0909;

(Operation: Thread)
(Cutting Unit ID: C4-266RFG-27050-16)
(Insert ID: 266RG-16UN01C200M)
(RPM: 968)
(Fn: 0.005in/rev)

G97 S968 M03;
G00 G54 Z1.0;
X3.6;
Z0.1 M08;

Z-0.4258 M24;
G92 X2.9841 Z-1.75 F0.055;
X2.9710;
X2.9589;
X2.9497;
X2.9419;
X2.9351;

G80;

G28 G40 X3.6 M09;
G28;
M30;
%
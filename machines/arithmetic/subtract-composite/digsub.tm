chkcry

chkcry f -> sub ~ U
chkcry n -> chkcry w N * carry.tm
chkcry w -> chkcry ~ N
chkcry 0123456789 -> done ~ H

sub 0 -> b0 ~ U
sub 1 -> b1 ~ U
sub 2 -> b2 ~ U
sub 3 -> b3 ~ U
sub 4 -> b4 ~ U
sub 5 -> b5 ~ U
sub 6 -> b6 ~ U
sub 7 -> b7 ~ U
sub 8 -> b8 ~ U
sub 9 -> b9 ~ U

b0 0 -> p0 ~ DD
b0 1 -> p1 ~ DD
b0 2 -> p2 ~ DD
b0 3 -> p3 ~ DD
b0 4 -> p4 ~ DD
b0 5 -> p5 ~ DD
b0 6 -> p6 ~ DD
b0 7 -> p7 ~ DD
b0 8 -> p8 ~ DD
b0 9 -> p9 ~ DD

b1 0 -> p9 ~ DD
b1 1 -> p0 ~ DD
b1 2 -> p1 ~ DD
b1 3 -> p2 ~ DD
b1 4 -> p3 ~ DD
b1 5 -> p4 ~ DD
b1 6 -> p5 ~ DD
b1 7 -> p6 ~ DD
b1 8 -> p7 ~ DD
b1 9 -> p8 ~ DD

b2 0 -> p8 ~ DD
b2 1 -> p9 ~ DD
b2 2 -> p0 ~ DD
b2 3 -> p1 ~ DD
b2 4 -> p2 ~ DD
b2 5 -> p3 ~ DD
b2 6 -> p4 ~ DD
b2 7 -> p5 ~ DD
b2 8 -> p6 ~ DD
b2 9 -> p7 ~ DD

b3 0 -> p7 ~ DD
b3 1 -> p8 ~ DD
b3 2 -> p9 ~ DD
b3 3 -> p0 ~ DD
b3 4 -> p1 ~ DD
b3 5 -> p2 ~ DD
b3 6 -> p3 ~ DD
b3 7 -> p4 ~ DD
b3 8 -> p5 ~ DD
b3 9 -> p6 ~ DD

b4 0 -> p6 ~ DD
b4 1 -> p7 ~ DD
b4 2 -> p8 ~ DD
b4 3 -> p9 ~ DD
b4 4 -> p0 ~ DD
b4 5 -> p1 ~ DD
b4 6 -> p2 ~ DD
b4 7 -> p3 ~ DD
b4 8 -> p4 ~ DD
b4 9 -> p5 ~ DD

b5 0 -> p5 ~ DD
b5 1 -> p6 ~ DD
b5 2 -> p7 ~ DD
b5 3 -> p8 ~ DD
b5 4 -> p9 ~ DD
b5 5 -> p0 ~ DD
b5 6 -> p1 ~ DD
b5 7 -> p2 ~ DD
b5 8 -> p3 ~ DD
b5 9 -> p4 ~ DD

b6 0 -> p4 ~ DD
b6 1 -> p5 ~ DD
b6 2 -> p6 ~ DD
b6 3 -> p7 ~ DD
b6 4 -> p8 ~ DD
b6 5 -> p9 ~ DD
b6 6 -> p0 ~ DD
b6 7 -> p1 ~ DD
b6 8 -> p2 ~ DD
b6 9 -> p3 ~ DD

b7 0 -> p3 ~ DD
b7 1 -> p4 ~ DD
b7 2 -> p5 ~ DD
b7 3 -> p6 ~ DD
b7 4 -> p7 ~ DD
b7 5 -> p8 ~ DD
b7 6 -> p9 ~ DD
b7 7 -> p0 ~ DD
b7 8 -> p1 ~ DD
b7 9 -> p2 ~ DD

b8 0 -> p2 ~ DD
b8 1 -> p3 ~ DD
b8 2 -> p4 ~ DD
b8 3 -> p5 ~ DD
b8 4 -> p6 ~ DD
b8 5 -> p7 ~ DD
b8 6 -> p8 ~ DD
b8 7 -> p9 ~ DD
b8 8 -> p0 ~ DD
b8 9 -> p1 ~ DD

b9 0 -> p1 ~ DD
b9 1 -> p2 ~ DD
b9 2 -> p3 ~ DD
b9 3 -> p4 ~ DD
b9 4 -> p5 ~ DD
b9 5 -> p6 ~ DD
b9 6 -> p7 ~ DD
b9 7 -> p8 ~ DD
b9 8 -> p9 ~ DD
b9 9 -> p0 ~ DD

p0 f -> done 0 H
p1 f -> done 1 H
p2 f -> done 2 H
p3 f -> done 3 H
p4 f -> done 4 H
p5 f -> done 5 H
p6 f -> done 6 H
p7 f -> done 7 H
p8 f -> done 8 H
p9 f -> done 9 H
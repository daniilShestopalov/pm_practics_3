set N := n1 n2 n3;
set T := t1 t2 t3 t4 t5 t6 t7 t8;

# трудоёмкости задач
param effort :=
  t1 4
  t2 6
  t3 6
  t4 6
  t5 7
  t6 5
  t7 3
  t8 4 ;

# предпочтения работников
param pref:
       t1  t2  t3  t4  t5  t6  t7  t8  :=
n1     1   4   4   4   3   10  7   2
n2     10  7   2   2   3   6   4   2
n3     4   5   6   9   7   8   3   1;

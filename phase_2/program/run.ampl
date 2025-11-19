let {n in N, m in T} x[n,m] :=
    if ( (ord(m)-1) mod card(N) + 1 ) = ord(n) then 1 else 0;

solve;

display maxLoad, minAvgPref;
display load, totalPref, avgPref, assigned;
display x;

printf "\nAssignments (worker <- task):\n";
for {n in N, m in T: x[n,m] > 0.5} {
    printf "%s <- %s\n", n, m;
}

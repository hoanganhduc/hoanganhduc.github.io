child_fact(oscar, karen, frank). 
child_fact(mary, karen, frank). 
child_fact(eve, anne, oscar). 
child_fact(henry, anne, oscar). 
child_fact(isolde, anne, oscar). 
child_fact(clyde, mary, oscarb). 

child(X,Z,Y) :- child_fact(X,Y,Z). 
child(X,Z,Y) :- child_fact(X,Z,Y).

descendant(X,Y) :- child(X,Y,Z).
descendant(X,Y) :- child(X,U,V), descendant(U,Y).

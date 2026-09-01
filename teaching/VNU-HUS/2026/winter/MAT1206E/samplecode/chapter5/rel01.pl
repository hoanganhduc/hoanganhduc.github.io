child(oscar, karen, frank). 
child(mary, karen, frank). 
child(eve, anne, oscar). 
child(henry, anne, oscar). 
child(isolde, anne, oscar). 
child(clyde, mary, oscarb). 

descendant(X,Y) :- child(X,Y,Z). 
descendant(X,Y) :- child(X,Z,Y). 
descendant(X,Y) :- child(X,U,V), descendant(U,Y).

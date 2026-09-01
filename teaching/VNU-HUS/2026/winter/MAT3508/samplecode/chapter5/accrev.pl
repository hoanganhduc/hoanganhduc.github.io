accrev([],A,A). 
accrev([H|T],A,R) :- accrev(T,[H|A],R).

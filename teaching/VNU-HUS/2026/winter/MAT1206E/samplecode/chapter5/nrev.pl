nrev([],[]). 
nrev([H|T],R) :- nrev(T,RT), append(RT,[H],R).

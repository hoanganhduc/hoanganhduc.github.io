start :- action(state(left,left,left,left),
                state(right,right,right,right)).

action(Start,Goal) :-
   plan(Start,Goal,[Start],Path),
   nl,write('Solution:'),nl,
   write_path(Path).
%   write_path(Path), fail. % all solutions output

plan(Start,Goal,Visited,Path) :-
   go(Start,Next),
   safe(Next),
   \+ member(Next,Visited),    % not(member(...))
   plan(Next,Goal,[Next|Visited],Path).
plan(Goal,Goal,Path,Path).

go(state(X,X,Z,K),state(Y,Y,Z,K)) :- across(X,Y). % farmer, wolf
go(state(X,W,X,K),state(Y,W,Y,K)) :- across(X,Y). % farmer, goat
go(state(X,W,Z,X),state(Y,W,Z,Y)) :- across(X,Y). % farmer, cabbage
go(state(X,W,Z,K),state(Y,W,Z,K)) :- across(X,Y). % farmer

across(left,right).
across(right,left).

safe(state(B,W,Z,K)) :- across(W,Z), across(Z,K).
safe(state(B,B,B,K)).
safe(state(B,W,B,B)).

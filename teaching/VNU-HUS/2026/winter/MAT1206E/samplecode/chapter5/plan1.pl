% Run start. to start the program
start :- action(state(left,left,left,left),
                state(right,right,right,right)).

% state(Farmer,Wolf,Goat,Cabbage) describes the current 
% state of the world. Each variable has two possible values: left, right
% state(left,left,right,right) means 
% the farmer and the wolf are on the left-hand side
% and the goat and cabbage are on the right-hand side

action(Start,Goal) :-
   plan(Start,Goal,[Start],Path),
   nl,write('Solution:'),nl,
   write(Path), fail.
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

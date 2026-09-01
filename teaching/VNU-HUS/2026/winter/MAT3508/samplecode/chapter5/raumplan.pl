%%% Run in GNU-PROLOG
start :-
    fd_domain([Mayer, Hoover, Miller, Smith],1,4), 
    fd_all_different([Mayer, Miller, Hoover, Smith]), 
    
    fd_domain([German, English, Math, Physics],1,4), 
    fd_all_different([German, English, Math, Physics]), 
    
    fd_labeling([Mayer, Hoover, Miller, Smith]), 
    
    Mayer #\=4,                  % Mayer not in room 4
    Miller #= German,            % Miller tests German
    dist(Miller, Smith) #>= 2,   % Distance Miller/Smith >= 2
    Hoover #= Math,              % Hoover tests mathematics
    Physics #= 4,                % Physics in room 4
    German #\= 1,                % German not in room 1
    English #\= 1,               % English not in room 1
    nl,
    write([Mayer, Hoover, Miller, Smith]), nl, 
    write([German, English, Math, Physics]), nl.

% --- Facts ---
dog(fido).
dog(rex).
cat(whiskers).
bird(tweety).

% --- Rules ---
animal(X) :- dog(X).
animal(X) :- cat(X).
animal(X) :- bird(X).

mammal(X) :- dog(X).
mammal(X) :- cat(X).

% --- Example of reasoning ---
likes_to_play(X) :- dog(X).
likes_to_play(X) :- cat(X).

what_is_it :-
    write('Enter a name: '),
    read(Name),
    (   dog(Name) -> write('That is a dog!');
        cat(Name) -> write('That is a cat!');
        bird(Name) -> write('That is a bird!');
        write('Unknown creature.')
    ), nl.

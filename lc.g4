grammar lc;

SELECT: 'select';
FROM: 'from';
ID: [a-zA-Z0-9_]+;

select: SELECT columnList FROM ID ';';
columnList: '*' | column (',' column)*;

column: ID
    | expression 'as' ID
 ;

expression: ID #Identifier
          | expression '*' ID        # Mult
          | expression '+' ID       # Sum
          | expression '-' ID        # Subst
          | expression '/' ID        # Div
          | '(' expression ')'         # Phar
;

Spaces: [ \t\r\n] -> skip;


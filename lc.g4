grammar lc;

SELECT: 'select';
FROM: 'from';
ORDER: 'order';
BY: 'by';
ID: [a-zA-Z0-9_.]+;

select: SELECT columnList FROM ID ';'
 | SELECT columnList FROM ID ORDER BY constraintList ';'
;

columnList: '*' | column (',' column)*;

column: ID
    | expression 'as' ID
 ;

constraintList: constraint (',' constraint);

constraint: ID 'asc'
 | ID 'desc'
 ;

expression: ID #Identifier
          | expression '*' ID        # Mult
          | expression '+' ID       # Sum
          | expression '-' ID        # Subst
          | expression '/' ID        # Div
          | '(' expression ')'         # Phar
;

Spaces: [ \t\r\n] -> skip;


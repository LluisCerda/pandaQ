grammar lc;

SELECT: 'select';
FROM: 'from';
ID: [a-zA-Z0-9_]+;

select: SELECT columnList FROM ID ';';
columnList: '*' | expression (',' expression)*;

expression: ID #Identifier
          | ID '*' expression        # Mult
          | ID '+' expression        # Sum
          | ID '-' expression        # Subst
          | ID '/' expression        # Div
          | '(' expression ')'       # Phar
          | ID 'as' ID               # Alias
;

Spaces: [\t\r\n] -> skip;


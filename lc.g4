grammar lc;

SELECT: 'select';
FROM: 'from';
ORDER: 'order';
BY: 'by';
WHERE: 'where';
NOT: 'not';
INNER: 'inner';
JOIN: 'join';
ON: 'on';
PLOT: 'plot';
ID: [a-zA-Z0-9_.]+;

root: assignation | select | plot;

plot: PLOT ID;

assignation: ID ':=' select ;

select: SELECT columnList FROM ID ';'
 | SELECT columnList FROM ID ORDER BY constraintList ';'
 | SELECT columnList FROM ID WHERE conditionList ';'
 | SELECT columnList FROM ID WHERE conditionList ORDER BY constraintList ';'
 | SELECT columnList FROM ID innerJoinList ';'
 | SELECT columnList FROM ID innerJoinList WHERE conditionList ';'
 | SELECT columnList FROM ID innerJoinList WHERE conditionList ORDER BY constraintList ';'
;

innerJoinList: innerJoin (innerJoin)*;
innerJoin: INNER JOIN ID ON ID '=' ID;

columnList: '*' | column (',' column)*;
column: ID
    | expression 'as' ID
 ;

constraintList: constraint (',' constraint)*;
constraint: ID 'asc'
 | ID 'desc'
 ;

conditionList: condition ('and' condition)*;
condition: ID '=' ID               #Equals
 | ID '<' ID                             #Minor
 | NOT ID '=' ID                     #NotEquals
 | NOT ID '<' ID                     #NotMinor
 ;

expression: ID #Identifier
          | expression '*' ID        # Mult
          | expression '+' ID       # Sum
          | expression '-' ID        # Subst
          | expression '/' ID        # Div
          | '(' expression ')'         # Phar
;

Spaces: [ \t\r\n] -> skip;


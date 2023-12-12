grammar lc;

root: assignation | select | plot;

plot: PLOT ID ';';

assignation: ID ':=' select ;

select: SELECT columnList FROM ID (innerJoinList)? (WHERE conditionList)? (subQuery)? (ORDER BY orderingList)? ';'
;

subQuery: WHERE ID IN '(' select ')';

innerJoinList: innerJoin (innerJoin)*;
innerJoin: INNER JOIN ID ON ID '=' ID;

columnList: '*' | column (',' column)*;
column: ID
    | expression 'as' ID
 ;

 expression: ID #Identifier
          | expression '*' NUM        # Mult
          | expression '+' NUM       # Sum
          | expression '-' NUM        # Subst
          | expression '/' NUM        # Div
;

orderingList: order (',' order)*;
order: ID 'asc'
 | ID 'desc'
 ;

conditionList: condition ('and' condition)*;
condition: ID '=' ID               #Equals
 | ID '<' ID                             #Minor
 | NOT ID '=' ID                     #NotEquals
 | NOT ID '<' ID                     #NotMinor
 ;

Spaces: [ \t\r\n] -> skip;
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
IN: 'in';
ID: [a-zA-Z0-9_]+;
NUM: DIGIT+ ('.' DIGIT+)?;
DIGIT: '0'..'9';


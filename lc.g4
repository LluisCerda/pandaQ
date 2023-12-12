grammar lc;

root: assignation ';' | select ';' | plot ';';

plot: PLOT ID;

assignation: ID ':=' select ;

select: SELECT columnList FROM ID (innerJoinList)? (WHERE conditionList)? (subQuery)? (ORDER BY orderingList)? ;

columnList: '*' | column (',' column)*;

column: ID | expression 'as' ID;

expression: ID #Identifier
          | expression '*' NUM          # Mult
          | '(' expression ')' '*' NUM  # Mult
          | expression '+' NUM         # Sum
          | '(' expression ')' '+' NUM  # Sum
          | expression '-' NUM          # Subst
          | '(' expression ')' '-' NUM  # Subst
          | expression '/' NUM          # Div
          | '(' expression ')' '/' NUM  # Div
;

innerJoinList: innerJoin (innerJoin)*;

innerJoin: INNER JOIN ID ON ID '=' ID;

conditionList: condition ('and' condition)*;

condition: ID '=' ID               #Equals
 | ID '<' ID                             #Minor
 | NOT ID '=' ID                     #NotEquals
 | NOT ID '<' ID                     #NotMinor
;

subQuery: WHERE ID IN '(' select ')';


orderingList: order (',' order)*;

order: ID | ID ASC | ID DESC;

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
ASC: 'asc';
DESC: 'desc';
ID: [a-zA-Z0-9_]+;
NUM: DIGIT+ ('.' DIGIT+)?;
DIGIT: '0'..'9';


grammar lc;

// Define lexer rules
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';

ID: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*;

SELECT: 'SELECT';
FROM: 'FROM';
STAR: '*';
SEMICOLON: ';';

// Define parser rules
sql_query: SELECT STAR FROM ID SEMICOLON;

// Skip whitespaces and newlines
WS: [ \t\r\n]+ -> skip;


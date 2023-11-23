grammar lc;

SELECT: 'select';
FROM: 'from';
ID: [a-zA-Z]+; 

select: SELECT '*' FROM ID ';';

SPACES: [ \t\r\n] -> skip;


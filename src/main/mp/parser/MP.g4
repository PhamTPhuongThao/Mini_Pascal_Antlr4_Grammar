// Pham Thi Phuong Thao
// MSSV: 1613224

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:
	(vardecblock|funcdec|prodec)*
    ; 

// VARIABLE DECLARATION 
	
	vardecblock: VAR (vardec SEMI)+;
	
	vardec: 
		listofid COLON twotype
		;
	
	listofid: 
		ID COMMA listofid 
		| ID
		;
	
	twotype:
		pritype
		|arraytype
		;

	pritype: 
		INTEGER 
		| REAL 
		| STRING 
		| BOOLEAN
		;
	
	arraytype: 
		ARRAY LSB indexlist RSB OF pritype
		;
	
	indexlist: 
		(MINUS)? expression DOUBLEDOT (MINUS)? expression
		;

// FUNCTION DECLARATION

	funcdec:
		FUNCTION ID LB (paralist)? RB COLON returntype SEMI (vardecblock)? compoundstmt
		;

	paralist:
		paradec SEMI paralist
		|paradec
		;

	paradec:
		listofid COLON pritype 
		|ID COLON arraytype
		;

	returntype:
		pritype
		|arraytype
		;

// PROCEDURE DECLARATION
	
	prodec:
		PROCEDURE ID LB (paralist)? RB SEMI (vardecblock)? compoundstmt
		;

// COMMENT

	BLOCK_COMMENT:
	'(*' .*? '*)' ->skip
    ;

	NEW_BLOCK_COMMENT:
	'{' .*? '}' ->skip
    ;

	LINE_COMMENT:
	'//' ~[\r\n]* ->skip
    ;

// STATEMENT DECLARATION

	statement:
		assignstmt SEMI
		|ifstmt
		|forstmt
		|whilestmt
		|breakstmt SEMI
		|continuestmt SEMI
		|returnstmt SEMI
		|callstmt SEMI
		|compoundstmt
		|withstmt
		;

	assignstmt: 
		vari (':=' expression)+
		;

	vari: 
		ID
		|ID LSB expression RSB 
		//|literals
		;

	ifstmt:
		IF expression THEN statement 
		|IF expression THEN statement (ELSE statement)? 
		;

	whilestmt: 
		WHILE expression DO statement
		;

	forstmt: 
		FOR ID ':=' expression chooseassign expression DO statement
		;
	
	chooseassign:
		TO
		|DOWNTO
		;

	breakstmt:
		BREAK
		;

	continuestmt:
		CONTINUE
		;

	returnstmt:
		RETURN
		;
	
	compoundstmt:
		BEGIN (statement)* END 
		;

	withstmt:
		WITH (vardec SEMI)+ DO statement
		;
	
	callstmt:
		ID LB explist RB
		;

	explist:
		expression COMMA explist
		|expression
		;

// EXPRESSION

	expression:
		expression (AND THEN | OR ELSE) expression1
		|expression1
		;
	
	expression1: 
		expression2 ('='|'<>'|'<'|'<='|'>'|'>=') expression2
		|expression2
		;

	expression2:
		expression2 (PLUS|MINUS|OR) expression3
		|expression3
		;

	expression3:
		expression3 (DIVI|MULT|DIV|MOD|AND) expression4
		|expression4
		;

	expression4:
		expression4 (MINUS|NOT) expression5
		|expression5
		;

	expression5:
		expression5 LB expression RB
		|expression6
		;

	expression6:
		literals
		|ID
		|funccall
		|LB expression RB 
		|ID LSB expression RSB 
		;

	funccall: 
		ID LB ((expression COMMA)* expression)? RB ;

// LEXER RULES

	fragment A:('a'|'A'); 
	fragment B:('b'|'B');
	fragment C:('c'|'C');
	fragment D:('d'|'D');
	fragment E:('e'|'E');
	fragment F:('f'|'F');
	fragment G:('g'|'G');
	fragment H:('h'|'H');
	fragment I:('i'|'I');
	fragment J:('j'|'J');
	fragment K:('k'|'K');
	fragment L:('l'|'L');
	fragment M:('m'|'M');
	fragment N:('n'|'N');
	fragment O:('o'|'O');
	fragment P:('p'|'P');
	fragment Q:('q'|'Q');
	fragment R:('r'|'R');
	fragment S:('s'|'S');
	fragment T:('t'|'T');
	fragment U:('u'|'U');
	fragment V:('v'|'V');
	fragment W:('w'|'W');
	fragment X:('x'|'X');
	fragment Y:('y'|'Y');
	fragment Z:('z'|'Z');
	
//TOKENS
	
	VAR : V A R ;

	FUNCTION: F U N C T I O N ;

	PROCEDURE: P R O C E D U R E ;
	
	ARRAY : A R R A Y;
	
	OF : O F ;
	
	INTEGER : I N T E G E R;

	BOOLEAN : B O O L E A N ;

	REAL : R E A L ;

	STRING : S T R I N G ;

	TRUE : T R U E ;

	FALSE : F A L S E;

	IF  : I F ;

	THEN : T H E N ;

	ELSE : E L S E ;

	WHILE: W H I L E ;
	
	DO: D O ;

	FOR: F O R ;
	
	TO: T O ;

	DOWNTO: D O W N T O ;

	BREAK: B R E A K ;

	CONTINUE: C O N T I N U E ;

	RETURN: R E T U R N ;

	BEGIN: B E G I N ;

	END: E N D ;

	WITH: W I T H ;

	DIV : D I V ;
	
	OR  : O R ;
	
	AND : A N D ;
	
	NOT : N O T ;

	MOD: M O D ;

	PLUS : '+';
	
	MINUS : '-';
	
	MULT : '*';

	DIVI : '/';
	
	EQUALS : '=';
	
	LB: '(' ;

	RB: ')' ;

	SEMI: ';' ;

	COLON: ':';

	LSB: '[';

	RSB: ']';

	COMMA: ',';
	
	DOUBLEDOT: '..';
	
	ID: [a-zA-Z_]+[a-zA-Z0-9_]*  ;

//LITERAL
	literals:
		BOOLLIT
		|INTLIT
		|FLOATLIT
		|STRINGLIT
		;

	BOOLLIT
		:'true'
		|'false'
		;

	INTLIT: 
		[0-9]+
		;

	FLOATLIT:
		INTLIT '.' [0-9]* EXPONENT?
		|'.' INTLIT EXPONENT?
		| INTLIT EXPONENT
		;

	STRINGLIT
    : '"'(ESC | ~[\r\n"\\EOF])*'"' 
        {
            s=self.text[1:-1]
            self.text=s
        }
    ;

	fragment EXPONENT     
		: ('e'|'E') ('-')? [0-9]+
		;   
		
	WS 
		: [ \t\r\n\f]+ -> skip 
		; // skip spaces, tabs, newlines

	fragment ESC
		: '\\' [bfrnt'"\\] 
		;

// ERROR
	ERROR_CHAR
		: .
			{ 
				raise ErrorToken(self.text) 
			}
		;

	ILLEGAL_ESCAPE
		: '"' (ESC | ~["\\])*? ([\\] ~[bfrnt'"\\]) 
			{
			raise IllegalEscape(self.text[1:])
			}
		;

	UNCLOSE_STRING
		:  '"' (ESC | ~["\r\n] |((~'\\')'\\"'))* ('\n'| EOF)
			{
				if self.text[-1]=='\n':
					raise UncloseString(self.text[1:-1])
				else:
					raise UncloseString(self.text[1:])
			}
		;
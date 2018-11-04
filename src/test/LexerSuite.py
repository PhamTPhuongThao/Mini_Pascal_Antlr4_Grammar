import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_id1(self):
        """test id1"""
        self.assertTrue(TestLexer.test("abc a1_ a B _","abc,a1_,a,B,_,<EOF>", 101))
    def test_id2(self):
        """test id2"""
        self.assertTrue(TestLexer.test("1_a", "1,_a,<EOF>", 102))
    def test_id3(self):
        """test id3"""
        self.assertTrue(TestLexer.test("1A_", "1,A_,<EOF>", 103))
    def test_id4(self):
        """test id4"""
        self.assertTrue(TestLexer.test("A_1__b2 a_1_c_2", "A_1__b2,a_1_c_2,<EOF>", 104))



    def test_integer1(self):
        """test integer1"""
        self.assertTrue(TestLexer.test("123 _a 123","123,_a,123,<EOF>", 105))
    def test_integer2(self):
        """test integer2"""
        self.assertTrue(TestLexer.test("0 00 000", "0,00,000,<EOF>", 106)) 
    def test_integer3(self):
        """test integer3"""
        self.assertTrue(TestLexer.test("00a000", "00,a000,<EOF>", 107))
    def test_integer4(self):
        """test integer4"""
        self.assertTrue(TestLexer.test("_0 _00 _000","_0,_00,_000,<EOF>", 108))
    def test_integer5(self):
        """test integer5"""
        self.assertTrue(TestLexer.test("0x00 0e00","0,x00,0e00,<EOF>", 109))
    def test_integer6(self):
        """test integer6"""



    def test_real1(self):
        """test real1"""
        self.assertTrue(TestLexer.test("1. 0. 33. 454.", "1.,0.,33.,454.,<EOF>", 110))
    def test_real2(self):
        """test real2"""
        self.assertTrue(TestLexer.test("1.2 34.3 434.5 3.643 33.66", "1.2,34.3,434.5,3.643,33.66,<EOF>", 111))
    def test_real3(self):
        """test real3"""
        self.assertTrue(TestLexer.test(".1 .35 .352 .0000", ".1,.35,.352,.0000,<EOF>", 112))
    def test_real4(self):
        """test real4"""
        self.assertTrue(TestLexer.test("1e2 2e34 24e2 00e35", "1e2,2e34,24e2,00e35,<EOF>", 113))
    def test_real5(self):
        """test real5"""
        self.assertTrue(TestLexer.test("1.2E-2 23.24E3 43.54E64", "1.2E-2,23.24E3,43.54E64,<EOF>", 114))
    def test_real6(self):
        """test real6"""
        self.assertTrue(TestLexer.test("1.2e-2 24.22e8 35.38e72", "1.2e-2,24.22e8,35.38e72,<EOF>", 115))
    def test_real7(self):
        """test real7"""
        self.assertTrue(TestLexer.test(".1E2 .2e24 .33e6 .35e64", ".1E2,.2e24,.33e6,.35e64,<EOF>", 116))
    def test_real8(self):
        """test real8"""
        self.assertTrue(TestLexer.test("0.0 00.35 45.00 00.00", "0.0,00.35,45.00,00.00,<EOF>", 117))
    def test_real9(self):
        """test real9"""
        self.assertTrue(TestLexer.test("3e7 0E74 94e2 59E34","3e7,0E74,94e2,59E34,<EOF>", 118))
    def test_real10(self):
        """test real10"""
        self.assertTrue(TestLexer.test("0.33E-3 3434e-534", "0.33E-3,3434e-534,<EOF>", 119))
    def test_real11(self):
        """test real11"""
        self.assertTrue(TestLexer.test("1.e2", "1.e2,<EOF>", 120))



    def test_string1(self):
        """test string1"""
        self.assertTrue(TestLexer.test('"_______"', "_______,<EOF>", 121))
    def test_string2(self):
        """test string2"""
        self.assertTrue(TestLexer.test('"_\\b___"', "_\\b___,<EOF>", 122))
    def test_string3(self):
        """test string3"""
        self.assertTrue(TestLexer.test('"_\\f___"', "_\\f___,<EOF>", 123))
    def test_string4(self):
        """test string4"""
        self.assertTrue(TestLexer.test('"_\\r___"', "_\\r___,<EOF>", 124))
    def test_string5(self):
        """test string5"""
        self.assertTrue(TestLexer.test('"_\\n___"', "_\\n___,<EOF>", 125))
    def test_string6(self):
        """test string6"""
        self.assertTrue(TestLexer.test('"_\\t___"', "_\\t___,<EOF>", 126))
    def test_string7(self):
        """test string7"""
        self.assertTrue(TestLexer.test('"_\\\'__"', "_\\\'__,<EOF>", 127))
    def test_string8(self):
        """test string8"""
        self.assertTrue(TestLexer.test('"_\\\"__"', "_\\\"__,<EOF>", 128))
    def test_string9(self):
        """test string9"""
        self.assertTrue(TestLexer.test('"_\\\\__"', "_\\\\__,<EOF>", 129))

    def test_string_error1(self):
        """test string error1"""
        self.assertTrue(TestLexer.test('"__\b__"', "Unclosed String: __", 130))
    def test_string_error2(self):
        """test string error2"""
        self.assertTrue(TestLexer.test('"__\f__"', "Unclosed String: __", 131))
    def test_string_error3(self):
        """test string error3"""
        self.assertTrue(TestLexer.test('"__\r__"', "Unclosed String: __", 132))
    def test_string_error4(self):
        """test string error4"""
        self.assertTrue(TestLexer.test('"__\n__"', "Unclosed String: __", 133))
    def test_string_error5(self):
        """test string error5"""
        self.assertTrue(TestLexer.test('"__\t__"', "Unclosed String: __", 134))
    def test_string_error6(self):
        """test string error6"""
        self.assertTrue(TestLexer.test('"__\'__"', "Unclosed String: __", 135))
    def test_string_error7(self):
        """test string error7"""
        self.assertTrue(TestLexer.test('"__\"__"', "__,__,Unclosed String: ", 136))
    def test_string_error8(self):
        """test string error8"""
        self.assertTrue(TestLexer.test('"__\\__"', "Illegal Escape In String: __\\_", 137))
    def test_string_error9(self):
        """test string error9"""
        self.assertTrue(TestLexer.test('"abc', "Unclosed String: abc", 138))
    def test_string_error10(self):
        """test string error10"""
        self.assertTrue(TestLexer.test('"abc\\a"',"Illegal Escape In String: abc\\a", 139))
    def test_string_error11(self):
        """test string error11"""
        self.assertTrue(TestLexer.test('"abc\\a',"Illegal Escape In String: abc\\a", 140))
    def test_string_error12(self):
        """test string error12"""
        self.assertTrue(TestLexer.test('"abc\\', "Unclosed String: abc", 141))
    def test_string_error13(self):
        """test string error13"""
        self.assertTrue(TestLexer.test('"dsad\\t \\b \\n "', r"dsad\t \b \n ,<EOF>", 142))



    def test_comment1(self):
        """test comment1"""
        self.assertTrue(TestLexer.test("(*ab\b\f\r\n\t\'\"\"\\cde*)","<EOF>", 143))
    def test_comment2(self):
        """test comment2"""
        self.assertTrue(TestLexer.test("{ab\b\f\r\n\t\'\"\"\\cde}", "<EOF>", 144))
    def test_comment3(self):
        """test comment3"""
        self.assertTrue(TestLexer.test("//ab\b\f\t\'\"\"\\cde", "<EOF>", 145))
    def test_comment4(self):
        """test comment4"""
        self.assertTrue(TestLexer.test("//(*abcde*)", "<EOF>", 146))
    def test_comment5(self):
        """test comment5"""
        self.assertTrue(TestLexer.test("//{abcde}", "<EOF>", 147))
    def test_comment6(self):
        """test comment6"""
        self.assertTrue(TestLexer.test("(*//abcde*)", "<EOF>", 148))
    def test_comment7(self):
        """test comment7"""
        self.assertTrue(TestLexer.test("{//abcde}", "<EOF>", 149))
    def test_comment8(self):
        """test comment8"""
        self.assertTrue(TestLexer.test("//ab\rcde", "cde,<EOF>", 150))
    def test_comment9(self):
        """test comment9"""
        self.assertTrue(TestLexer.test("//ab\ncde", "cde,<EOF>", 151))
    def test_comment10(self):
        """test comment10"""
        self.assertTrue(TestLexer.test("(*a(*b*)c*)", "c,*,),<EOF>", 152))
    def test_comment11(self):
        """test comment11"""
        self.assertTrue(TestLexer.test("{a{b}c}", "c,Error Token }", 153))
    


    def test_keyword_break(self):
        """test keyword break"""        
        self.assertTrue(TestLexer.test("break BREAK 0bReAk", "break,BREAK,0,bReAk,<EOF>", 154))
    def test_keyword_continue(self):
        """test keyword continue"""   
        self.assertTrue(TestLexer.test("continue CONTINUE IcOnTiNue", "continue,CONTINUE,IcOnTiNue,<EOF>", 155))
    def test_keyword_for(self):
        """test keyword for"""   
        self.assertTrue(TestLexer.test("for FOR fOrG FoRg", "for,FOR,fOrG,FoRg,<EOF>", 156))
    def test_keyword_to(self):
        """test keyword to"""   
        self.assertTrue(TestLexer.test("to TO AtO ToA", "to,TO,AtO,ToA,<EOF>", 157))
    def test_keyword_downto(self):
        """test keyword downto"""   
        self.assertTrue(TestLexer.test("downto DOWNTO DoWnToA", "downto,DOWNTO,DoWnToA,<EOF>", 158))
    def test_keyword_do(self):
        """test keyword do"""   
        self.assertTrue(TestLexer.test("do DO IdO DoI", "do,DO,IdO,DoI,<EOF>", 159))
    def test_keyword_if(self):
        """test keyword if"""   
        self.assertTrue(TestLexer.test("if IF IFa eif", "if,IF,IFa,eif,<EOF>", 160))
    def test_keyword_then(self):
        """test keyword then"""   
        self.assertTrue(TestLexer.test("then then iThen thenI", "then,then,iThen,thenI,<EOF>", 161))
    def test_keyword_else(self):
        """test keyword else"""   
        self.assertTrue(TestLexer.test("else ELSE iElSe elseI", "else,ELSE,iElSe,elseI,<EOF>", 162))
    def test_keyword_return(self):
        """test keyword return"""   
        self.assertTrue(TestLexer.test("return RETURN iRETurn retUrnI", "return,RETURN,iRETurn,retUrnI,<EOF>", 163))
    def test_keyword_while(self):
        """test keyword while"""   
        self.assertTrue(TestLexer.test("while WHILE iWhile whILEi", "while,WHILE,iWhile,whILEi,<EOF>", 164))
    def test_keyword_begin(self):
        """test keyword begin"""   
        self.assertTrue(TestLexer.test("begin BEGIN iBegin beginI", "begin,BEGIN,iBegin,beginI,<EOF>", 165))
    def test_keyword_end(self):
        """test keyword end"""   
        self.assertTrue(TestLexer.test("end END keND enDk", "end,END,keND,enDk,<EOF>", 166))
    def test_keyword_function(self):
        """test keyword function"""   
        self.assertTrue(TestLexer.test("function uFUNCTION FuNcTionu", "function,uFUNCTION,FuNcTionu,<EOF>", 167))
    def test_keyword_procedure(self):
        """test keyword procedure"""   
        self.assertTrue(TestLexer.test("procedure pPROCEDURE pRocEduREp", "procedure,pPROCEDURE,pRocEduREp,<EOF>", 168))
    def test_keyword_var(self):
        """test keyword var"""   
        self.assertTrue(TestLexer.test("var VAR vvAR VaRv", "var,VAR,vvAR,VaRv,<EOF>", 169))
    def test_keyword_true(self):
        """test keyword true"""   
        self.assertTrue(TestLexer.test("true TRue tRUEi", "true,TRue,tRUEi,<EOF>", 170))
    def test_keyword_false(self):
        """test keyword false"""   
        self.assertTrue(TestLexer.test("false FAlSE aFalSe", "false,FAlSE,aFalSe,<EOF>", 171))
    def test_keyword_array(self):
        """test keyword array"""   
        self.assertTrue(TestLexer.test("array ARRAY ArraYa", "array,ARRAY,ArraYa,<EOF>", 172))
    def test_keyword_of(self):
        """test keyword of"""   
        self.assertTrue(TestLexer.test("of OF rOf oFr", "of,OF,rOf,oFr,<EOF>", 173))
    def test_keyword_real(self):
        """test keyword real"""   
        self.assertTrue(TestLexer.test("real REAL gReal rEALg", "real,REAL,gReal,rEALg,<EOF>", 174))
    def test_keyword_boolean(self):
        """test keyword boolean"""   
        self.assertTrue(TestLexer.test("boolean BOOLEAN bOOleaNq", "boolean,BOOLEAN,bOOleaNq,<EOF>", 175))
    def test_keyword_integer(self):
        """test keyword integer"""   
        self.assertTrue(TestLexer.test("integer INTEGER aInteGer", "integer,INTEGER,aInteGer,<EOF>", 176))
    def test_keyword_string(self):
        """test keyword string"""   
        self.assertTrue(TestLexer.test("string STRING kStrinG", "string,STRING,kStrinG,<EOF>", 177))
    def test_keyword_not(self):
        """test keyword not"""   
        self.assertTrue(TestLexer.test("not NOT nOth sNot", "not,NOT,nOth,sNot,<EOF>", 178))
    def test_keyword_and(self):
        """test keyword and"""   
        self.assertTrue(TestLexer.test("and AND yaND yAnD", "and,AND,yaND,yAnD,<EOF>", 179))
    def test_keyword_or(self):
        """test keyword or"""   
        self.assertTrue(TestLexer.test("or OR hoR Orh", "or,OR,hoR,Orh,<EOF>", 180))
    def test_keyword_div(self):
        """test keyword div"""   
        self.assertTrue(TestLexer.test("div DIV jDiv diVj", "div,DIV,jDiv,diVj,<EOF>", 181))
    def test_keyword_mod(self):
        """test keyword mod"""   
        self.assertTrue(TestLexer.test("mod MOD nmOD MoDn", "mod,MOD,nmOD,MoDn,<EOF>", 182))
    def test_keyword_with(self):
        """test keyword with"""   
        self.assertTrue(TestLexer.test("with WITH mWItH wIthm", "with,WITH,mWItH,wIthm,<EOF>", 183))
      
        

    def test_operator1(self):
        """test operator1"""
        self.assertTrue(TestLexer.test("+ - * / <> = < > <= >=", "+,-,*,/,<>,=,<,>,<=,>=,<EOF>", 184))
    def test_operator2(self):
        """test operator2"""
        self.assertTrue(TestLexer.test("+-*/<>=<><=>=", "+,-,*,/,<>,=,<>,<=,>=,<EOF>", 185))
    def test_operator3(self):
        """test operator3"""
        self.assertTrue(TestLexer.test("<+>", "<,+,>,<EOF>", 186))
    def test_operator4(self):
        """test operator4"""
        self.assertTrue(TestLexer.test("==<<=<", "=,=,<,<=,<,<EOF>", 187))
        


    def test_separator1(self):
        """test separator1"""
        self.assertTrue(TestLexer.test("[]:();,..:=", "[,],:,(,),;,,,..,:=,<EOF>", 188))



    def test_error1(self):
        """test error1"""
        self.assertTrue(TestLexer.test("\\ .", "Error Token \\", 189))
    def test_error2(self):
        """test error2"""
        self.assertTrue(TestLexer.test(". ..", "Error Token .", 190))
    def test_error3(self):
        """test error3"""
        self.assertTrue(TestLexer.test("...", "..,Error Token .", 191))

        

    def test_complex1(self):
        """test complex1"""
        input = r"""4f for ,  real <> if do downto :
        (* * ) e4686,end,integer ; , for return if Bbfd7 +rf588 > R8121,-,,*)
        // var,+,, M6af4 , with,=,-
        to >= ( Q51ca : ] to Ie9
        """
        expect = r"4,f,for,,,real,<>,if,do,downto,:,to,>=,(,Q51ca,:,],to,Ie9,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 192))


    def test_complex2(self):
        """test complex2"""
        input = r"""
            // <>,>,:=  Df28f * := - mod , of ;lf8f5 not := <= end <= , mod continue
            (* , for zd0ec,end,T9167 = He16f,-,(*) else,with,or
            begin real for z77c3 ]  s229b else ; continue 
            """
        expect = r"else,,,with,,,or,begin,real,for,z77c3,],s229b,else,;,continue,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 193))


    def test_complex3(self):
        """test complex3"""
        input = r"""
        // real,),: E75c5 /z8fe1,Oadae ( < >= R76acontinue,F7d93 .. F69d9
        if,and,array[  while else .. + T3117 while
        <> : ; 7  *procedure procedure false <> / if <> mod
        (* ; do ,,,<>*)
        """
        expect = r"if,,,and,,,array,[,while,else,..,+,T3117,while,<>,:,;,7,*,procedure,procedure,false,<>,/,if,<>,mod,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 194))


    def test_complex4(self):
        """test complex4"""
        input = r"""
        // for,[,(ebd2c / real <= n9afc begin <>  t59e3 := false end ebd2c / real <=function,real,while
        (  n9afc begin <> for < to * if array Icd8e := ] ; + return = [
        (* , -  array Icd8e := ] ; + rN3453,+,caa7a <> for,[,( t59e3 := functionZf62a,+,]*)
        """
        expect = r"(,n9afc,begin,<>,for,<,to,*,if,array,Icd8e,:=,],;,+,return,=,[,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 195))   


    def test_complex5(self):
        """test complex5"""
        input = r"""
        break,+,] e8fe2 of ..,:=,if Wcaa7 = := begin else else
        := boolean then Mto while true downto  ( return
        (* ( function Nc1f8,*,T9f7a en M7be9 function end > k3932 / := .. >= to while tr:= Z1d53,<>,..*)
        """
        expect = r"break,,,+,,,],e8fe2,of,..,,,:=,,,if,Wcaa7,=,:=,begin,else,else,:=,boolean,then,Mto,while,true,downto,(,return,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 196))


    def test_complex6(self):
        """test complex6"""
        input = r"""
        procedure f(); 
	    begin
		    with a,b: real;; do with a: array [1 .. 56] of real; do n := a*b; 
		    with x:string; do with str: string; do x := str;
	    end
        """
        expect = r"procedure,f,(,),;,begin,with,a,,,b,:,real,;,;,do,with,a,:,array,[,1,..,56,],of,real,;,do,n,:=,a,*,b,;,with,x,:,string,;,do,with,str,:,string,;,do,x,:=,str,;,end,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 197))


    def test_complex7(self):
        """test complex7"""
        input = r"""
        FUNCtion aaa(): real ;
        var x1,y2: real;
        begin
            with num: real ; arr : array [1 .. 2] of string ; do begin
                func(arr);
                proc(x, y, z);
                with i: real ; do begin
                    if(x>0) then merge(i,"test");
                end end end
        """
        expect = r"FUNCtion,aaa,(,),:,real,;,var,x1,,,y2,:,real,;,begin,with,num,:,real,;,arr,:,array,[,1,..,2,],of,string,;,do,begin,func,(,arr,),;,proc,(,x,,,y,,,z,),;,with,i,:,real,;,do,begin,if,(,x,>,0,),then,merge,(,i,,,test,),;,end,end,end,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 198))


    def test_complex8(self):
        """test complex8"""
        input = r"""procedure foo(a: real) ;
        var num: string ;
        begin
            3 := t;
            a[1][1] := t[12] ;
        end
        """
        expect = r"procedure,foo,(,a,:,real,),;,var,num,:,string,;,begin,3,:=,t,;,a,[,1,],[,1,],:=,t,[,12,],;,end,<EOF>"

        self.assertTrue(TestLexer.test(input, expect, 199))


    def test_complex9(self):
        """test complex9"""
        input = r"""
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End
        """
        expect = r"procedurE,foo,(,b,:,real,),;,begin,1,[,1,],:=,1,;,(,1,>=,0,),[,2,],:=,2,+,a,[,1,],[,1,],+,c,+,(,abc,<,0,),;,ahihi,(,1,),[,m,+,1,],:=,3,;,(,1,+,a,[,1,],+,(,1,<,0,),),[,10,],:=,4,;,End,<EOF>"
        
        self.assertTrue(TestLexer.test(input, expect, 200))


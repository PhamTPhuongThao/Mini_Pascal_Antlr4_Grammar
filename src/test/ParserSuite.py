import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_vardecl_single_id(self):
        """test vardecl single id"""
        input = """var a: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 201))

    def test_vardecl_multi_id(self):
        """test vardecl multi id"""
        input = """var a, b: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 202))

    def test_vardecl_multi_line_single_var(self):
        """test vardecl multi line single var"""
        input = """var a, b: real;
                c,d,e: real;
                s: string;
                f: boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 203))

    def test_vardecl_multi_line_multi_var(self):
        """test vardecl multi line multi var"""
        input = """var a, b: real;
                var c,d,e: real;
                var s: string;
                var f: boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 204))

    def test_vardecl_array(self):
        """test vardecl array"""
        input = """var a, b: array[1 .. 3] of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 205))
    
    def test_vardecl_array_negative_index(self):
        """test vardecl array negative index"""
        input = """
        var 
            abktuc: array [-1 .. 4] of real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 206))

    def test_vardecl_error_array_exp_index(self):
        """test vardecl error array exp index"""
        input = """
        var str: string;
            f57: array [-1 + 2 .. 7 - 3] of string;"""
        expect = "Error on line 3 col 27: +"
        self.assertTrue(TestParser.test(input,expect, 207))

    def test_vardecl_error_array_exp_index2(self):
        """test vardecl error array exp index2"""
        input = """
        var abc: array [x * 5 .. y] of real;
        """
        expect = "Error on line 2 col 24: x"
        self.assertTrue(TestParser.test(input,expect, 208))

    def test_vardecl_array_error_doubledot(self):
        """test vardecl array error doubledot"""
        input = """var a , b , c : real ;
            d : array [ 1 . . 5 ] of real ;
            e , f : real ;"""
        expect = "."
        self.assertTrue(TestParser.test(input,expect, 209))

    def test_vardecl_array_error_doubledot2(self):
        """test vardecl array error doubledot2"""
        input = """
        var abc: array [1..5] of string;
        """
        expect = "Error on line 2 col 24: 1."
        self.assertTrue(TestParser.test(input,expect, 210))

    def test_vardecl_array_error_type(self):
        """test vardecl array error type"""
        input = """
        var test: array [7 .. 9]// of real;
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect, 211))

    def test_vardecl_in_complex_stmt(self):
        """test vardecl in complex stmt"""
        input = """
        var num: real;
        procedure foo(a: real) ;
		begin
            var arr: real;
        end
        """
        expect = "Error on line 5 col 12: var"
        self.assertTrue(TestParser.test(input,expect, 212))









    def test_funcdecl_return_array(self):
        """test funcdecl return array"""
        input = """
        function htr(ab: string): array [1 .. 3] of real;
        begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 213))

    def test_funcdecl_vardecl(self):
        """test funcdecl vardecl"""
        input = """
        FUNcTION hfgsh(a, b: real; fsd:string):array [1 .. 2] of real ;
        var gfd,htyujyt: real ;
        begin
        
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 214))
    
    def test_procdecl_simple(self):
        """test procdecl simple"""
        input = """
        procedure _fsdf(a: real);
        var jyt,ytry: real ;
        begin
        
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 215))

    def test_funcdecl_error_no_return(self):
        """test funcdecl error no return"""
        input = """
        FUNction foo(fsd7d,gdfg78df: real);
        begin

        end
        """
        expect = "Error on line 2 col 42: ;"
        self.assertTrue(TestParser.test(input,expect, 216))

    def test_procdecl_vardecl(self):
        """test procdecl vardecl"""
        input = """
        procedure htrh();
        var hdtu,tyer: strinG;
        begin
        
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 217))

    def test_procdecl_error_return(self):
        """test procdecl error return"""
        input = """
        procedure ggdfg(): string;
        var x, y: string;
            z: real;
        begin
        end"""
        expect = "Error on line 2 col 25: :"
        self.assertTrue(TestParser.test(input,expect, 218))

    def test_procdecl_error_compstmt_no_begin(self):
        """test procdecl error compstmt no begin"""
        input = """
        procedure hfgjhf();
        var yyt,terte: string;
        
        end"""
        expect = "Error on line 5 col 8: end"
        self.assertTrue(TestParser.test(input,expect, 219))
    
    def test_funcdecl_error_compstmt_no_end(self):
        """test funcdecl error compstmt no end"""
        input = """
        function htrhrj(): real
        begin
        
        """
        expect = "Error on line 3 col 8: begin"
        self.assertTrue(TestParser.test(input,expect, 220))

    def test_procdecl_error_parameter2(self):
        """test procdecl error parameter2"""
        input = """
        procedure Main(grre: real : string;
        begin 
        end

        """
        expect = "Error on line 2 col 34: :"
        self.assertTrue(TestParser.test(input,expect, 221))

    def test_funcdecl_error_parameter(self):
        """test funcdecl error parameter"""
        input = """
        function gd7845Y;
        begin
        end
        """
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.test(input,expect, 222))

    def test_procdecl_error_parameter(self):
        """test procdecl error parameter"""
        input = """
        procedure hyhfg): string; 
        begin
        
        end
        """
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.test(input,expect, 223))

    def test_procdecl_error_no_sm(self):
        """test procdecl error no sm"""
        input = """
        procedure gfdgdfg() 
        var x: real; 
        begin end
        """
        expect = "Error on line 3 col 8: var"
        self.assertTrue(TestParser.test(input,expect, 224))

    def test_funcdecl_error_no_sm(self):
        """test funcdecl error no sm"""
        input = """
        FUNCtion __gfdgdfg(a: string): real
        begin       end
        """
        expect = "Error on line 3 col 8: begin"
        self.assertTrue(TestParser.test(input,expect, 225))

    def test_funcdecl_error_parameter_type(self):
        """test funcdecl error parameter type"""
        input = """
        FUNCtion gtg(xfds): real;
        begin end
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.test(input,expect, 226))

    def test_funcdecl_error_parameter_sm(self):
        """test funcdecl error parameter sm"""
        input = """
        function fdsaf(fds: string;): strING;
        begin
        
        end
        """
        expect = "Error on line 2 col 34: ;"
        self.assertTrue(TestParser.test(input,expect, 227))

    def test_funcdecl_error_vardecl(self):
        """test funcdecl error vardecl"""
        input = """
        var a:real;
        procedure foo(); 
	    x, hghhgh:string;
		regfd: real;
	    begin 
	    end
	    """
        expect = "Error on line 4 col 5: x"
        self.assertTrue(TestParser.test(input,expect, 228))

    def test_funcdecl_error_vardecl_sm(self):
        """test funcdecl error vardecl sm"""
        input = """
        var fdas: strING;
        function jtyjty( ) :  string;
        var x,y: real
        begin
            procedure grg();
        	begin
                
            end
        end
        """
        expect = "Error on line 5 col 8: begin"
        self.assertTrue(TestParser.test(input,expect, 229))

    def test_procdecl_error_multi_var(self):
        """test procdecl error multi var"""
        input = """
        procedure gg(); 
	    var retr: string;
		var ut,ytry: real;
	    begin 
	    end"""
        expect = "Error on line 4 col 2: var"
        self.assertTrue(TestParser.test(input,expect, 230))

    def test_procdecl_error_var_parameter(self):
        """test procdecl error var parameter"""
        input = """
        procedure fds(var fdfd: string);    
	    begin end
	    """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input,expect, 231))
    
    def test_procdecl_error_no_implement(self):
        """test procdecl error no implement"""
        input = """
        procedure htr();
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect, 232))







    def test_assignstmt_in_procdecl(self):
        """test assignstmt in procdecl"""
        input = """
        procedure foo(a: real) ;
        begin
            x := 1;
            ghj := a[12] ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 233))
    
    def test_assignstmt_in_funcdecl(self):
        """test assignstmt in funcdecl"""
        input = """
        function f(): real; 
        begin
            aof := "ghgh";
            m := n := func(1,a+1) ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 234))
    
    def test_assignstmt_error_lhs(self):
        """test assignstmt error lhs"""
        input = """
        procedure foo(a: real) ;
        var num: string ;
        begin
            3 := t;
            a[1][1] := t[12] ;
        end
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect, 235))
    
    def test_assignstmt_complex(self):
        """test assignstmt complex"""
        input = """
        function foo(): real ;
        var arr: array[1 .. 2] of real;
        begin
            g[b - c] := a[m/2] ;
            a()[m*n] := a[a + 3] ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 236))
   
    def test_assignstmt_complex2(self):
        """test assignstmt complex2"""
        input = """
        function foo(num: real): real ;
        begin
            tmp[m+n] := foo()[m*1] := abc[a div 2] := (p > 0) or else (m<=k);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 237))
    
    def test_assignstmt_error_rp(self):
        """test assignstmt error rp"""
        input = """
        procedure gdfg(); 
	    begin
	    x := ehg[2]  := fix();
	    a := b := c = kug());
	    end
	    """
        expect = "Error on line 5 col 24: )"
        self.assertTrue(TestParser.test(input,expect, 238))

    def test_assignstmt_arror_sm(self):
        """test assignstmt arror sm"""
        input = """
        procedure yre(); 
	    begin
	        n := tre, arr[1] := gfhg();
	    end
	    """
        expect = "Error on line 4 col 17: ,"
        self.assertTrue(TestParser.test(input,expect, 239))





    def test_ifstmt_simple(self):
        """test ifstmt simple"""
        input = """
        function test(g, h: string): string ;
        begin
            if(g > h) then h[2]:= h+1 ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 240))
    
    def test_ifstmt_else(self):
        """test ifstmt else"""
        input = """
        procedure foo() ;
        begin
            if(x * y > m) then x := y*2 ;
            else x := y+2;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 241))
    
    def test_ifstmt_else_complex(self):
        """test ifstmt else complex"""
        input = """
        funCtioN aaa(num: string): real ;
        begin
            if(t>1) then a:=1 ;
            else if (t<5)=(a<t) then t:= t + i ;
            else aaa(a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 242))
    
    def test_ifstmt_else_complex2(self):
        """test ifstmt else complex2"""
        input = """
        procedure aaa(t: real) ;
        var a: real ;
        begin
            if(a>1) then a:= a/2 ;
            if (t[1]< tmp[2]) then begin t[1]:=i ; end
            else aaa(x);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 243))
    
    def test_ifstmt_else_complex3(self):
        """test ifstmt else complex3"""
        input = """
        function f(t: real): string ;
        begin
            if(a>1) then a:= a/2 ;
            else if (t[1]< t[2]) then begin t[1]:=i ; end
            else if (t > 0) then f(x);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 244))
    
    def test_ifstmt_error_no_begin(self):
        """test ifstmt error no begin"""
        input = """
        function aaa(ttt: real): string ;
        begin
            if(tmp>1) then 
                g:=1 ;
                if(a <> b ) then a[1]:= t[1];
                else y:=z[1]:= 1;
            end
        end
        """
        expect = "Error on line 9 col 8: end"
        self.assertTrue(TestParser.test(input,expect, 245))
    
    def test_ifstmt_error_exp(self):
        """test ifstmt error exp"""
        input = """
		procedure aaa( );
        begin
            if () then return a ; //CORRECT
            else return b ;
        end
        """
        expect = "Error on line 4 col 16: )"
        self.assertTrue(TestParser.test(input,expect, 246))

    def test_ifstmt_error_missing_then(self):
        """test ifstmt error missing then"""
        input = """
            procedure gdfht();
            begin
              If k mod 16 = 0 then t:="0"+t ;
              else If k mod 16 = 1 then t:="1"+t;
              else If k mod 16 = 2  t:="2"+t;
             end
            end
            """
        expect = "Error on line 6 col 36: t"
        self.assertTrue(TestParser.test(input, expect, 247))







    def test_whilestmt_simple1(self):
        """test whilestmt simple1"""
        input = """
        procedure aaa() ;
        var a,b: string ;
        begin
            while(t<>a) do begin 
                a:= b*2; 
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 248))
    
    def test_whilestmt_simple2(self):
        """test whilestmt simple2"""
        input = """
        funcTION aaaa(): real ;
        var a1,a2:real ;
        begin
            WhiLe(a1<>a2) do begin
                if(a1 = a2) then t:=1;
                foo(t);
            end end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 249))
    
    def test_whilestmt_simple3(self):
        """test whilestmt simple3"""
        input = """
        procedure aaa(arr: real) ;
        var a,b: real ;
        begin
            WHILE(t<>1) do begin
                while(x) do a:= a+2;
                end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 250))
    
    def test_whilestmt_error_end(self):
        """test whilestmt error end"""
        input = """
        procedure aaa(t: real) ;
        begin
            WhiLe(t<>1) do begin
                while(0) do a:= t;
                    if(t < n) then begin t := t*2 end
            end
        end"""
        expect = "Error on line 6 col 50: end"
        self.assertTrue(TestParser.test(input,expect, 251))

    def test_whilestmt_error_sm(self):
        """test whilestmt error sm"""
        input = """
        procedure a();
        begin
			while n>10 do ;
            a := t := foo(); 
        end"""
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.test(input,expect, 252))

    def test_whilestmt_error_condition(self):
        """test whilestmt error condition"""
        input = """
        procedure a();
        begin
			while n==10 do ;
            a := t := foo(); 
        end"""
        expect = "Error on line 4 col 11: ="
        self.assertTrue(TestParser.test(input,expect, 253))






    def test_withstmt_simple1(self):
        """test withstmt simple1"""
        input = """
        procedure aaa() ;
        begin
            with a,a,aa :real ; str : array [1 .. 2] of string ; do
            t := a[t*3] / 2 + g ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 254))
    
    def test_withstmt_simple2(self):
        """test withstmt simple2"""
        input = """
        procedure aaaa() ;
        var t: real;
        begin
            with num : real; a: real; do begin
                sort(a);
                sum(a,b,c);
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 255))
    
    def test_withstmt_simple3(self):
        """test withstmt simple3"""
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 256))
    
    def test_withstmt_error_type(self):
        """test withstmt error type"""
        input = """
        function f(): real;
        begin
        with num real, a : array [1 .. 2] of string ; do
            sort(arr);  sum(x, y, z);
        end
        """
        expect = "Error on line 4 col 17: real"
        self.assertTrue(TestParser.test(input,expect, 257))
    
    def test_withstmt_error_sm(self):
        """test withstmt error sm"""
        input = """
        procedure f(); 
	    begin
		    with a,b: real;; do with a: array [1 .. 56] of real; do n := a*b; 
		    with x:string; do with str: string; do x := str;
	    end"""
        expect = "Error on line 4 col 21: ;"
        self.assertTrue(TestParser.test(input,expect, 258))

    def test_withstmt_error_missing_do(self):
        """test withstmt error missing do"""
        input = """procedure f(); 
	   	begin
	        with a: real;  if (t > 0) then a:= a+ t;
	    end
	    """
        expect = "Error on line 3 col 24: if"
        self.assertTrue(TestParser.test(input,expect, 259))

    def test_withstmt_complex(self):
        """test withstmt complex"""
        input = """procedure foo(c: real) ;
        begin
            with a1, a2 : real ; c : array [1 .. 2] of real ; do begin
                d := c [a] + b ; foo();foo1(a,b,c);
                with a , b : real ; do begin
                    foo2(a,b,"anc");
            end
        end
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 260))








    def test_forstmt_simple1(self):
        """test forstmt simple1"""
        input = """function aaaa(c: real): real;
                   begin
                    FOR i:=1 to t+10 do 
                        t := t + 1; end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 261))

    def test_forstmt_simple2(self):
        """test forstmt simple2"""
        input = """function aaa(c: string): real;
                   begin
                    FOR i:=1 to t+10 do begin
                        t := t + 1;
                        if(a=1) then t:=t-1;
                    end
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 262))

    def test_forstmt_downto_simple1(self):
        """test forstmt downto simple1"""
        input = """function fa(c: string): real;
                   begin
                    FOR i:=1 to g+10 do 
                    begin
                        for j:=m+1 doWnTO 100 do 
                        begin
                            t := t + 1;
                            if(a=1) then g:=g-1;
                        end
                    end
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 263))
        
    def test_forstmt_downto_simple2(self):
        """test forstmt downto simple2"""
        input = """procedure aaa(x: string);
                   begin
                    for x:=1 to x+10 do 
                        begin
                        while i>1 do
                            for i:=x+1 doWnTO 10 do
                                while j>1 do y:=func(10);
                    end
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 264))







    def test_breakstmt(self):
        """test breakstmt"""
        input = """procedure aaa();
                   begin
                    for i:=1 downto 343 do begin
                        break;
                    end end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 265))
    def test_continuestmt(self):
        """test continuestmt"""
        input = """procedure a();
                   begin
                    while (true) do continue ;
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 266))
    def test_returnstmt1(self):
        """test returnstmt1"""
        input = """procedure a();
                   begin
                    while (true) do return ;
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 267))
    def test_returnstmt2(self):
        """test returnstmt2"""
        input = """function aaa(): real;
                begin
                   return aaa(t+1);
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 268))
    def test_compstmt(self):
        """test compstmt"""
        input = """function foo(): boolean;
                   begin
                    while (x = 345) do begin end
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 269))
    def test_callstmt1(self):
        """test callstmt1"""
        input = """function aaa(): boolean;
                   begin
                    foo (3,a+1);
                    foo1();
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 270))
    def test_callstmt2(self):
        """test callstmt2"""
        input = """function foo(): real; begin
                    foo(3,t+343,t<>5,t[10]);
                    return 1;
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 271))
    def test_callstmt3(self):
        """test callstmt3"""
        input = """function aaa(): boolean;
                   begin
                    foo(3,t,x and then y,a[1],foo(4324)[634+543]);
                    return foo2();
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 272))
    def test_callstmt4(self):
        """test callstmt4"""
        input = """function aaa(): string;
                   begin
                    a(3,a(a(foo(2,34))));
                    return aaa(a(3423));
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 273))
    def test_callstmt5(self):
        """test callstmt5"""
        input = """function aaa(): real;
                   begin
                    set(brown); { seta }
                    return func(t(1,2,4));
                   end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 274))





    def test_eof_program(self):
        """test eof program"""
        input = """var i: real;
               )()"""
        expect = "Error on line 2 col 15: )"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_empty_program(self):
        """test empty program"""
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 276))


    





    def test_program_complex1(self):
        """test program complex1"""
        input = """
        var i: real ;
        function func(): real;
        begin
            return s(arr);
        end
        procedure main() ;
        var main: real ;
        begin
            m := f() ;
            putIntLn(m);
            with i: real; main: real; do begin
                m := i:= sum(a,b);
                put (i);
            end
        end
        var str: real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 277))

    def test_program_complex2(self):
        """test program complex2"""
        input = """
                var i: real ;
                function f(): real ;
                begin
                   return 353;
                end
                procedure main() ;
                var
                   main: real ;
                begin
                   main := f() ;
                   putIntLn(main);
                   with
                        i: real;
                        m: real;
                        f: real;
                   do begin
                        a := b [ 10 ] := foo ( ) [ 3 ] := x := 1 ;
                        main := f := i:= 100;
                        f (i);
                        f (main );
                        f (f);
                   end
                   putIntLn (main);
                end
                var g: real ;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 278))

    def test_program_complex3(self):
        """test program complex3"""
        input = """
                Var name, surname: String;
                procedure Main();
                begin
                   print("Nhap ten cua ban:");
                   readfromfile(name);
                   print("Nhap ho cua ban:");
                   readfromfile(surname);
                   println();(*new line*)
                   println();//new line}
                   println("Ten day du cua ban la : ",name," ",surname);
                   readfromfile();
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 279))

    def test_program_complex4(self):
        """test program complex4"""
        input = """Procedure InsertionSort();
            Var i,j: real;
            Begin
                For i:=2 to n do
                Begin
                    j:=i;
                    While (j>1) and (a[j]<a[j-1]) do
                    Begin
                        Swap (a[j],a[j-1]);
                        j:=j-1;
                    End
                End
            End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 280))

    def test_program_complex5(self):
        """test program complex5""" 
        input = """
                Var PD, Dname, Cmodel : String;
                CostPD, TCostPD, Distance : real;
                {real is a decimal (described later on)}
                procedure main();
                begin
                    textbackground(brown); {background colour}
                    clearScreen(); {Clear screen with a brown colour. Try run the program without this..}
                    TextColor(lightgreen); {text colour}
                    TCostPD := 0;
                    println("This program prompts you to input the cost per litre of");
                    println("the petrol/diesel you spend in and the average distance you travel");
                    println("with your car every week. Then, the computer calculates the total cost");
                    println("you spend in fuel every week.");
                    Readkey(); {program move on as soon as a key is pressed}
                    clearScreen(); {short for clear screen}
                    GotoXy(28,3); {move to a position on the screen: x (horizontal), y (vertical)}
                    readfromfile();
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 281))
    def test_program_complex6(self):
        """test program complex6"""
        input = """
                procedure main() ;
                begin
                 a[b[2]] := 10;
                 foo();
                 return ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 282))
    def test_program_complex7(self):
        """test program complex7""" 
        input = """
                procedure main() ;
                begin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 283))
    def test_program_complex8(self):
        """test program complex8"""
        input = """
                procedure main() ;
                var a: array[0 .. -1] of real;
                 i,j,temp: real;
                begin
                    for i := 0 to n - 2 do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then begin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            end
                    print(a);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 284))

    def test_program_complex9(self):
        """test program complex9""" 
        input = """
                procedure NhapMang1C(A : array[0 .. 10] of real;N:real);
                Var i: real;
                begin
                print("So luong phan tu:");
                readfromfile( N);
                For i:=0 to N do
                    begin
                        print("Nhap phan tu thu", i," ");
                        readfromfile( A[i] );
                    end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 285))

    def test_program_complex10(self):
        """test program complex10""" 
        input = """
                Function Tong_So_Chia_Het_Cho5(A:array[0 .. 10] of real ; N:real):real;
                Var S,i :real;
                begin
                    S:=0;
                    For i:=0 to N do
                    If(A[i] mod 5=0) then
                    S := S+A[i];
                    return S;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 286))

    def test_program_complex11(self):
        """test program complex11""" 
        input = """
                Function LaSoNT(N:real) :real;
                Var i:real;
                begin
                 For i:=2 to N-1 do
                  If(N mod i = 0) then
                    return 0;
                  else
                    return 1;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 287))
    def test_program_complex12(self):
        """test program complex12""" 
        input = """
                Function DemPtuX(A:array[0 .. 10] of real; N,X : real) : real;
                Var i , Count : real;
                begin
                 Count := 0;
                 For i:=0 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 288))
    def test_program_complex13(self):
        """test program complex13"""
        input = """
                procedure ThayTheTatCa (A:array[0 .. 10] of real;N, x,y:real);
                Var i:real;
                begin
                 For i:=0 to N do
                  If(A[i] = x) then { Tim thay x ==> thay the thanh y }
                  A[i] := y;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 289))
    def test_program_complex14(self):
        """test program complex14""" 
        input = """
                procedure ThayTheBangTong(A:array[0 .. 10] of real; N:real; X, Y:real);
                Var i,k:real;
                begin
                 For i:=0 to N do
                 If( (A[i-1]+A[i]) mod 10 = 0) then
                 begin
                  k := (A[i-1]+A[i]);
                  A[i-1] := k;
                  A[i] := k;
                 end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 290))
    def test_program_complex15(self):
        """test program complex15"""
        input = """
                Function KtraDoiXung (A:array[0 .. 10] of real; N:real ) : Boolean;
                Var Flag:Boolean;
                    i :real;
                begin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                 return flag;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 291))
    def test_program_complex16(self):
        input = """
                Function KtraMangTang ( A:array[0 .. 10] of real; N :real) : Boolean;
                Var Flag : Boolean;
                 i :real;
                begin
                 Flag := True;
                 i:= 0;
                 while(i<n) do begin
                  If(A[i] < A[i-1]) Then
                   Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                  i:=i+1;
                 end
                 return Flag;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 292))
    def test_program_complex17(self):
        """test program complex17"""
        input = """
                Function KtraMangCapSoCong (A: khongPhaiType;  N:real; k:real):Boolean;
                Var flag :boolean;
                i :real;
                begin
                 for i:=1 to N do
                 if(A[i] <> A[i-1] + k) then
                  flag:=false;     // Cham dut, ket qua: khong phai
                 return flag; {Ket qua kiem tra la mang cap so cong}
                end
                """
        expect = "Error on line 2 col 47: khongPhaiType"
        self.assertTrue(TestParser.test(input,expect, 293))
    def test_program_complex18(self):
        """test program complex18"""
        input = """
                procedure ChenPhanTu(A:array[0 .. 10] of real;N: real; k, X:real);
                Var i :real;
                begin
                 For i:=N downto k+ 1 do
                  A[i] := A[i-1];
                 A[k] := X;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 294))
    def test_program_complex19(self):
        """test program complex19"""
        input = """
                function gt(x:real):real;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 295))
    def test_program_complex20(self):
        """test program complex20"""
        input = """
                function fibo(x: real): real;
                var f1,f2: real;
                begin
                 if x<=2 then
                  return 1;
                 else
                  return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 296))
    def test_program_complex21(self):
        """test program complex21"""
        input = """
                function ok(i : real):boolean;
                var k : real;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if cp(s,i-2*k+1,k) = cp(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 297))
    def test_program_complex22(self):
        """test program complex22"""
        input = """
                procedure find(n: real);
                begin
                 Assign(f,fo);
                  Reprint(f);
                 If n > 0 then
                  begin
                  print(f,n mod 10);
                  find(n div 10);
                  end
                 Close(f);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 298))
    def test_program_complex23(self):
        """test program complex23"""
        input = """
                Function findNumber(m,n:real):real;
                begin
                 If(m=n) then RETURN m ;
                 else
                  If (m>n) then return findNumber(m-n,n);
                  else return findNumber(m,n-m);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 299))
    def test_program_complex24(self):
        """test program complex24"""
        input = """
                Var r,dt,cv:real;
                procedure main() ;
                begin
                 clearScreen();
                 println("TINH DIEN TICH & CHU VI HINH TRON:");
                 println("--------------------------------------------------");
                 print ("Nhap ban kinh R="); readfromfile(r);
                 dt:=pi*r*r;
                 cv:=2*pi*r;
                 println("Dien tich hinh tron la:",dt);
                 println("Chu vi hinh tron la:",cv);
                 readfromfile();
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 300))
    
# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardecblock.
    def visitVardecblock(self, ctx:MPParser.VardecblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardec.
    def visitVardec(self, ctx:MPParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listofid.
    def visitListofid(self, ctx:MPParser.ListofidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#twotype.
    def visitTwotype(self, ctx:MPParser.TwotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#pritype.
    def visitPritype(self, ctx:MPParser.PritypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraytype.
    def visitArraytype(self, ctx:MPParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexlist.
    def visitIndexlist(self, ctx:MPParser.IndexlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdec.
    def visitFuncdec(self, ctx:MPParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paralist.
    def visitParalist(self, ctx:MPParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paradec.
    def visitParadec(self, ctx:MPParser.ParadecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returntype.
    def visitReturntype(self, ctx:MPParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#prodec.
    def visitProdec(self, ctx:MPParser.ProdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstmt.
    def visitAssignstmt(self, ctx:MPParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vari.
    def visitVari(self, ctx:MPParser.VariContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstmt.
    def visitIfstmt(self, ctx:MPParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestmt.
    def visitWhilestmt(self, ctx:MPParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstmt.
    def visitForstmt(self, ctx:MPParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#chooseassign.
    def visitChooseassign(self, ctx:MPParser.ChooseassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstmt.
    def visitBreakstmt(self, ctx:MPParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestmt.
    def visitContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstmt.
    def visitReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstmt.
    def visitCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstmt.
    def visitWithstmt(self, ctx:MPParser.WithstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstmt.
    def visitCallstmt(self, ctx:MPParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#explist.
    def visitExplist(self, ctx:MPParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression1.
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression2.
    def visitExpression2(self, ctx:MPParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression3.
    def visitExpression3(self, ctx:MPParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression4.
    def visitExpression4(self, ctx:MPParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression5.
    def visitExpression5(self, ctx:MPParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression6.
    def visitExpression6(self, ctx:MPParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funccall.
    def visitFunccall(self, ctx:MPParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literals.
    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        return self.visitChildren(ctx)



del MPParser
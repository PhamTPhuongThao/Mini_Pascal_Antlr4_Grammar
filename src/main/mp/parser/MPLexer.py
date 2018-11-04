# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0249\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u00ca\n\b\f\b\16\b\u00cd\13\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\7\t\u00d6\n\t\f\t\16\t\u00d9\13\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\7\n\u00e3\n\n\f\n\16\n\u00e6")
        buf.write("\13\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\39\39\39\39\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\6P\u01dd\nP\rP\16")
        buf.write("P\u01de\3P\7P\u01e2\nP\fP\16P\u01e5\13P\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3Q\5Q\u01f0\nQ\3R\6R\u01f3\nR\rR\16R\u01f4")
        buf.write("\3S\3S\3S\7S\u01fa\nS\fS\16S\u01fd\13S\3S\5S\u0200\nS")
        buf.write("\3S\3S\3S\5S\u0205\nS\3S\3S\3S\5S\u020a\nS\3T\3T\3T\7")
        buf.write("T\u020f\nT\fT\16T\u0212\13T\3T\3T\3T\3U\3U\5U\u0219\n")
        buf.write("U\3U\6U\u021c\nU\rU\16U\u021d\3V\6V\u0221\nV\rV\16V\u0222")
        buf.write("\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\7Y\u0230\nY\fY\16Y\u0233")
        buf.write("\13Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\7Z\u0240\nZ\fZ\16")
        buf.write("Z\u0243\13Z\3Z\5Z\u0246\nZ\3Z\3Z\5\u00cb\u00d7\u0231\2")
        buf.write("[\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31")
        buf.write("\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65")
        buf.write("\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\fK\rM\16O\17Q\20S\21")
        buf.write("U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m\36o")
        buf.write("\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089")
        buf.write(",\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097")
        buf.write("\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a18\u00a39")
        buf.write("\u00a5:\u00a7;\u00a9\2\u00ab<\u00ad\2\u00af=\u00b1>\u00b3")
        buf.write("?\3\2\'\4\2\f\f\17\17\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff")
        buf.write("\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2M")
        buf.write("Mmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4")
        buf.write("\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZz")
        buf.write("z\4\2[[{{\4\2\\\\||\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;")
        buf.write("\b\2\f\f\17\17$$GHQQ^^\5\2\13\f\16\17\"\"\n\2$$))^^dd")
        buf.write("hhppttvv\4\2$$^^\3\2^^\5\2\f\f\17\17$$\3\3\f\f\2\u0242")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\3\u00b5")
        buf.write("\3\2\2\2\5\u00b8\3\2\2\2\7\u00bb\3\2\2\2\t\u00bd\3\2\2")
        buf.write("\2\13\u00c0\3\2\2\2\r\u00c2\3\2\2\2\17\u00c5\3\2\2\2\21")
        buf.write("\u00d3\3\2\2\2\23\u00de\3\2\2\2\25\u00e9\3\2\2\2\27\u00eb")
        buf.write("\3\2\2\2\31\u00ed\3\2\2\2\33\u00ef\3\2\2\2\35\u00f1\3")
        buf.write("\2\2\2\37\u00f3\3\2\2\2!\u00f5\3\2\2\2#\u00f7\3\2\2\2")
        buf.write("%\u00f9\3\2\2\2\'\u00fb\3\2\2\2)\u00fd\3\2\2\2+\u00ff")
        buf.write("\3\2\2\2-\u0101\3\2\2\2/\u0103\3\2\2\2\61\u0105\3\2\2")
        buf.write("\2\63\u0107\3\2\2\2\65\u0109\3\2\2\2\67\u010b\3\2\2\2")
        buf.write("9\u010d\3\2\2\2;\u010f\3\2\2\2=\u0111\3\2\2\2?\u0113\3")
        buf.write("\2\2\2A\u0115\3\2\2\2C\u0117\3\2\2\2E\u0119\3\2\2\2G\u011b")
        buf.write("\3\2\2\2I\u011d\3\2\2\2K\u0121\3\2\2\2M\u012a\3\2\2\2")
        buf.write("O\u0134\3\2\2\2Q\u013a\3\2\2\2S\u013d\3\2\2\2U\u0145\3")
        buf.write("\2\2\2W\u014d\3\2\2\2Y\u0152\3\2\2\2[\u0159\3\2\2\2]\u015e")
        buf.write("\3\2\2\2_\u0164\3\2\2\2a\u0167\3\2\2\2c\u016c\3\2\2\2")
        buf.write("e\u0171\3\2\2\2g\u0177\3\2\2\2i\u017a\3\2\2\2k\u017e\3")
        buf.write("\2\2\2m\u0181\3\2\2\2o\u0188\3\2\2\2q\u018e\3\2\2\2s\u0197")
        buf.write("\3\2\2\2u\u019e\3\2\2\2w\u01a4\3\2\2\2y\u01a8\3\2\2\2")
        buf.write("{\u01ad\3\2\2\2}\u01b1\3\2\2\2\177\u01b4\3\2\2\2\u0081")
        buf.write("\u01b8\3\2\2\2\u0083\u01bc\3\2\2\2\u0085\u01c0\3\2\2\2")
        buf.write("\u0087\u01c2\3\2\2\2\u0089\u01c4\3\2\2\2\u008b\u01c6\3")
        buf.write("\2\2\2\u008d\u01c8\3\2\2\2\u008f\u01ca\3\2\2\2\u0091\u01cc")
        buf.write("\3\2\2\2\u0093\u01ce\3\2\2\2\u0095\u01d0\3\2\2\2\u0097")
        buf.write("\u01d2\3\2\2\2\u0099\u01d4\3\2\2\2\u009b\u01d6\3\2\2\2")
        buf.write("\u009d\u01d8\3\2\2\2\u009f\u01dc\3\2\2\2\u00a1\u01ef\3")
        buf.write("\2\2\2\u00a3\u01f2\3\2\2\2\u00a5\u0209\3\2\2\2\u00a7\u020b")
        buf.write("\3\2\2\2\u00a9\u0216\3\2\2\2\u00ab\u0220\3\2\2\2\u00ad")
        buf.write("\u0226\3\2\2\2\u00af\u0229\3\2\2\2\u00b1\u022c\3\2\2\2")
        buf.write("\u00b3\u0239\3\2\2\2\u00b5\u00b6\7<\2\2\u00b6\u00b7\7")
        buf.write("?\2\2\u00b7\4\3\2\2\2\u00b8\u00b9\7>\2\2\u00b9\u00ba\7")
        buf.write("@\2\2\u00ba\6\3\2\2\2\u00bb\u00bc\7>\2\2\u00bc\b\3\2\2")
        buf.write("\2\u00bd\u00be\7>\2\2\u00be\u00bf\7?\2\2\u00bf\n\3\2\2")
        buf.write("\2\u00c0\u00c1\7@\2\2\u00c1\f\3\2\2\2\u00c2\u00c3\7@\2")
        buf.write("\2\u00c3\u00c4\7?\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7*")
        buf.write("\2\2\u00c6\u00c7\7,\2\2\u00c7\u00cb\3\2\2\2\u00c8\u00ca")
        buf.write("\13\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00ce\3\2\2\2")
        buf.write("\u00cd\u00cb\3\2\2\2\u00ce\u00cf\7,\2\2\u00cf\u00d0\7")
        buf.write("+\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\b\b\2\2\u00d2\20")
        buf.write("\3\2\2\2\u00d3\u00d7\7}\2\2\u00d4\u00d6\13\2\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00da\u00db\7\177\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00dd\b\t\2\2\u00dd\22\3\2\2\2\u00de\u00df\7\61\2\2\u00df")
        buf.write("\u00e0\7\61\2\2\u00e0\u00e4\3\2\2\2\u00e1\u00e3\n\2\2")
        buf.write("\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e7\u00e8\b\n\2\2\u00e8\24\3\2\2\2\u00e9")
        buf.write("\u00ea\t\3\2\2\u00ea\26\3\2\2\2\u00eb\u00ec\t\4\2\2\u00ec")
        buf.write("\30\3\2\2\2\u00ed\u00ee\t\5\2\2\u00ee\32\3\2\2\2\u00ef")
        buf.write("\u00f0\t\6\2\2\u00f0\34\3\2\2\2\u00f1\u00f2\t\7\2\2\u00f2")
        buf.write("\36\3\2\2\2\u00f3\u00f4\t\b\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\t\t\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\t\n\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\t\13\2\2\u00fa&\3\2\2\2\u00fb\u00fc")
        buf.write("\t\f\2\2\u00fc(\3\2\2\2\u00fd\u00fe\t\r\2\2\u00fe*\3\2")
        buf.write("\2\2\u00ff\u0100\t\16\2\2\u0100,\3\2\2\2\u0101\u0102\t")
        buf.write("\17\2\2\u0102.\3\2\2\2\u0103\u0104\t\20\2\2\u0104\60\3")
        buf.write("\2\2\2\u0105\u0106\t\21\2\2\u0106\62\3\2\2\2\u0107\u0108")
        buf.write("\t\22\2\2\u0108\64\3\2\2\2\u0109\u010a\t\23\2\2\u010a")
        buf.write("\66\3\2\2\2\u010b\u010c\t\24\2\2\u010c8\3\2\2\2\u010d")
        buf.write("\u010e\t\25\2\2\u010e:\3\2\2\2\u010f\u0110\t\26\2\2\u0110")
        buf.write("<\3\2\2\2\u0111\u0112\t\27\2\2\u0112>\3\2\2\2\u0113\u0114")
        buf.write("\t\30\2\2\u0114@\3\2\2\2\u0115\u0116\t\31\2\2\u0116B\3")
        buf.write("\2\2\2\u0117\u0118\t\32\2\2\u0118D\3\2\2\2\u0119\u011a")
        buf.write("\t\33\2\2\u011aF\3\2\2\2\u011b\u011c\t\34\2\2\u011cH\3")
        buf.write("\2\2\2\u011d\u011e\5? \2\u011e\u011f\5\25\13\2\u011f\u0120")
        buf.write("\5\67\34\2\u0120J\3\2\2\2\u0121\u0122\5\37\20\2\u0122")
        buf.write("\u0123\5=\37\2\u0123\u0124\5/\30\2\u0124\u0125\5\31\r")
        buf.write("\2\u0125\u0126\5;\36\2\u0126\u0127\5%\23\2\u0127\u0128")
        buf.write("\5\61\31\2\u0128\u0129\5/\30\2\u0129L\3\2\2\2\u012a\u012b")
        buf.write("\5\63\32\2\u012b\u012c\5\67\34\2\u012c\u012d\5\61\31\2")
        buf.write("\u012d\u012e\5\31\r\2\u012e\u012f\5\35\17\2\u012f\u0130")
        buf.write("\5\33\16\2\u0130\u0131\5=\37\2\u0131\u0132\5\67\34\2\u0132")
        buf.write("\u0133\5\35\17\2\u0133N\3\2\2\2\u0134\u0135\5\25\13\2")
        buf.write("\u0135\u0136\5\67\34\2\u0136\u0137\5\67\34\2\u0137\u0138")
        buf.write("\5\25\13\2\u0138\u0139\5E#\2\u0139P\3\2\2\2\u013a\u013b")
        buf.write("\5\61\31\2\u013b\u013c\5\37\20\2\u013cR\3\2\2\2\u013d")
        buf.write("\u013e\5%\23\2\u013e\u013f\5/\30\2\u013f\u0140\5;\36\2")
        buf.write("\u0140\u0141\5\35\17\2\u0141\u0142\5!\21\2\u0142\u0143")
        buf.write("\5\35\17\2\u0143\u0144\5\67\34\2\u0144T\3\2\2\2\u0145")
        buf.write("\u0146\5\27\f\2\u0146\u0147\5\61\31\2\u0147\u0148\5\61")
        buf.write("\31\2\u0148\u0149\5+\26\2\u0149\u014a\5\35\17\2\u014a")
        buf.write("\u014b\5\25\13\2\u014b\u014c\5/\30\2\u014cV\3\2\2\2\u014d")
        buf.write("\u014e\5\67\34\2\u014e\u014f\5\35\17\2\u014f\u0150\5\25")
        buf.write("\13\2\u0150\u0151\5+\26\2\u0151X\3\2\2\2\u0152\u0153\5")
        buf.write("9\35\2\u0153\u0154\5;\36\2\u0154\u0155\5\67\34\2\u0155")
        buf.write("\u0156\5%\23\2\u0156\u0157\5/\30\2\u0157\u0158\5!\21\2")
        buf.write("\u0158Z\3\2\2\2\u0159\u015a\5;\36\2\u015a\u015b\5\67\34")
        buf.write("\2\u015b\u015c\5=\37\2\u015c\u015d\5\35\17\2\u015d\\\3")
        buf.write("\2\2\2\u015e\u015f\5\37\20\2\u015f\u0160\5\25\13\2\u0160")
        buf.write("\u0161\5+\26\2\u0161\u0162\59\35\2\u0162\u0163\5\35\17")
        buf.write("\2\u0163^\3\2\2\2\u0164\u0165\5%\23\2\u0165\u0166\5\37")
        buf.write("\20\2\u0166`\3\2\2\2\u0167\u0168\5;\36\2\u0168\u0169\5")
        buf.write("#\22\2\u0169\u016a\5\35\17\2\u016a\u016b\5/\30\2\u016b")
        buf.write("b\3\2\2\2\u016c\u016d\5\35\17\2\u016d\u016e\5+\26\2\u016e")
        buf.write("\u016f\59\35\2\u016f\u0170\5\35\17\2\u0170d\3\2\2\2\u0171")
        buf.write("\u0172\5A!\2\u0172\u0173\5#\22\2\u0173\u0174\5%\23\2\u0174")
        buf.write("\u0175\5+\26\2\u0175\u0176\5\35\17\2\u0176f\3\2\2\2\u0177")
        buf.write("\u0178\5\33\16\2\u0178\u0179\5\61\31\2\u0179h\3\2\2\2")
        buf.write("\u017a\u017b\5\37\20\2\u017b\u017c\5\61\31\2\u017c\u017d")
        buf.write("\5\67\34\2\u017dj\3\2\2\2\u017e\u017f\5;\36\2\u017f\u0180")
        buf.write("\5\61\31\2\u0180l\3\2\2\2\u0181\u0182\5\33\16\2\u0182")
        buf.write("\u0183\5\61\31\2\u0183\u0184\5A!\2\u0184\u0185\5/\30\2")
        buf.write("\u0185\u0186\5;\36\2\u0186\u0187\5\61\31\2\u0187n\3\2")
        buf.write("\2\2\u0188\u0189\5\27\f\2\u0189\u018a\5\67\34\2\u018a")
        buf.write("\u018b\5\35\17\2\u018b\u018c\5\25\13\2\u018c\u018d\5)")
        buf.write("\25\2\u018dp\3\2\2\2\u018e\u018f\5\31\r\2\u018f\u0190")
        buf.write("\5\61\31\2\u0190\u0191\5/\30\2\u0191\u0192\5;\36\2\u0192")
        buf.write("\u0193\5%\23\2\u0193\u0194\5/\30\2\u0194\u0195\5=\37\2")
        buf.write("\u0195\u0196\5\35\17\2\u0196r\3\2\2\2\u0197\u0198\5\67")
        buf.write("\34\2\u0198\u0199\5\35\17\2\u0199\u019a\5;\36\2\u019a")
        buf.write("\u019b\5=\37\2\u019b\u019c\5\67\34\2\u019c\u019d\5/\30")
        buf.write("\2\u019dt\3\2\2\2\u019e\u019f\5\27\f\2\u019f\u01a0\5\35")
        buf.write("\17\2\u01a0\u01a1\5!\21\2\u01a1\u01a2\5%\23\2\u01a2\u01a3")
        buf.write("\5/\30\2\u01a3v\3\2\2\2\u01a4\u01a5\5\35\17\2\u01a5\u01a6")
        buf.write("\5/\30\2\u01a6\u01a7\5\33\16\2\u01a7x\3\2\2\2\u01a8\u01a9")
        buf.write("\5A!\2\u01a9\u01aa\5%\23\2\u01aa\u01ab\5;\36\2\u01ab\u01ac")
        buf.write("\5#\22\2\u01acz\3\2\2\2\u01ad\u01ae\5\33\16\2\u01ae\u01af")
        buf.write("\5%\23\2\u01af\u01b0\5? \2\u01b0|\3\2\2\2\u01b1\u01b2")
        buf.write("\5\61\31\2\u01b2\u01b3\5\67\34\2\u01b3~\3\2\2\2\u01b4")
        buf.write("\u01b5\5\25\13\2\u01b5\u01b6\5/\30\2\u01b6\u01b7\5\33")
        buf.write("\16\2\u01b7\u0080\3\2\2\2\u01b8\u01b9\5/\30\2\u01b9\u01ba")
        buf.write("\5\61\31\2\u01ba\u01bb\5;\36\2\u01bb\u0082\3\2\2\2\u01bc")
        buf.write("\u01bd\5-\27\2\u01bd\u01be\5\61\31\2\u01be\u01bf\5\33")
        buf.write("\16\2\u01bf\u0084\3\2\2\2\u01c0\u01c1\7-\2\2\u01c1\u0086")
        buf.write("\3\2\2\2\u01c2\u01c3\7/\2\2\u01c3\u0088\3\2\2\2\u01c4")
        buf.write("\u01c5\7,\2\2\u01c5\u008a\3\2\2\2\u01c6\u01c7\7\61\2\2")
        buf.write("\u01c7\u008c\3\2\2\2\u01c8\u01c9\7?\2\2\u01c9\u008e\3")
        buf.write("\2\2\2\u01ca\u01cb\7*\2\2\u01cb\u0090\3\2\2\2\u01cc\u01cd")
        buf.write("\7+\2\2\u01cd\u0092\3\2\2\2\u01ce\u01cf\7=\2\2\u01cf\u0094")
        buf.write("\3\2\2\2\u01d0\u01d1\7<\2\2\u01d1\u0096\3\2\2\2\u01d2")
        buf.write("\u01d3\7]\2\2\u01d3\u0098\3\2\2\2\u01d4\u01d5\7_\2\2\u01d5")
        buf.write("\u009a\3\2\2\2\u01d6\u01d7\7.\2\2\u01d7\u009c\3\2\2\2")
        buf.write("\u01d8\u01d9\7\60\2\2\u01d9\u01da\7\60\2\2\u01da\u009e")
        buf.write("\3\2\2\2\u01db\u01dd\t\35\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e3\3\2\2\2\u01e0\u01e2\t\36\2\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u00a0\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e6\u01e7\7v\2\2\u01e7\u01e8\7t\2\2\u01e8\u01e9\7w")
        buf.write("\2\2\u01e9\u01f0\7g\2\2\u01ea\u01eb\7h\2\2\u01eb\u01ec")
        buf.write("\7c\2\2\u01ec\u01ed\7n\2\2\u01ed\u01ee\7u\2\2\u01ee\u01f0")
        buf.write("\7g\2\2\u01ef\u01e6\3\2\2\2\u01ef\u01ea\3\2\2\2\u01f0")
        buf.write("\u00a2\3\2\2\2\u01f1\u01f3\t\37\2\2\u01f2\u01f1\3\2\2")
        buf.write("\2\u01f3\u01f4\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u00a4\3\2\2\2\u01f6\u01f7\5\u00a3R\2\u01f7")
        buf.write("\u01fb\7\60\2\2\u01f8\u01fa\t\37\2\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u0200\5\u00a9U\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2")
        buf.write("\2\2\u0200\u020a\3\2\2\2\u0201\u0202\7\60\2\2\u0202\u0204")
        buf.write("\5\u00a3R\2\u0203\u0205\5\u00a9U\2\u0204\u0203\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u020a\3\2\2\2\u0206\u0207\5")
        buf.write("\u00a3R\2\u0207\u0208\5\u00a9U\2\u0208\u020a\3\2\2\2\u0209")
        buf.write("\u01f6\3\2\2\2\u0209\u0201\3\2\2\2\u0209\u0206\3\2\2\2")
        buf.write("\u020a\u00a6\3\2\2\2\u020b\u0210\7$\2\2\u020c\u020f\5")
        buf.write("\u00adW\2\u020d\u020f\n \2\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020d\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0210\u0211\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u0210\3")
        buf.write("\2\2\2\u0213\u0214\7$\2\2\u0214\u0215\bT\3\2\u0215\u00a8")
        buf.write("\3\2\2\2\u0216\u0218\t\7\2\2\u0217\u0219\7/\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3\2\2\2")
        buf.write("\u021a\u021c\t\37\2\2\u021b\u021a\3\2\2\2\u021c\u021d")
        buf.write("\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write("\u00aa\3\2\2\2\u021f\u0221\t!\2\2\u0220\u021f\3\2\2\2")
        buf.write("\u0221\u0222\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3")
        buf.write("\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\bV\2\2\u0225\u00ac")
        buf.write("\3\2\2\2\u0226\u0227\7^\2\2\u0227\u0228\t\"\2\2\u0228")
        buf.write("\u00ae\3\2\2\2\u0229\u022a\13\2\2\2\u022a\u022b\bX\4\2")
        buf.write("\u022b\u00b0\3\2\2\2\u022c\u0231\7$\2\2\u022d\u0230\5")
        buf.write("\u00adW\2\u022e\u0230\n#\2\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0231\u022f\3\2\2\2\u0232\u0234\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0234\u0235\t$\2\2\u0235\u0236\n\"\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\bY\5\2\u0238\u00b2\3\2\2\2\u0239")
        buf.write("\u0241\7$\2\2\u023a\u0240\5\u00adW\2\u023b\u0240\n%\2")
        buf.write("\2\u023c\u023d\n$\2\2\u023d\u023e\7^\2\2\u023e\u0240\7")
        buf.write("$\2\2\u023f\u023a\3\2\2\2\u023f\u023b\3\2\2\2\u023f\u023c")
        buf.write("\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241")
        buf.write("\u0242\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0244\u0246\t&\2\2\u0245\u0244\3\2\2\2\u0246\u0247\3")
        buf.write("\2\2\2\u0247\u0248\bZ\6\2\u0248\u00b4\3\2\2\2\30\2\u00cb")
        buf.write("\u00d7\u00e4\u01de\u01e3\u01ef\u01f4\u01fb\u01ff\u0204")
        buf.write("\u0209\u020e\u0210\u0218\u021d\u0222\u022f\u0231\u023f")
        buf.write("\u0241\u0245\7\b\2\2\3T\2\3X\3\3Y\4\3Z\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    BLOCK_COMMENT = 7
    NEW_BLOCK_COMMENT = 8
    LINE_COMMENT = 9
    VAR = 10
    FUNCTION = 11
    PROCEDURE = 12
    ARRAY = 13
    OF = 14
    INTEGER = 15
    BOOLEAN = 16
    REAL = 17
    STRING = 18
    TRUE = 19
    FALSE = 20
    IF = 21
    THEN = 22
    ELSE = 23
    WHILE = 24
    DO = 25
    FOR = 26
    TO = 27
    DOWNTO = 28
    BREAK = 29
    CONTINUE = 30
    RETURN = 31
    BEGIN = 32
    END = 33
    WITH = 34
    DIV = 35
    OR = 36
    AND = 37
    NOT = 38
    MOD = 39
    PLUS = 40
    MINUS = 41
    MULT = 42
    DIVI = 43
    EQUALS = 44
    LB = 45
    RB = 46
    SEMI = 47
    COLON = 48
    LSB = 49
    RSB = 50
    COMMA = 51
    DOUBLEDOT = 52
    ID = 53
    BOOLLIT = 54
    INTLIT = 55
    FLOATLIT = 56
    STRINGLIT = 57
    WS = 58
    ERROR_CHAR = 59
    ILLEGAL_ESCAPE = 60
    UNCLOSE_STRING = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'<>'", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", 
            "'*'", "'/'", "'='", "'('", "')'", "';'", "':'", "'['", "']'", 
            "','", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "NEW_BLOCK_COMMENT", "LINE_COMMENT", "VAR", 
            "FUNCTION", "PROCEDURE", "ARRAY", "OF", "INTEGER", "BOOLEAN", 
            "REAL", "STRING", "TRUE", "FALSE", "IF", "THEN", "ELSE", "WHILE", 
            "DO", "FOR", "TO", "DOWNTO", "BREAK", "CONTINUE", "RETURN", 
            "BEGIN", "END", "WITH", "DIV", "OR", "AND", "NOT", "MOD", "PLUS", 
            "MINUS", "MULT", "DIVI", "EQUALS", "LB", "RB", "SEMI", "COLON", 
            "LSB", "RSB", "COMMA", "DOUBLEDOT", "ID", "BOOLLIT", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "BLOCK_COMMENT", 
                  "NEW_BLOCK_COMMENT", "LINE_COMMENT", "A", "B", "C", "D", 
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                  "VAR", "FUNCTION", "PROCEDURE", "ARRAY", "OF", "INTEGER", 
                  "BOOLEAN", "REAL", "STRING", "TRUE", "FALSE", "IF", "THEN", 
                  "ELSE", "WHILE", "DO", "FOR", "TO", "DOWNTO", "BREAK", 
                  "CONTINUE", "RETURN", "BEGIN", "END", "WITH", "DIV", "OR", 
                  "AND", "NOT", "MOD", "PLUS", "MINUS", "MULT", "DIVI", 
                  "EQUALS", "LB", "RB", "SEMI", "COLON", "LSB", "RSB", "COMMA", 
                  "DOUBLEDOT", "ID", "BOOLLIT", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "EXPONENT", "WS", "ESC", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[82] = self.STRINGLIT_action 
            actions[86] = self.ERROR_CHAR_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            actions[88] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        s=self.text[1:-1]
                        self.text=s
                    
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
            				raise ErrorToken(self.text) 
            			
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            			raise IllegalEscape(self.text[1:])
            			
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            				if self.text[-1]=='\n':
            					raise UncloseString(self.text[1:-1])
            				else:
            					raise UncloseString(self.text[1:])
            			
     



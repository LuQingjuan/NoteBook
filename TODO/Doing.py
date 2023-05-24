import re

class Stack():
    def __init__(self):
        self.data = []
        self.len = 0
    def pop(self):
        if self.len>0:
            self.len-=1
            return self.data.pop()
        else:
            return None
    def push(self, value):
        self.data.append(value)
        self.len+=1

class Source():
    def __init__(self, infile):
        self.key_dict = {# KEYWORD
                            "far": 257,
                            "near": 258,
                            "pascal": 259,
                            "register": 260,
                            "asm": 261,
                            "cdecl": 262,
                            "huge": 263,
                            "auto": 264,
                            "double": 265,
                            "int": 266,
                            "struct": 267,
                            "break": 268,
                            "else": 269,
                            "long": 270,
                            "switch": 271,
                            "case": 272,
                            "enum": 273,
                            "register": 274,
                            "typedef": 275,
                            "char": 276,
                            "extern": 277,
                            "return": 278,
                            "union": 279,
                            "const": 280,
                            "float": 281,
                            "short": 282,
                            "unsigned": 283,
                            "continue": 284,
                            "for": 285,
                            "signed": 286,
                            "void": 287,
                            "default": 288,
                            "goto": 289,
                            "sizeof": 290,
                            "volatile": 291,
                            "do": 292,
                            "if": 293,
                            "while": 294,
                            "static": 295,
                            "interrupt": 296,
                            "sizeof": 297,
                            "NULL": 298,
                            # SEPARATOR
                            "{": 299,
                            "}": 300,
                            "[": 301,
                            "]": 302,
                            "(": 303,
                            ")": 304,
                            "~": 305,
                            ",": 306,
                            ";": 307,
                            ".": 308,
                            "#": 309,
                            "?": 310,
                            ":": 311,
                            # OPERATOR
                            "<<": 312,
                            ">>": 313,
                            "<": 314,
                            "<=": 315,
                            ">": 316,
                            ">=": 317,
                            "=": 318,
                            "==": 319,
                            "|": 320,
                            "||": 321,
                            "|=": 322,
                            "^": 323,
                            "^=": 324,
                            "&": 325,
                            "&&": 326,
                            "&=": 327,
                            "%": 328,
                            "%=": 329,
                            "+": 330,
                            "++": 331,
                            "+=": 332,
                            "-": 333,
                            "--": 334,
                            "-=": 335,
                            "->": 336,
                            "/": 337,
                            "/=": 338,
                            "*": 339,
                            "*=": 340,
                            "!": 341,
                            "!=": 342,
                            "sizeof": 343,
                            "<<=": 344,
                            ">>=": 345,
                            "inum": 346,
                            "int16": 347,
                            "int8": 348,
                            "char": 350,
                            "string": 351,
                            "bool": 352,
                            "fnum": 353,
                            "IDN": 354
                        }

        with open(infile, 'r', encoding='utf-8') as file:
            self.code = file.read()
        self.str = Stack()

    # ***************对关键字进行搜索**************
    def is_keyword(self, is_res):
        return self.key_dict.get(is_res,0)

        for i in range(MAX):
            if symtable[i].lexptr == is_res:
                return symtable[i].token
        return 0

    # *****************判断是否为自定义函数*****************
    def is_deFunc(self, word):
        # 定义正则表达式
        pattern = r'\b[a-zA-Z_]\w*\s*\(' #任意字母下划线加(0-无穷)个字母下划线加无空格
        matches = re.findall(pattern, self.code)
        deFunc = [match[:-1].rstrip().lower() for match in matches if match[:-1] not in str]

        for s in deFunc:
            if s == word:
                return s
        return 0

    # *****************判断是否为字母*****************
    def is_letter(self, c):
        if c.isalpha():
            return True
        else:
            return False

    # *************判断是否为数字**************
    def is_digit(self, c):
        if c.isdigit():
            return True
        else:
            return False

    def analyse(self):
        code_len = len(self.code)
        i = 0
        while(i<code_len):
            print(self.code[i])
            i+=1






fpin = r"hello.c"
fpout = r"data1.txt"
code = Source(fpin)
code.analyse()


s=Stack()
s.push({"AAA",1})
print(s.pop())
s.push({"BBB",2})
s.push("CCC")
print(s.pop())
s.push("DDDD")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
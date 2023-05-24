import re
 
MAX = 22  # 分析符号表的最大容量
RES_MAX = 10  # 关键字的最大长度
MAXBUF = 255  # 缓冲区的大小
 
ch = ' '  # 存放读入当前的输入字符
Line_NO = 1  # 记录行号
 
# 关键字
class keywords:
    def __init__(self, lexptr, token):
        self.lexptr = lexptr
        self.token = token
 
symtable = [keywords("", 0) for _ in range(MAX)]#初始化symtable
 
str = ["int","char","float","main","double","case", "for","if","auto","else","do",
       "while","void","static", "return","break","struct","const","union","switch","typedef","enum"]
CATEGORY_DICT = {
    # KEYWORD
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

# 最小的token是program：3，最大的token是or：24
 
def init():#将对应的单词填进结构体lexptr中
    for j in range(MAX):
        symtable[j].lexptr = str[j]
        symtable[j].token = j + 3   #int的种类编码为3，所以从3开始
 
# ***************对关键字进行搜索**************
def is_keyword(is_res):
    for i in range(MAX):
        if symtable[i].lexptr == is_res:
            return symtable[i].token
    return 0
 
# *****************判断是否为自定义函数*****************
def is_deFunc(word, deFunc):
    for s in deFunc:
        if s == word:
            return s
    return 0
 
# *****************判断是否为字母*****************
def is_letter(c):
    if c.isalpha():
        return True
    else:
        return False
 
# *************判断是否为数字**************
def is_digit(c):
    if c.isdigit():
        return True
    else:
        return False
 
fpin = r"hello.c"
fpout = r"data1.txt"
# ***************分析程序**************
def analyse(fpin, fpout):
    global ch, Line_NO
    j = 0
    arr = [""] * MAXBUF  # 输入缓冲区，存放一个单词符号
 
    with open(fpin, 'r', encoding='utf-8') as file:
        c_code = file.read()
        # 定义正则表达式
        pattern = r'\b[a-zA-Z_]\w*\s*\(' #任意字母下划线加(0-无穷)个字母下划线加无空格
        matches = re.findall(pattern, c_code)
        deFunc = [match[:-1].rstrip().lower() for match in matches if match[:-1] not in str]
 
    with open(fpin, 'rb') as file, open(fpout, 'w') as outfile:
        while True:
            arr = [""] * MAXBUF
            bch = file.read(1)
            ch = bch.decode('utf-8', errors='ignore')
            if not bch:
                # 如果读取到文件末尾，退出循环
                break
            # 碰到空格、tab则跳过
            if ch == ' ' or ch == '\t':
                pass
            elif ch == '\r':
                bch = file.read(1)
                ch = bch.decode('utf-8', errors='ignore')
                if ch == '\n':
                    Line_NO += 1
#*********************字符串的处理*************************
            elif is_letter(ch):
                while is_letter(ch) or is_digit(ch) or ch == '_':
                    if ch.isupper():
                        ch = ch.lower()  # 忽略大小写,如果是大写则转换为小写
                    arr[j] = ch
                    j += 1
                    bch = file.read(1)
                    ch = bch.decode('utf-8', errors='ignore')
                #输入指针回退一个字符,参数 -1 表示向前移动一个字节，参数 1 表示相对于当前位置进行移动
                file.seek(-1, 1)
                y = ''.join(arr)
                # 直到读取到的不是字母，数字或者_执行
                j = 0
                if is_keyword(y):
                    outfile.write("{}\t\t{}\t\t关键字\t\t{}\n".format(y, is_keyword(y), Line_NO))
                elif is_deFunc(y, deFunc):
                    outfile.write("{}\t\t\t\t自定义函数\t\t{}\n".format(y , Line_NO))
                else:
                    outfile.write("{}\t\t{}\t\t标识符\t\t{}\n".format(y, 1, Line_NO))
            # ** ** ** ** ** ** ** ** ** ** ** ** *数字的处理 ** ** ** ** ** ** ** ** ** ** ** ** ** **
            elif is_digit(ch):
                arr = [""] * MAXBUF
                s = 0
                while(is_digit(ch) or is_letter(ch)):
                    if is_letter(ch):
                        arr[j] = ch
                        j += 1
                        bch = file.read(1)
                        ch = bch.decode('utf-8', errors='ignore')
                        s = 1
                    elif is_digit(ch):
                        arr[j] = ch
                        j += 1
                        bch = file.read(1)
                        ch = bch.decode('utf-8', errors='ignore')
                if is_letter(ch) or is_digit(ch) or ch == '_':
                    file.seek(-1, 1)
                j = 0
                file.seek(-1, 1)
                if s == 0:
                    outfile.write("{}\t\t{}\t\t无符号整数\t\t{}\n".format(''.join(arr), 2, Line_NO))
                elif s == 1:
                    outfile.write("{}\t\t{}\t\t错误\t\t{}\n".format(''.join(arr), 3, Line_NO))
 
            elif ch == '+':
                bch = file.read(1)
                ch = bch.decode('utf-8', errors='ignore')
                if ch == '+':
                    outfile.write("{}\t\t{}\t\t自加运算符\t\t{}\n".format("++", 41, Line_NO))
                    continue
                elif ch == '=':
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("+=", 42, Line_NO))
                    continue
                else:
                    file.seek(-1, 1)
                outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("+", 43, Line_NO))
 
            elif ch == '-':
                ch = file.read(1)
                if ch == '-':
                    outfile.write("{}\t\t{}\t\t自减运算符\t\t{}\n".format("--", 44, Line_NO))
                    continue
 
                elif ch == '=':
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("-=", 45,Line_NO))
                else:
                    file.seek(-1, 1)
                outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("-", 46, Line_NO))
 
            elif ch == '*':
                outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("*", 47, Line_NO))
                continue
 
            elif ch == '(':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("(", 25, Line_NO))
                continue
 
            elif ch == ')':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format(")", 26, Line_NO))
                continue
 
            elif ch == '[':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("[", 27, Line_NO))
                continue
 
            elif ch == ']':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("]", 28, Line_NO))
                continue
 
            elif ch == ';':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format(";", 29, Line_NO))
                continue
 
            elif ch == '=':
                outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("=", 48, Line_NO))
                continue
 
            elif ch == '.':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format(".", 30, Line_NO))
                continue
 
            elif ch == ',':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format(",", 31, Line_NO))
                continue
 
            elif ch == ':':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format(":", 32, Line_NO))
                continue
 
            elif ch == '{':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("{", 33, Line_NO))
                continue
 
            elif ch == '}':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("}", 34, Line_NO))
                continue
 
            elif ch == '%':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("%", 35, Line_NO))
                continue
 
            elif ch == '\"':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("\"", 36, Line_NO))
                continue
 
            elif ch == '\\':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("\\", 37, Line_NO))
                continue
 
            elif ch == '#':
                outfile.write("{}\t\t{}\t\t分界符\t\t{}\n".format("#", 38, Line_NO))
                continue
 
            elif ch == '>':
                bch = file.read(1)
                ch = bch.decode('utf-8', errors='ignore')
                if ch == '=':
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format(">=", 49, Line_NO))
                    continue
                else:
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format(">", 50, Line_NO))
                    file.seek(-1, 1)
                    continue
 
            elif ch == '<':
                bch = file.read(1)
                ch = bch.decode('utf-8', errors='ignore')
                if ch == '=':
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("<=", 51, Line_NO))
                    continue
                elif ch == ">":
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("<>", 52, Line_NO))
                    continue
                else:
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("<", 53, Line_NO))
                    file.seek(-1, 1)
                    continue
 
            # ** ** ** ** ** ** ** *出现在 / / 之间的全部作为注释部分处理 ** ** ** ** ** ** ** ** ** *
            elif ch == '/':
                bch = file.read(1)
                ch = bch.decode('utf-8', errors='ignore')
                if ch == '/':
                    while ch != '\n':
                        bch = file.read(1)
                        ch = bch.decode('utf-8', errors='ignore')
                        if not bch:
                            # 如果读取到文件末尾，退出循环
                            break
                    Line_NO += 1
                elif ch == '*':
                    while ch != '/':
                        bch = file.read(1)
                        ch = bch.decode('utf-8', errors='ignore')
                        if not bch:
                            # 如果读取到文件末尾，退出循环
                            break
                    if ch == ' ':
                        outfile.write("缺少一个'/'\n")
                else:
                    outfile.write("{}\t\t{}\t\t运算符\t\t{}\n".format("/", 39, Line_NO))
                    file.seek(-1, 1)
 
            else:
                outfile.write("在第{}行无法识别的字符\t{}\n".format(Line_NO, ch))
 
init()
analyse(fpin, fpout)
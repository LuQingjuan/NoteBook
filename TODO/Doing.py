import re
'''
1、数据类型关键字（12个）
char
double
enum
float
int
long
short
signed
struct
union
unsigned
void
2、控制语句关键字（12个）：
A循环语句
for
do
while
break
continue
B条件语句
if
else
goto
C开关语句
switch
case
default
D返回语句
return
3、存储类型关键字（4个）：
auto
extern
register
static
4、其它关键字（4个）：
const
sizeof
typedef
volatile
'''

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

# for i,file in enumerate(os.listdir(path))

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

# ***************分析程序**************
def analyse(fpin, fpout):
    global ch, Line_NO
    j = 0
    arr = [""] * MAXBUF  # 输入缓冲区，存放一个单词符号
 
    with open(fpin, 'r', encoding='utf-8') as file:
        c_code = file.read()
        #print(c_code)
        # 定义正则表达式
        pattern = r'\b[a-zA-Z_]\w*\s*\(' #任意字母下划线加(0-无穷)个字母下划线加无空格
        matches = re.findall(pattern, c_code)
        deFunc = [match[:-1].rstrip().lower() for match in matches if match[:-1] not in str]
 
    with open(fpin, 'rb') as file, open(fpout, 'w') as outfile:
        while True:
            arr = [""] * MAXBUF
            bch = file.read(1)
            ch = bch.decode('utf-8', errors='ignore')
            #print("bcn: ",bch," ch: ",ch)
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
            # ** ** ** ** ** ** ** ** ** ** *字符串的处理 ** ** ** ** ** ** ** ** ** ** ** ** *
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


class Stack():
    def __init__(self):
        self.data = []
        self.len = 0

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.data.pop()
        else:
            return None

    def push(self, value):
        self.data.append(value)
        self.len += 1

def analyse_group(key_list):
    sentences = []
    #sentences.insert(0,data)
    group = Stack()
    for data in key_list:
        if data in ['}',')',']',';']:
            tmp_data = group.pop()
            while None != tmp_data:
                pass
        if ';' == data:
            tmp_group = Stack()
            while None != tmp_data and ';' != tmp_data:
                tmp_data = group.pop()

        elif data in ['{','(','[']:
            pass
        else:
            group.push(data)

def analyse_new(fpin):
    with open(fpin, 'r', encoding='utf-8') as file:
        sentences = re.split(r"([^a-zA-Z0-9_])", file.read())
        for item in sentences[:]:
            if '' == item:
                sentences.remove(item)
    #print(sentences)

    sub = Stack()
    id = 0
    flag = ''
    start_id = -1
    end_id = -1
    new_sentences = []
    group = Stack()
    while id < len(sentences):
        if '/*' == flag:
            # /*    */
            if '\\' != sentences[id-2] and '*' == sentences[id-1] and '/' == sentences[id]:
                end_id = id
        elif '//' == flag:
            # //    \n
            if '\\' != sentences[id-1] and '\n' == sentences[id]:
                end_id = id
        elif '"' == flag:
            # "    "
            if '\\' != sentences[id-1] and '"' == sentences[id]:
                end_id = id
        elif '\'' == flag:
            # '    '
            if '\\' != sentences[id-1] and '\'' == sentences[id]:
                end_id = id
        else:
            # 查找特殊字符
            if '*' == sentences[id]:
                # /*
                if (1 == id and '/' == sentences[id-1]) or (id > 1 and '\\' != sentences[id-2] and '/' == sentences[id-1]):
                    start_id = id-1
                    flag = ''.join(sentences[start_id:start_id+2])
            elif '/' == sentences[id]:
                # //
                if (1 == id and '/' == sentences[id-1]) or (id > 1 and '\\' != sentences[id-2] and '/' == sentences[id-1]):
                    start_id = id-1
                    flag = ''.join(sentences[start_id:start_id+2])
            elif '"' == sentences[id]:
                # "
                if (0 == id) or (id > 0 and '\\' != sentences[id-1]):
                    start_id = id
                    flag = '"'
            elif '\'' == sentences[id]:
                # '
                if (0 == id) or (id > 0 and '\\' != sentences[id-1]):
                    start_id = id
                    flag = '\''
                    
            else:
                if sentences[id] not in [' ','\t','\r','\n']:
                    new_sentences.append(sentences[id])

        if end_id > 0:
            # 特殊字符结束
            new_sentences.append(''.join(sentences[start_id:end_id+1]))
            print(''.join(sentences[start_id:end_id+1]))
            flag = ''
            start_id = -1
            end_id = -1

        id += 1
    print(new_sentences)
    analyse_group(new_sentences)
'''        elif '\'' == sentences[id]:
            id += 1
            while id < len(sentences) and '\\' != sentences[id-1] '\'' != sentences[id]:
                id += 1
            id += 1
        elif '' == sentences[id]:
        elif '' == sentences[id]:
        elif '' == sentences[id]:
        elif '' == sentences[id]:
        elif '' == sentences[id]:
        elif '' == sentences[id]:
        id += 1
    #with open(fpin, 'rb') as file, open(fpout, 'w') as outfile:
'''
init()
fpin = r"hello.c"
fpout = r"data1.txt"
analyse_new(fpin)
arr = ['a','b','c','d']
str1 = ''.join(arr[2:3])
print(str1)

'''
import os
from datetime import datetime

code = Source(fpin)
code.analyse()

ctime = os.path.getctime(fpin) #创建时间
ctime_string = datetime.fromtimestamp(int(ctime))
 
mtime = os.path.getmtime(fpin) #修改时间
mtime_string = datetime.fromtimestamp(int(ctime))
 
atime = os.path.getatime(fpin) #访问时间
atime_string = datetime.fromtimestamp(int(ctime))
 
print(
    f"创建时间：{ctime_string}", 
    f"修改时间：{mtime_string}", 
    f"访问时间：{atime_string}", 
    sep="\n"
)
 
 

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
'''
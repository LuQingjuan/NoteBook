from bs4 import BeautifulSoup
#参考资料：https://cuiqingcai.com/1319.html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


#soup = BeautifulSoup(html)
soup = BeautifulSoup(open('test.html'))
#格式化
print(soup.prettify())

print("----------------------------------------------------")
#查找的是在所有内容中的第一个符合要求的标签
print(soup.title)
print(soup.head)

# Tag两个重要的属性，是 name 和 attrs
print(soup.head.name)
print(soup.p.attrs)

#获取某个属性
#print(soup.p.attrs['class'])
print(soup.p['class'])
print(soup.p.get('class'))


#获取标签内部的文字
print(soup.p.string)
#判断了它的类型，是否为 Comment 类型，然后再进行其他操作，如打印输出。
#if type(soup.a.string)==bs4.element.Comment:
#    print(soup.a.string)

#可以将 tag 的子节点以列表的方式输出
print(soup.body.contents)
print("-------------------------------------------------------------------")
#遍历子孙节点
for child in  soup.body.children:
    print(child)
print("-------------------------------------------------------------------")
#遍历所有子孙节点
for child in soup.descendants:
    print(child)
print("-------------------------------------------------------------------")

#最里面的内容 唯一子节点
print(soup.head.string)
print(soup.title.string)

#获取多个内容，不过需要遍历获取
for string in soup.strings:
    print(repr(string))
print("-------------------------------------------------------------------")
#去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))
print("-------------------------------------------------------------------")

#父节点
content = soup.head.title.string
print(content.parent.name)
#所有父辈节点
content = soup.head.title.string
for parent in  content.parents:
    print(parent.name)

#兄弟节点
#.next_sibling 
#.previous_sibling
print(soup.p.next_sibling.next_sibling)

#兄弟节点
#.next_siblings 
#.previous_siblings
for sibling in soup.a.next_siblings:
    print(repr(sibling))

#    find( name , attrs , recursive , text , **kwargs )【根据参数来找出对应的标签,但只返回第一个符合条件的结果】
#    find_all( name , attrs , recursive , text , **kwargs ):【根据参数来找出对应的标签,但只返回所有符合条件的结果】
#    筛选条件参数介绍：
#        name：为标签名,根据标签名来筛选标签
#        attrs:为属性,，根据属性键值对来筛选标签，赋值方式可以为:属性名=值,attrs={属性名:值}【但由于class是python关键字，需要使用class_】
#        text：为文本内容，根据指定文本内容来筛选出标签，【单独使用text作为筛选条件，只会返回text，所以一般与其他条件配合使用】
#        recursive：指定筛选是否递归，当为False时，不会在子结点的后代结点中查找，只会查找子结点
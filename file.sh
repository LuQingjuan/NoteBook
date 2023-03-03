#!/bin/bash
#folder="./test"

function readfile ()
{
    if [[ $(ls $1 | grep "Catalog.md") != "" ]]
    then
        echo $3" "`basename $1` >> Catalog.md
        #echo "包含"
        #echo "@import \"$1/Catalog.md\"" >> Catalog.md
        echo "* **[[ $1/Catalog.md | `basename $1`_Catalog ]]**" >> Catalog.md
    else
        #echo "不包含"
        echo $3" "`basename $1` >> Catalog.md
        #这里`为esc下面的按键符号
        for file in `ls $1`
        do
            #这里的-d表示是一个directory，即目录/子文件夹
            if [ -d $1"/"$file ]
            then
                #如果子文件夹则递归
                if [ $(($2-1)) -gt 0 ]
                then
                    readfile $1"/"$file $(($2-1)) "${3}#"
                else
                    echo "* **"$file"**" >> Catalog.md
                fi
            else
                if [[ "Catalog.md" != $file ]]
                then
                    #否则就能够读取该文件的地址
                    echo "* [[ "$1"/"$file" | "$file" ]]" >> Catalog.md
                fi
            #读取该文件的文件名，basename是提取文件名的关键字
            #echo `basename $file`
        fi
        done
    fi
    echo "" >> Catalog.md
}

#echo $*
#echo $1
#echo $2
#echo $(($2-1))

if [ 2 -ne $# ]
then
    echo "./file.sh folder deep"
else
    rm Catalog.md
    readfile $1 $2 "#"
fi
#函数定义结束，这里用来运行函数
#folder="./Note"
#readfile $folder "#"
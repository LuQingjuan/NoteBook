#!/bin/bash

function Init_Daily_Folder(){
    path=$1
    if [ ! -d "$path" ]; then
        mkdir -p "${path}"
    fi
}

function Create_Note() {
    file_name=$1
    topic=$2
    date_time=$3

    echo "* Type:"                  >> $file_name
    echo "* Tags:"                  >> $file_name
    echo "* Date: $date_time"       >> $file_name
    echo "* Related:"               >> $file_name
    echo "* Reference:[]()"         >> $file_name
    echo ""                         >> $file_name
    echo "## $topic"                >> $file_name
}

function Create_Day() {
    file_name=$1
    date=$2
    echo "## Detail"                >> $file_name
    echo "![[TodoList#$2|$2]]"      >> $file_name
    echo ""                         >> $file_name
    echo "## 日复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "### 活动执行过程"          >> $file_name
    echo "* 这样很好"                >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
    echo "* 可以提升"                >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
    echo "### 其他人处理方式"        >> $file_name
    echo "* 值得学习"                >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
    echo "* 自己避免"                >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
    echo "### 自我评价"              >> $file_name
    echo "* 棒棒的"                  >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
    echo "* 调整下"                 >> $file_name
    echo "    1. "                  >> $file_name
    echo ""                         >> $file_name
}

function Create_Week() {
    file_name=$1
    echo "## 周复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Month() {
    file_name=$1
    echo "## 月度复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Quarter() {
    file_name=$1
    echo "## 季度复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Year() {
    file_name=$1
    echo "## 年度复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Usage() {
    echo "---------------------------------------------------"
    echo "                       Usage                       "
    echo "./template.sh Note [Topic]"
    echo "./template.sh Day"
    echo "---------------------------------------------------"
}


current=$(date +"%Y%m%d %H:%M:%S %w")
tmp_year=${current:0:4}
tmp_month=${current:4:2}
tmp_day=${current:6:2}
tmp_time=${current:8:9}
tmp_week=${current:18:1}

# echo $tmp_year
# echo $tmp_month
# echo $tmp_day
# echo $tmp_time
# echo $tmp_week


# $ date -d 20230308 +"%w"
# 3
# $ date -d 20230308 +"%V"
# 10

case $1 in
    "Note")
        path=${current:0:8}
        Init_Daily_Folder ${path}
        cd ${path}
        if [ ! -f "$2.md" ]; then
            Create_Note "$2.md" $2 "$current"
        fi
        #cd NoteBook/01\ Note/
        #path=${tmp_year}_${tmp_month}_${tmp_day}
        #cd ${path}
        #cd -
        ;;
    "Day")
        if [ ! -f "${current:0:8}.md" ]; then
            Create_Day "${current:0:8}.md" ${tmp_year}${tmp_month}${tmp_day}
        fi
        ;;
    "Week")
        Create_Week
        ;;
    "Month")
        Create_Month
        ;;
    "Quarter")
        Create_Quarter
        ;;
    "Year")
        Create_Year
        ;;
    *)
        Usage
esac

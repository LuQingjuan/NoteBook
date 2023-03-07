#!/bin/bash


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
    echo "## 日复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Week() {
    file_name=$1
    echo "## 日复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Month() {
    file_name=$1
    echo "## 日复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Quarter() {
    file_name=$1
    echo "## 日复盘"                >> $file_name
    echo ""                         >> $file_name
    echo "## Detail"                >> $file_name
    echo "#### Work"                >> $file_name
    echo "* "                       >> $file_name
    echo "#### Study"               >> $file_name
    echo "* "                       >> $file_name
}

function Create_Year() {
    file_name=$1
    echo "## 日复盘"                >> $file_name
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
    echo "---------------------------------------------------"
}



today_time=$(date +"%Y/%m/%d %H:%M:%S")
echo $date_time

case $1 in
    "Note")
        cd Vault/NoteBook/01\ Note/
        #path=$(date +"%Y_%m_%d")
        #mkdir -p ${path}
        #Create_Note "${path}/$2.md" $2 "$date_time"
        Create_Note "$2.md" $2 "$date_time"
        cd -
        ;;
    "Day")
        Create_Day "${path}.md" $2 "$date_time"
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

from datetime import datetime, date, timedelta
def getDatetimeToday():
    t = date.today()  #date类型
    print(str(t))
    dt = datetime.strptime(str(t),'%Y-%m-%d %H:%M:%S') #date转str再转datetime
    return dt

def getDatetimeYesterday():
    today = getDatetimeToday() #datetime类型当前日期
    yesterday = today + timedelta(days = -1) #减去一天
    return yesterday


def get_week_of_month(year, month, day):
    """
    获取指定的某天是某个月中的第几周
    周一作为一周的开始
    """
    end = int(datetime(year, month, day).strftime("%W"))
    begin = int(datetime(year, month, 1).strftime("%W"))
    return end - begin + 1



def Insert_Data(src_lines, topic_id, topic_list, info):
    topic = topic_list[0]
    topic_flag = " ".rjust(topic_id+4, "#")
    tmp_src_lines = []

    write_flag = False
    search_flag = False
    update_info = ""
    for line in src_lines:
        if not write_flag:
            if not search_flag:
                if line == topic_flag + topic + "\n":
                    search_flag = True
            elif search_flag:
                if line[:len(topic_flag)] != topic_flag:
                    tmp_src_lines.append(line)
                if line[:len(topic_flag)] == topic_flag:
                    write_flag = True
                    if 0 == len(topic_list[1:]):
                        update_info = update_info + info + "\n"
                    else:
                        update_info = update_info + Insert_Data(tmp_src_lines, topic_id+1, topic_list[1:], info)
        update_info = update_info + line

    if write_flag == False:
        if search_flag == False:
            if 0 == len(topic_list[1:]):
                update_info = update_info + topic_flag + topic + "\n" + info + "\n"
            else:
                update_info = update_info + topic_flag + topic + "\n"
                update_info = update_info + Insert_Data(tmp_src_lines, topic_id+1, topic_list[1:], info)
        else:
            update_info = update_info + info + "\n"
    return update_info

def Insert_To_Todo_List(topic_list, info):
    update_info = ""
    search_flag = False
    write_flag = False
    r_file = open("TodoList.md", 'r')
    try:
        lines_list = r_file.readlines()
    finally:
        r_file.close()

        update_info = Insert_Data(lines_list, 0, topic_list, info)

        #print(update_info)
        w_file = open("TodoList.md", 'w')
        try:
            w_file.write(update_info)
        finally:
            w_file.close( )



print(get_week_of_month(2015, 1, 4))
print(get_week_of_month(2015, 1, 5))
print(get_week_of_month(2015, 1, 15))
print(get_week_of_month(2015, 1, 18))







if __name__ == '__main__':
    week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

    #print(getDatetimeToday())
    #print(getDatetimeYesterday())
    print(str(datetime.today()))
    print(str(datetime.today())[:10])
    print(str(datetime.today())[11:19])
    print(datetime(2023, 1, 1).strftime("%W"))
    print(week_list[datetime.today().weekday()])
    print(datetime.strptime("2023-03-08",'%Y-%m-%d') + timedelta(days = -1) )

    #Insert_To_Todo_List(["Note","项目","L5GC"],"1234")
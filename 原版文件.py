#e听说content文件解析
#By:XiaoYe_Furry
#2025/9/19
#最后一次更新:2025/9/20
result = {}
zsaw=''
while True:  # 这个是主程序循环
    content = str(input("粘贴content2:"))
    if content == "000":
        break
    a = 0
    b = 0
    flag=0
    while a < len(content):
        c1 = content[a:a+7] if a + 7 <= len(content) else ''  # 避免索引越界
        th=''
        ######选择题######
        if c1 == 'xt_nr":':
            th = content[a + 8:a + 10]  # 取出题号
            th=th.replace('.','')
            a += 10
            while a<len(content):  # 这个循环是取出答案
                c1 = str(content[a:a + 8])
                if c1 == 'answer":':
                    a += 9
                    aw = content[a:a + 1]
                    result[th] = aw
                    break
                a += 1
        ######选择题结束######

        ######其他题型######
        elif c1 == 'value":':
            a += 8
            b = 0
            aw = ''
            th=''
            # 提取答案内容（直到遇到句号或引号）
            while a+b<len(content):
                if flag==1:
                    break
                if content[a + b] != '"' and content[a + b] != '<':
                    aw+=content[a + b]
                    b+=1
                else:
                    # 找到后寻找题号
                    found_th = False
                    while a+b<len(content):
                        if str(content[a+b:a+b+5]) == 'ask":':
                            th+=str(content[a+b+6:a+b+8])
                            th=th.replace('.','')
                            found_th = True
                            break
                        elif str(content[a+b:a+b+4]) == 'th":':
                            th = str(content[a+b+5:a+b+7])
                            found_th = True
                            break
                        b += 1
                    if not found_th:
                        zsaw+=str(aw)
                        flag=1
                    if found_th:
                        result[th] = aw
                        a += b  # 移动主指针
                    break  # 无论是否找到都退出内层循环
        ######其他题型结束######
        a += 1
######输出部分######
sort_by_key = sorted(result.items(), key=lambda x: int(x[0]))
sort_result= dict(sort_by_key)
j=0
for i in sort_result.keys():
    if j%2==0:
        print(i+'.'+sort_result[i],end='  ')
    else:
        print(i+'.'+sort_result[i])
    j+=1
print()
print('听后转述:')
for n in zsaw:
    if n!='.':
        print(n,end='')
    else:
        print()

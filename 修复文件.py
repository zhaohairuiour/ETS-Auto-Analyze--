# content 文件解析（修复稳定版）
# By: XiaoYe_Furry（原版修复）
# 最后修复: 2026/9/26

import re

result = {}
zsaw = ''

while True:
    content = input("粘贴content2（输入000退出）:\n")
    if content == "000":
        break

    result.clear()
    zsaw = ''

    i = 0
    length = len(content)

    while i < length:

        # ===== 选择题 =====
        if content[i:i+8] == 'xt_nr":':
            i += 8
            # 提取题号（数字）
            th = ''
            while i < length and content[i].isdigit():
                th += content[i]
                i += 1

            # 向后找 answer
            while i < length:
                if content[i:i+8] == 'answer":':
                    i += 8
                    aw = content[i] if i < length else ''
                    result[th] = aw
                    break
                i += 1

        # ===== 其他题型 =====
        elif content[i:i+7] == 'value":':
            i += 7
            # 提取答案直到 " 或 <
            aw = ''
            while i < length and content[i] not in ('"', '<'):
                aw += content[i]
                i += 1

            # 向后找 ask 或 th
            found = False
            while i < length:
                if content[i:i+5] == 'ask":':
                    i += 5
                    th = ''
                    while i < length and content[i].isdigit():
                        th += content[i]
                        i += 1
                    result[th] = aw
                    found = True
                    break
                elif content[i:i+4] == 'th":':
                    i += 4
                    th = ''
                    while i < length and content[i].isdigit():
                        th += content[i]
                        i += 1
                    result[th] = aw
                    found = True
                    break
                i += 1

            if not found:
                zsaw += aw

        else:
            i += 1

    # ===== 输出结果 =====
    print("\n--- 解析结果 ---")
    valid_items = [(k, v) for k, v in result.items() if k.isdigit()]
    valid_items.sort(key=lambda x: int(x[0]))

    for idx, (k, v) in enumerate(valid_items):
        if idx % 2 == 0:
            print(f"{k}.{v}", end='  ')
        else:
            print(f"{k}.{v}")

    print("\n\n听后转述:")
    for ch in zsaw:
        if ch != '.':
            print(ch, end='')
        else:
            print()

#!/usr/bin/env python3
import re

with open('综合技术面试题库-2026-04-08-仅题目.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 找出所有主章节（排除目录和总结）
main_sections = []
for i, line in enumerate(lines):
    match = re.match(r'^## (\d+)\. (.+) 面试题$', line.strip())
    if match:
        main_sections.append((i, int(match.group(1)), match.group(2)))

print(f"找到 {len(main_sections)} 个章节")

# 按出现顺序重新编号
new_lines = []
current_new_num = 0

for i, line in enumerate(lines):
    stripped = line.strip()

    # 检查是否是主章节行
    match = re.match(r'^## (\d+)\. (.+) 面试题$', stripped)
    if match:
        current_new_num += 1
        name = match.group(2)
        new_line = f'## {current_new_num}. {name} 面试题'
        new_lines.append(new_line)
        print(f"  行{i}: {line} -> {new_line}")
        continue

    # 检查是否是子章节行（如 ### 6.1 或 ### 7.2）
    match = re.match(r'^### (\d+)\.(\d+)', stripped)
    if match:
        second = match.group(2)
        new_line = f'### {current_new_num}.{second}'
        new_lines.append(new_line)
        continue

    new_lines.append(line)

# 先写入临时文件验证
with open('综合技术面试题库-2026-04-08-仅题目-临时.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("\n验证新文件章节:")
with open('综合技术面试题库-2026-04-08-仅题目-临时.md', 'r') as f:
    for i, line in enumerate(f):
        if re.match(r'^## \d+\. .+ 面试题$', line.strip()):
            print(f"  {line.strip()}")

# 如果正确，替换原文件
import os
os.rename('综合技术面试题库-2026-04-08-仅题目-临时.md', '综合技术面试题库-2026-04-08-仅题目.md')
print("\n修复完成！")

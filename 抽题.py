#!/usr/bin/env python3
import random
import re

with open('综合技术面试题库-2026-04-08-仅题目.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 分割每个题目块
blocks = re.split(r'\n---\n', content)

# 提取每个题目及其章节信息
questions = []
current_section = ""
current_subsection = ""

for block in blocks:
    lines = block.strip().split('\n')
    for line in lines:
        if line.startswith('## '):
            current_section = line
        elif line.startswith('### '):
            current_subsection = line
        elif line.startswith('**题目'):
            questions.append((current_section, current_subsection, line))

# 随机选择50题
random.seed()  # 使用随机种子
selected = random.sample(questions, 50)

# 生成文件1
with open('随机面试题目-批次1.md', 'w', encoding='utf-8') as f:
    f.write('# 随机面试题目（批次1）\n\n')
    f.write('**抽题日期**: 2026-04-09\n\n')
    f.write('**题目数量**: 50\n\n')
    f.write('---\n\n')
    for i, (section, subsection, question) in enumerate(selected[:25], 1):
        f.write(f'{section}\n\n{subsection}\n\n**{i}. {question[10:]}\n\n---\n\n')

    for i, (section, subsection, question) in enumerate(selected[25:], 26):
        f.write(f'{section}\n\n{subsection}\n\n**{i}. {question[10:]}\n\n---\n\n')

# 生成文件2（使用不同的随机种子）
random.seed(42)
selected2 = random.sample(questions, 50)

with open('随机面试题目-批次2.md', 'w', encoding='utf-8') as f:
    f.write('# 随机面试题目（批次2）\n\n')
    f.write('**抽题日期**: 2026-04-09\n\n')
    f.write('**题目数量**: 50\n\n')
    f.write('---\n\n')
    for i, (section, subsection, question) in enumerate(selected2[:25], 1):
        f.write(f'{section}\n\n{subsection}\n\n**{i}. {question[10:]}\n\n---\n\n')

    for i, (section, subsection, question) in enumerate(selected2[25:], 26):
        f.write(f'{section}\n\n{subsection}\n\n**{i}. {question[10:]}\n\n---\n\n')

print("生成完成！")
print(f"文件1: 随机面试题目-批次1.md")
print(f"文件2: 随机面试题目-批次2.md")

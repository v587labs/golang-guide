#!/usr/bin/env python3
import re

# 定义排序顺序
ORDER_MAP = {
    'Golang': 1,
    'PostgreSQL': 2,
    'Linux': 3,
    'Docker': 4,
    'Kubernetes': 5,
    'AI': 6,
    '区块链': 7,
    'Redis': 8,
    '计算机网络': 9,
}

def parse_file(content):
    blocks = content.split('\n---\n')
    questions = []

    for block in blocks:
        lines = block.strip().split('\n')
        section = ""
        subsection = ""
        question = ""

        for line in lines:
            if line.startswith('## '):
                section = line
            elif line.startswith('### '):
                subsection = line
            elif line.startswith('**'):
                question = line

        if section and question:
            # 从section中提取板块名称
            match = re.search(r'## (\d+)\. (.+) 面试题', section)
            if match:
                num, name = match.groups()
                questions.append({
                    'num': int(num),
                    'name': name,
                    'section': section,
                    'subsection': subsection,
                    'question': question
                })

    return questions

def sort_questions(questions):
    def get_order(q):
        name = q['name']
        for key, val in ORDER_MAP.items():
            if key in name:
                return val
        return 999

    return sorted(questions, key=get_order)

def generate_file(questions, filename, title):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n')
        f.write('**抽题日期**: 2026-04-09\n\n')
        f.write('**题目数量**: 50\n\n')
        f.write('---\n\n')

        current_order = None
        idx = 1

        for q in questions:
            order = get_order_key(q['name'])
            if order != current_order:
                current_order = order
                f.write(f'\n## {q["section"].replace("## ", "")}\n\n')

            f.write(f'{q["subsection"]}\n\n')
            f.write(f'**{idx}. {q["question"][10:]}\n\n---\n\n')
            idx += 1

def get_order_key(name):
    for key, val in ORDER_MAP.items():
        if key in name:
            return val
    return 999

# 处理文件1
with open('随机面试题目-批次1.md', 'r', encoding='utf-8') as f:
    content1 = f.read()

# 处理文件2
with open('随机面试题目-批次2.md', 'r', encoding='utf-8') as f:
    content2 = f.read()

questions1 = parse_file(content1)
questions2 = parse_file(content2)

sorted1 = sort_questions(questions1)
sorted2 = sort_questions(questions2)

generate_file(sorted1, '随机面试题目-批次1-整理版.md', '随机面试题目（批次1-整理版）')
generate_file(sorted2, '随机面试题目-批次2-整理版.md', '随机面试题目（批次2-整理版）')

print("整理完成！")
print("文件1: 随机面试题目-批次1-整理版.md")
print("文件2: 随机面试题目-批次2-整理版.md")

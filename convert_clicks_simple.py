#!/usr/bin/env python3
"""
简单的 v-clicks 到 v-click at 转换器
"""

import re
import sys

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 正则表达式匹配 <v-clicks>...</v-clicks> 块
    pattern = r'<v-clicks>(.*?)</v-clicks>'
    
    def replace_v_clicks(match):
        inner_content = match.group(1)
        
        # 分割成各个部分（以 ### 开头的块）
        blocks = re.split(r'(\n### )', inner_content)
        
        result = []
        click_index = 1
        
        i = 0
        while i < len(blocks):
            if blocks[i] == '\n### ' and i + 1 < len(blocks):
                # 这是一个新块
                block_content = blocks[i] + blocks[i + 1]
                result.append(f'\n<v-click at="{click_index}">\n{block_content}\n</v-click>\n')
                click_index += 1
                i += 2
            else:
                # 跳过空白或其他内容
                i += 1
        
        return ''.join(result)
    
    # 执行替换
    converted = re.sub(pattern, replace_v_clicks, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"✓ 转换完成: {filepath}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filepath in sys.argv[1:]:
            convert_file(filepath)
    else:
        print("用法: python3 convert_clicks_simple.py <文件1> <文件2> ...")

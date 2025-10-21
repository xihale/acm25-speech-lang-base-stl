#!/usr/bin/env python3
"""
将所有使用 <v-clicks> 的幻灯片转换为使用 <v-click at="X"> 的格式，
以实现左侧代码高亮与右侧解释的同步。
"""

import re
import sys

def convert_v_clicks_to_v_click_at(content):
    """
    将 <v-clicks>...</v-clicks> 转换为独立的 <v-click at="X">...</v-click>
    """
    result = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # 检测 <v-clicks> 开始
        if '<v-clicks>' in line:
            # 找到对应的 </v-clicks>
            click_index = 1  # 从 1 开始，因为 0 是 'all'
            i += 1
            
            # 收集 <v-clicks> 内部的所有块
            blocks = []
            current_block = []
            
            while i < len(lines) and '</v-clicks>' not in lines[i]:
                line = lines[i]
                
                # 检测一个新的块（以 ### 开头）
                if line.strip().startswith('###'):
                    if current_block:
                        blocks.append(current_block)
                        current_block = []
                
                current_block.append(line)
                i += 1
            
            # 添加最后一个块
            if current_block:
                blocks.append(current_block)
            
            # 生成带 at 属性的 v-click
            for block_index, block in enumerate(blocks):
                result.append(f'<v-click at="{click_index}">')
                result.append('')
                result.extend(block)
                result.append('')
                result.append('</v-click>')
                result.append('')
                click_index += 1
            
            # 跳过 </v-clicks>
            if i < len(lines) and '</v-clicks>' in lines[i]:
                i += 1
        else:
            result.append(line)
            i += 1
    
    return '\n'.join(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_clicks.py <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    converted = convert_v_clicks_to_v_click_at(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"✓ Converted {filepath}")

if __name__ == '__main__':
    main()

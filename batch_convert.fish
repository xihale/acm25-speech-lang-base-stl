#!/usr/bin/env fish

# 批量转换所有 markdown 文件中的 v-clicks 为 v-click at

set files pages/01-language-basics.md pages/02-stl-containers.md pages/03-stl-algorithms.md pages/04-advanced-features.md

for file in $files
    echo "处理 $file..."
    
    # 使用 sed 进行替换
    # 这个脚本会查找 <v-clicks> 并将其内容转换为独立的 <v-click at="X">
    
    # 由于复杂性，我们使用 Python 脚本
    python3 convert_clicks_simple.py "$file"
    
    echo "✓ 完成 $file"
end

echo "所有文件转换完成！"

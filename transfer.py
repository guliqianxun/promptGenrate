import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 将 \( 和 \) 替换为 $ if which extra space move it
    content = re.sub(r'\\\(', r'$', content)
    content = re.sub(r'\\\)', r'$', content)

    # 将 \[ 替换为 $$\n
    content = re.sub(r'\\\[(\n\s*)', r'$$', content)

    # 将 \] 替换为 \n$$
    content = re.sub(r'(\n\s*)\\\]', r'$$', content)

    content = re.sub(r'\$(\s+)', r'$', content)

    with open('process.txt', 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    file_path = 'content.txt'
    process_file(file_path)
    print("文件处理完成。")
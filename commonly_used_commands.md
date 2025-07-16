# 根据工作环境分析推测的常用命令行指令

## 说明
由于我无法访问您的历史命令记录，以下是基于当前工作环境分析推测的常用命令：

## Python 开发相关
```bash
# Python 包管理
pip install -r requirements.txt
pip install [package_name]
pip list
pip show [package_name]

# Python 脚本执行
python3 translate_md_to_epub.py
python3 clean_md.py
python3 decode_progress.py
python3 merge_paragraphs.py
python3 reduce_paragraphs.py
```

## Git 版本控制
```bash
# 基本 Git 操作
git status
git add .
git commit -m "commit message"
git push origin main
git pull origin main
git log --oneline
git diff
git branch
git checkout [branch_name]
```

## 文件操作
```bash
# 文件和目录操作
ls -la
cd [directory]
mkdir [directory_name]
rm [file_name]
cp [source] [destination]
mv [source] [destination]
find . -name "*.py"
grep -r "keyword" .
```

## 文本编辑
```bash
# 文本编辑器
vim [file_name]
nano [file_name]
cat [file_name]
less [file_name]
head -n 10 [file_name]
tail -n 10 [file_name]
```

## 网络和下载
```bash
# 网络操作
curl -O [url]
wget [url]
ping [host]
```

## 系统信息
```bash
# 系统和进程
ps aux
top
df -h
du -sh *
free -h
uname -a
```

## 文本处理（基于项目特点）
```bash
# 由于项目涉及文本处理和翻译
wc -l [file_name]
sort [file_name]
uniq [file_name]
cut -d',' -f1 [file_name]
```

## 注意
这些命令是基于您当前的工作环境（Python 文本处理项目）推测的常用命令。如果您需要查看实际的命令使用记录，可以：
1. 检查 `~/.bash_history` 文件
2. 使用 `history` 命令查看当前会话历史
3. 在 shell 中按上下箭头键查看最近使用的命令
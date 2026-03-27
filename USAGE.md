# AI Hot Digest - 配置和使用指南

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yuxi-lsy/ai-hot-digest.git
cd ai-hot-digest
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量（可选）

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```bash
# GitHub Token (用于访问 GitHub API，推荐配置)
GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# 获取 GitHub Token:
# 1. 访问 https://github.com/settings/tokens
# 2. 点击 "Generate new token (classic)"
# 3. 选择 "repo" 权限
# 4. 复制生成的 token
```

### 4. 手动运行

```bash
# 方式 1: 使用一键脚本
./run.sh

# 方式 2: 分步运行
python scripts/collect_news.py
python scripts/collect_github.py
python scripts/collect_skills.py
python scripts/generate_report.py
```

### 5. 查看报告

生成的报告在 `output/` 目录：

```bash
# 完整日报
cat output/$(date +%Y-%m-%d)-summary.md

# 快速预览
cat output/$(date +%Y-%m-%d)-quick.md
```

---

## ⚙️ GitHub Actions 自动运行

### 启用自动运行

1. 访问 https://github.com/yuxi-lsy/ai-hot-digest/actions
2. 点击 **"I understand my workflows, go ahead and enable them"**
3. 点击 **"Run workflow"** 手动测试一次
4. 之后每日北京时间 8:00 自动运行

### 修改运行时间

编辑 `.github/workflows/daily-digest.yml`:

```yaml
on:
  schedule:
    # cron 表达式 (分钟 小时 日期 月份 星期) UTC 时间
    - cron: '0 0 * * *'  # 每日 UTC 0:00 = 北京 8:00
```

**常用时间配置:**

```bash
# 每日北京时间 8:00
- cron: '0 0 * * *'

# 每日北京时间 9:00
- cron: '0 1 * * *'

# 每 6 小时一次
- cron: '0 */6 * * *'

# 每周一 9:00
- cron: '0 1 * * 1'
```

---

## 📊 数据源说明

### AI 资讯收集

- **来源**: Web Search (Google/Bing)
- **关键词**: AI news, machine learning, LLM, deep learning
- **更新频率**: 每日
- **输出**: `data/YYYY-MM-DD-ai-news.json`

### GitHub Trending

- **来源**: GitHub API
- **筛选条件**: 
  - 编程语言：Python, TypeScript, Go
  - 创建时间：最近 7 天
  - 最少 Stars: 100
- **更新频率**: 每日
- **输出**: `data/YYYY-MM-DD-github-trending.json`

### OpenClaw Skill 更新

- **来源**: 
  - ClawHub API (如果可用)
  - GitHub Search (openclaw-skill 相关仓库)
- **更新频率**: 每日
- **输出**: `data/YYYY-MM-DD-skills-update.json`

---

## 🔧 自定义配置

### 添加新的数据源

在 `scripts/` 目录下创建新的收集脚本：

```python
#!/usr/bin/env python3
"""
收集 XXX 数据
"""

import json
from datetime import datetime
from pathlib import Path

def collect_xxx():
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 你的收集逻辑
    data = []
    
    output_file = Path("data") / f"{today}-xxx.json"
    output_file.parent.mkdir(exist_ok=True, parents=True)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "date": today,
            "data": data,
            "collected_at": datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    collect_xxx()
```

然后在工作流中添加运行步骤。

### 修改报告模板

编辑 `scripts/generate_report.py` 中的模板字符串。

### 添加通知推送

在 `generate_report.py` 末尾添加推送逻辑：

```python
# 推送到飞书
def send_to_feishu(webhook_url, content):
    import requests
    requests.post(webhook_url, json={"content": content})

# 推送到 Discord
def send_to_discord(webhook_url, content):
    import requests
    requests.post(webhook_url, json={"content": content})
```

---

## 📁 文件结构说明

```
ai-hot-digest/
├── .github/workflows/
│   └── daily-digest.yml    # GitHub Actions 配置
├── scripts/
│   ├── collect_news.py     # AI 资讯收集
│   ├── collect_github.py   # GitHub Trending 收集
│   ├── collect_skills.py   # Skill 更新收集
│   └── generate_report.py  # 报告生成
├── data/                    # 原始数据 (JSON)
│   ├── 2026-03-27-ai-news.json
│   ├── 2026-03-27-github-trending.json
│   └── 2026-03-27-skills-update.json
├── output/                  # 生成的报告 (Markdown)
│   ├── 2026-03-27-summary.md    # 完整日报
│   └── 2026-03-27-quick.md      # 快速预览
├── .env.example            # 环境变量示例
├── .gitignore              # Git 忽略文件
├── LICENSE                 # MIT License
├── README.md               # 项目说明
├── requirements.txt        # Python 依赖
└── run.sh                  # 一键运行脚本
```

---

## 🐛 常见问题

### 1. GitHub API 调用失败

**原因**: 未配置 GITHUB_TOKEN 或 token 过期

**解决**: 
```bash
# 重新生成 token
# https://github.com/settings/tokens
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

### 2. 报告为空

**原因**: 数据收集失败

**解决**: 检查 `data/` 目录下的 JSON 文件，查看是否有 error 字段

### 3. Actions 不运行

**原因**: 未启用 Actions

**解决**: 访问 Actions 页面手动启用

---

## 📬 反馈和建议

- **Issue**: https://github.com/yuxi-lsy/ai-hot-digest/issues
- **讨论**: https://github.com/yuxi-lsy/ai-hot-digest/discussions

---

**最后更新**: 2026-03-27  
**维护者**: @yuxi-lsy

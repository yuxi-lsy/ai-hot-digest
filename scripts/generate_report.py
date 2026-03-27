#!/usr/bin/env python3
"""
生成每日 AI 热门资讯报告
整合 AI 资讯、GitHub Trending 和 Skill 更新
"""

import json
from datetime import datetime
from pathlib import Path

def load_json_file(filepath):
    """加载 JSON 文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[WARN] 无法加载 {filepath}: {e}")
        return None

def generate_daily_report():
    """生成综合日报"""
    today = datetime.now().strftime("%Y-%m-%d")
    today_zh = datetime.now().strftime("%Y年%m月%d日")
    weekday = datetime.now().strftime("%A")
    
    print(f"[INFO] 生成 {today_zh} 的日报...")
    
    # 读取收集的数据
    data_dir = Path("data")
    
    ai_news_data = load_json_file(data_dir / f"{today}-ai-news.json")
    github_data = load_json_file(data_dir / f"{today}-github-trending.json")
    skills_data = load_json_file(data_dir / f"{today}-skills-update.json")
    
    # 提取数据
    ai_news = ai_news_data.get('news', []) if ai_news_data else []
    github_trending = github_data.get('trending', []) if github_data else []
    skills = skills_data.get('skills', []) if skills_data else []
    
    # 生成 AI 资讯部分
    ai_news_md = ""
    if ai_news:
        for i, news in enumerate(ai_news[:10], 1):
            ai_news_md += f"""
**{i}. {news.get('title', '无标题')}**

{news.get('summary', news.get('description', ''))}

> 📌 来源：{news.get('source', 'Unknown')} | [阅读原文]({news.get('url', '#')})

"""
    else:
        ai_news_md = "_暂无数据，等待首次运行收集_\n"
    
    # 生成 GitHub Trending 部分
    github_md = ""
    if github_trending:
        for i, project in enumerate(github_trending[:10], 1):
            stars = project.get('stars', 0)
            lang = project.get('language', 'Unknown')
            github_md += f"""
**{i}. [{project.get('name', 'unknown')}]({project.get('url', '#')})** by @{project.get('author', 'unknown')}

{project.get('description', '暂无描述')}

> ⭐ {stars:,} Stars | 🍴 {project.get('forks', 0):,} Forks | 💻 {lang}

"""
    else:
        github_md = "_暂无数据，等待首次运行收集_\n"
    
    # 生成 Skill 更新部分
    skills_md = ""
    if skills:
        for i, skill in enumerate(skills[:10], 1):
            skills_md += f"""
**{i}. [{skill.get('name', 'unknown')}]({skill.get('url', '#')})**

{skill.get('description', '暂无描述')}

> ⭐ {skill.get('stars', 0):,} Stars | 📂 {skill.get('category', 'General')} | 🕐 更新：{skill.get('updated_at', 'Unknown')}

"""
    else:
        skills_md = "_暂无数据，等待首次运行收集_\n"
    
    # 生成统计
    stats = f"""
| 类别 | 数量 |
|------|------|
| AI 资讯 | {len(ai_news)} |
| GitHub 项目 | {len(github_trending)} |
| Skill 更新 | {len(skills)} |
"""
    
    # 生成完整报告
    report = f"""# AI Hot Digest - {today_zh} ({weekday})

> 🤖 每日 AI 热门资讯、GitHub Trending 和 OpenClaw Skill 更新

---

## 📰 AI 资讯精选 {f"({len(ai_news)}条)" if ai_news else ""}

{ai_news_md}
---

## 🔥 GitHub Trending Top 10 {f"({len(github_trending)}个)" if github_trending else ""}

{github_md}
---

## 🛠️ OpenClaw Skill 更新 {f"({len(skills)}个)" if skills else ""}

{skills_md}
---

## 📊 今日统计

{stats}
---

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**数据来源**: AI Hot Digest Auto-Collector  
**星期**: {weekday}

---

📦 [GitHub 仓库](https://github.com/yuxi-lsy/ai-hot-digest) | 🤖 自动更新 | 📮 [提交 Issue](https://github.com/yuxi-lsy/ai-hot-digest/issues)

---

<div align="center">

**🌟 让 AI 资讯触手可及 | Made with ❤️ by @yuxi-lsy**

</div>
"""
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 保存综合日报
    output_file = output_dir / f"{today}-summary.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"[OK] 日报已生成：{output_file}")
    
    # 同时生成一个简短版本用于推送
    short_report = f"""# AI 日报速览 - {today}

## 📊 今日概览
- AI 资讯：{len(ai_news)} 条
- GitHub Trending: {len(github_trending)} 个
- Skill 更新：{len(skills)} 个

## 🔥 热门 Top 3

**AI 资讯:**
"""
    
    for i, news in enumerate(ai_news[:3], 1):
        short_report += f"\n{i}. {news.get('title', '无标题')}"
    
    short_report += "\n\n**GitHub 项目:**\n"
    for i, project in enumerate(github_trending[:3], 1):
        short_report += f"\n{i}. {project.get('name', 'unknown')} ({project.get('stars', 0):,}⭐)"
    
    short_report += "\n\n**Skill 更新:**\n"
    for i, skill in enumerate(skills[:3], 1):
        short_report += f"\n{i}. {skill.get('name', 'unknown')}"
    
    short_report += f"\n\n📖 [查看完整报告](https://github.com/yuxi-lsy/ai-hot-digest/blob/main/output/{today}-summary.md)"
    
    short_file = output_dir / f"{today}-quick.md"
    with open(short_file, "w", encoding="utf-8") as f:
        f.write(short_report)
    
    print(f"[OK] 速览已生成：{short_file}")
    
    return output_file

if __name__ == "__main__":
    generate_daily_report()

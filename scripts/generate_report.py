#!/usr/bin/env python3
"""
生成每日 AI 热门资讯报告
"""

import json
from datetime import datetime
from pathlib import Path

def generate_daily_report():
    """生成综合日报"""
    today = datetime.now().strftime("%Y-%m-%d")
    today_zh = datetime.now().strftime("%Y年%m月%d日")
    
    print(f"[INFO] 生成 {today_zh} 的日报...")
    
    # 读取收集的数据
    data_dir = Path("data")
    
    # 生成 markdown 报告
    report = f"""# AI Hot Digest - {today_zh}

> 每日 AI 热门资讯、GitHub Trending 和 OpenClaw Skill 更新

---

## 📰 AI 资讯精选

<!-- AI 新闻内容将自动填充 -->

_暂无数据，等待首次运行收集_

---

## 🔥 GitHub Trending Top 10

<!-- GitHub 热门项目将自动填充 -->

_暂无数据，等待首次运行收集_

---

## 🛠️ OpenClaw Skill 更新

<!-- Skill 更新将自动填充 -->

_暂无数据，等待首次运行收集_

---

## 📊 今日统计

| 类别 | 数量 |
|------|------|
| AI 资讯 | 0 |
| GitHub 项目 | 0 |
| Skill 更新 | 0 |

---

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**数据来源**: AI Hot Digest Auto-Collector

---

📦 [GitHub 仓库](https://github.com/yuxi-lsy/ai-hot-digest) | 🤖 自动更新
"""
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / f"{today}-summary.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"[OK] 日报已生成：{output_file}")
    return output_file

if __name__ == "__main__":
    generate_daily_report()

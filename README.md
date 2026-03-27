# AI Hot Digest 🤖

每日自动收集 AI 热门资讯、GitHub 热门项目和 OpenClaw 热门 Skill 更新。

## ✨ 功能特性

- 📰 **AI 资讯日报** - 自动搜索并整理最新 AI 行业新闻
- 🔥 **GitHub Trending** - 收集 GitHub 热门 AI 相关项目
- 🛠️ **Skill 更新** - 追踪 OpenClaw 生态系统中的热门 Skill
- 📊 **数据统计** - 自动生成统计报告和趋势分析

## 📁 目录结构

```
ai-hot-digest/
├── scripts/           # 自动化脚本
│   ├── collect_news.py      # 收集 AI 资讯
│   ├── collect_github.py    # 收集 GitHub trending
│   ├── collect_skills.py    # 收集 Skill 更新
│   └── generate_report.py   # 生成日报
├── data/              # 原始数据存放
├── output/            # 生成的报告
└── README.md
```

## 🚀 使用方式

### 手动运行

```bash
# 收集所有数据
python scripts/collect_news.py
python scripts/collect_github.py
python scripts/collect_skills.py

# 生成日报
python scripts/generate_report.py
```

### 自动运行 (GitHub Actions)

项目配置了 GitHub Actions，每日 UTC 0:00 自动运行并更新报告。

## 📅 输出内容

每日生成以下报告：

- `output/YYYY-MM-DD-ai-news.md` - AI 资讯日报
- `output/YYYY-MM-DD-github-trending.md` - GitHub 热门项目
- `output/YYYY-MM-DD-skills-update.md` - Skill 更新日志
- `output/YYYY-MM-DD-summary.md` - 综合日报

## 🔧 配置

编辑 `.env.example` 文件并重命名为 `.env`：

```bash
GITHUB_TOKEN=your_github_token
OPENCLAW_API_KEY=your_openclaw_key
```

## 📄 License

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**最后更新**: 自动更新
**维护者**: @yuxi-lsy

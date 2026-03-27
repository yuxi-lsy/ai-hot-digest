# AI Hot Digest 🤖

[![Daily Digest](https://github.com/yuxi-lsy/ai-hot-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/yuxi-lsy/ai-hot-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 每日自动收集 AI 热门资讯、GitHub Trending 和 OpenClaw Skill 更新

**🌐 在线查看**: [https://github.com/yuxi-lsy/ai-hot-digest](https://github.com/yuxi-lsy/ai-hot-digest)

---

## ✨ 功能特性

- 📰 **AI 资讯日报** - 自动搜索并整理最新 AI 行业新闻
- 🔥 **GitHub Trending** - 收集 GitHub 热门 AI 相关项目 (Top 10)
- 🛠️ **Skill 更新** - 追踪 OpenClaw/ClawHub 生态系统中的热门 Skill
- 📊 **数据统计** - 自动生成统计报告和趋势分析
- ⏰ **定时更新** - GitHub Actions 每日北京时间 8:00 自动运行

## 📁 目录结构

```
ai-hot-digest/
├── .github/workflows/   # GitHub Actions 配置
│   └── daily-digest.yml # 每日自动运行工作流
├── scripts/             # 自动化脚本
│   ├── collect_news.py      # 收集 AI 资讯
│   ├── collect_github.py    # 收集 GitHub trending
│   ├── collect_skills.py    # 收集 Skill 更新
│   └── generate_report.py   # 生成日报
├── data/                # 原始数据存放 (JSON)
├── output/              # 生成的报告 (Markdown)
├── README.md            # 本文件
└── .env.example         # 环境变量示例
```

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yuxi-lsy/ai-hot-digest.git
cd ai-hot-digest
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 GitHub Token
```

### 3. 安装依赖

```bash
pip install requests
```

### 4. 运行收集脚本

```bash
# 收集所有数据
python scripts/collect_news.py
python scripts/collect_github.py
python scripts/collect_skills.py

# 生成日报
python scripts/generate_report.py
```

## 📅 输出示例

每日生成综合日报 `output/YYYY-MM-DD-summary.md`：

```markdown
# AI Hot Digest - 2026 年 03 月 27 日

## 📰 AI 资讯精选
- OpenAI 发布 GPT-5.4 系列...
- Google DeepMind Nano Banana 2...

## 🔥 GitHub Trending Top 10
1. deer-flow (bytedance) - 2,394⭐今日
2. last30days-skill (mvanhorn) - 2,685⭐今日
...

## 🛠️ OpenClaw Skill 更新
- new-skill: 描述...
- updated-skill: 更新内容...
```

## ⏰ 自动运行

项目使用 GitHub Actions 每日自动运行：

- **运行时间**: 每日 UTC 0:00 (北京时间 8:00)
- **运行内容**: 收集数据 → 生成报告 → 自动提交
- **手动触发**: 在 Actions 页面点击 "Run workflow"

## 🔧 自定义

### 修改运行时间

编辑 `.github/workflows/daily-digest.yml`:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # 修改为你的时区
```

### 添加数据源

在 `scripts/` 目录下创建新的收集脚本，然后在 workflow 中添加运行步骤。

## 📊 API 使用

### GitHub API

项目使用 GitHub API 获取 Trending 数据，需要设置 `GITHUB_TOKEN`：

```bash
# 在 GitHub Settings → Developer settings → Personal access tokens 生成
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

## 🤝 贡献

欢迎贡献！请：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📬 联系方式

- **维护者**: [@yuxi-lsy](https://github.com/yuxi-lsy)
- **问题反馈**: [GitHub Issues](https://github.com/yuxi-lsy/ai-hot-digest/issues)

---

<div align="center">

**🤖 AI Hot Digest - 让 AI 资讯触手可及**

[⭐ Star](https://github.com/yuxi-lsy/ai-hot-digest) · [🍴 Fork](https://github.com/yuxi-lsy/ai-hot-digest/fork) · [📢 Share](https://github.com/yuxi-lsy/ai-hot-digest)

</div>

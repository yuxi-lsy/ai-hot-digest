#!/bin/bash
# AI Hot Digest - 一键运行脚本
# 用于手动收集数据并生成报告

set -e

echo "🤖 AI Hot Digest - 开始收集数据..."
echo "================================"

# 切换到项目目录
cd "$(dirname "$0")"

# 创建必要的目录
mkdir -p data output

# 1. 收集 AI 资讯
echo ""
echo "📰 收集 AI 资讯..."
python3 scripts/collect_news.py

# 2. 收集 GitHub Trending
echo ""
echo "🔥 收集 GitHub Trending..."
python3 scripts/collect_github.py

# 3. 收集 Skill 更新
echo ""
echo "🛠️  收集 Skill 更新..."
python3 scripts/collect_skills.py

# 4. 生成报告
echo ""
echo "📝 生成日报..."
python3 scripts/generate_report.py

echo ""
echo "================================"
echo "✅ 完成！报告已生成到 output/ 目录"
echo ""

# 显示今日统计
TODAY=$(date +%Y-%m-%d)
echo "📊 今日统计:"
if [ -f "data/${TODAY}-ai-news.json" ]; then
    AI_COUNT=$(python3 -c "import json; print(len(json.load(open('data/${TODAY}-ai-news.json')).get('news', [])))")
    echo "  - AI 资讯：${AI_COUNT} 条"
fi

if [ -f "data/${TODAY}-github-trending.json" ]; then
    GH_COUNT=$(python3 -c "import json; print(len(json.load(open('data/${TODAY}-github-trending.json')).get('trending', [])))")
    echo "  - GitHub 项目：${GH_COUNT} 个"
fi

if [ -f "data/${TODAY}-skills-update.json" ]; then
    SKILL_COUNT=$(python3 -c "import json; print(len(json.load(open('data/${TODAY}-skills-update.json')).get('skills', [])))")
    echo "  - Skill 更新：${SKILL_COUNT} 个"
fi

echo ""
echo "📄 查看报告：output/${TODAY}-summary.md"
echo "🚀 推送更改到 GitHub:"
echo "   git add -A && git commit -m 'chore: daily update $(date +%Y-%m-%d)' && git push"

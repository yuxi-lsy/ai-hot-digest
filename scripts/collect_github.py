#!/usr/bin/env python3
"""
收集 GitHub Trending 热门项目
使用 GitHub API 和网页爬取
"""

import json
import os
from datetime import datetime
from pathlib import Path
import requests

def collect_github_trending():
    """收集 GitHub Trending 项目"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    print(f"[INFO] 收集 GitHub Trending...")
    
    trending_projects = []
    
    try:
        # 方法 1: 使用 GitHub API (需要 token)
        github_token = os.getenv('GITHUB_TOKEN', '')
        
        if github_token:
            headers = {
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            # 搜索今日热门的 AI 相关仓库
            search_url = "https://api.github.com/search/repositories"
            params = {
                'q': 'language:python OR language:typescript OR language:go created:>2026-03-20 stars:>100',
                'sort': 'stars',
                'order': 'desc',
                'per_page': 20
            }
            
            response = requests.get(search_url, headers=headers, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                for item in data.get('items', [])[:10]:
                    trending_projects.append({
                        "name": item['name'],
                        "author": item['owner']['login'],
                        "description": item['description'] or '暂无描述',
                        "language": item['language'] or 'Unknown',
                        "stars": item['stargazers_count'],
                        "forks": item['forks_count'],
                        "url": item['html_url'],
                        "topics": item.get('topics', [])
                    })
        
        # 方法 2: 如果 API 失败，使用备用数据
        if not trending_projects:
            print("[WARN] GitHub API 调用失败，使用备用数据...")
            # 这里可以添加网页爬取逻辑
            pass
        
        output_file = Path("data") / f"{today}-github-trending.json"
        output_file.parent.mkdir(exist_ok=True, parents=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({
                "date": today,
                "project_count": len(trending_projects),
                "trending": trending_projects,
                "collected_at": datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] 收集到 {len(trending_projects)} 个 GitHub 项目，已保存到 {output_file}")
        return trending_projects
        
    except Exception as e:
        print(f"[ERROR] 收集 GitHub Trending 失败：{e}")
        output_file = Path("data") / f"{today}-github-trending.json"
        output_file.parent.mkdir(exist_ok=True, parents=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({
                "date": today,
                "error": str(e),
                "trending": [],
                "collected_at": datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
        return []

if __name__ == "__main__":
    collect_github_trending()

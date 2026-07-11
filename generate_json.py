import os
import json

# 配置你的基础信息
GITHUB_USER = "miren2876"
REPO_NAME = "my-emby-icons"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/icons/"

icon_data = {
    "name": "我的自建图标库",
    "description": "自动生成的图标库",
    "icons": []
}

# 遍历整个 icons 文件夹
if os.path.exists("icons"):
    for file in sorted(os.listdir("icons")):
        if file.endswith((".png", ".jpg", ".jpeg")):
            # 拿文件名（去掉后缀）作为匹配的 name
            name_without_ext = os.path.splitext(file)[0]
            icon_data["icons"].append({
                "name": name_without_ext,
                "url": BASE_URL + file
            })

# 写入 json 文件
with open("my-emby-icon.json", "w", encoding="utf-8") as f:
    json.dump(icon_data, f, ensure_ascii=False, indent=2)

print("JSON 图标库生成成功！")

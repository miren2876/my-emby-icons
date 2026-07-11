# 我的自用 Emby / 流媒体播放器图标库

这是一个专门为第三方 Emby 播放器（如 Hills、Fileball、Senplayer 等）以及网络代理工具（Quantumult X / Mihomo）定制的远程图标库，用于影视服务器与流媒体分流节点的外观美化。

特点：支持 GitHub Actions 全自动更新，提供国内直连加速加载链接。

---

## 订阅链接

请根据你的网络环境，选择以下任意一种链接导入到你的客户端中：

1. jsDelivr 加速线路 (国内直连推荐)
   https://cdn.jsdelivr.net/gh/miren2876/my-emby-icons@main/my-emby-icon.json

2. GitHub Proxy 加速线路 (备用)
   https://ghfast.top/https://raw.githubusercontent.com/miren2876/my-emby-icons/main/my-emby-icon.json

3. GitHub 官方原始链接 (需要代理环境)
   https://raw.githubusercontent.com/miren2876/my-emby-icons/main/my-emby-icon.json

---

## 客户端配置指南

### 1. 在 Hills / Fileball 等播放器中使用
1. 进入播放器的 设置 -> 外观/样式 -> 图标订阅。
2. 点击 添加订阅，粘贴上方推荐的 jsDelivr 加速链接。
3. 确保你的 Emby 服务器名称或媒体库名称中，包含图标文件名（不带后缀）。例如：服务器名叫 yecaodi，则会自动匹配并挂载 icons 文件夹下的 yecaodi.jpg 图标。

### 2. 在 Quantumult X 中使用
1. 长按主界面下方的策略组圆形图标。
2. 点击右上角的加号。
3. 粘贴上述 JSON 链接引入，策略组内的节点即可自动匹配对应图标。

---

## 自动化维护说明

本仓库已接入 GitHub Actions 自动化脚本：
* 图标存放路径：请将所有图标存放在 /icons 文件夹中。
* 自动同步：无论是新增、修改还是删除图标，只要向 main 分支提交变动，后台脚本都会自动重新扫描并刷新 my-emby-icon.json 索引文件，无需手动干预。

---

## 声明
* 本项目匹配规则与自动化灵感参考自开源项目。
* 仓库内部分图标素材来源于网络，版权归原作者所有。仅供个人学习与分流美化交流使用，严禁用于商业用途。

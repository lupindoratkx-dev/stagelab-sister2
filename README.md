# StageLab GitHub Pages 部署包

当前版本：V5。包含九节综艺舞美课件、五步双层视线样段、人物律动、舞台灯光、知识弹窗及真实现场图片。首页是本目录中的 `index.html`。

## 上传并生成网址

1. 解压 `StageLab_GitHub_Pages_V5.zip`，进入解压后的目录，确认能直接看见 `index.html`、`style.css`、`course.css`、`experience.css`、`src`、`base`、`vendor`、`fonts`、`images` 等文件或文件夹。
2. 在 GitHub 新建一个仓库，例如 `stagelab`。使用 GitHub Free 时选择 **Public**。仓库名称可以自行决定。
3. 在仓库的 **Code → Add file → Upload files** 中，上传解压后的全部文件和文件夹。请上传目录里面的内容，使 `index.html` 直接位于仓库根目录；ZIP 压缩包本身不作为网页入口。
4. 确认文件提交到 `main` 分支。提交后，仓库首页文件列表里应直接出现 `index.html` 和 `README.md`，并能看到 `src`、`vendor` 等文件夹。
5. 打开仓库 **Settings → Pages**，在 **Build and deployment** 中选择：

   - **Source**：`Deploy from a branch`
   - **Branch**：`main`
   - **Folder**：`/ (root)`

6. 点击 **Save**，等待 GitHub 完成部署。在同一页面点击 **Visit site** 或打开页面显示的网址。GitHub 官方说明，发布更新可能需要最多约 10 分钟。

本包为准备好的静态网页，可直接使用分支根目录发布。将 `.nojekyll` 一并上传，以按静态文件发布。此方式在线运行不需要安装 Node.js、npm 或 Python。

## 发布后检查

- 打开首页，向下滚动或通过章节目录进入课程。
- 进入“双层结构的视线”，依次查看整体、眼点、剖开、比较和现场五步。
- 在比较区切换前排、后排、上下层和头腰脚，确认图解与判断文字更新。
- 在“从一个人到七个人”中展开“舞台设置”，可切换 Jazz、Hip-hop、灯光和速度。
- 手机端使用顶部章节下拉菜单。
- 节目视频通过“选择本地正片片段”从本机选取；网页包内已包含现场照片，正片视频由教师自行准备。

## 本地预览

GitHub Pages 发布后直接访问生成的网址即可。本地检查时，若电脑已安装 Python 3，Windows 可双击 `start.bat`；其他系统在本目录运行 `python3 start.py`。浏览器会打开本地预览。

请通过 HTTP 预览或 GitHub Pages 打开课件。直接双击 `index.html` 使用 `file://` 地址时，浏览器可能限制脚本模块加载。

## 文件位置

| 文件或目录 | 内容 |
| --- | --- |
| `index.html` | 当前完整课程的入口与页面文字 |
| `course.css`、`experience.css`、`style.css` | 页面排版、五步样段与基础样式 |
| `src/` | 滚动镜头、三维适配、舞蹈、灯光与图解 |
| `base/` | 舞台模型和完整知识说明 |
| `vendor/` | 已保存的 Three.js、GSAP 和 ScrollTrigger |
| `fonts/` | 已保存的字体及字体许可 |
| `images/` | 现场图片及来源记录 |
| `sample.html` | 原视线样章 |
| `legacy/` | 原 V1 课件 |
| `.nojekyll` | GitHub Pages 的静态发布标记 |

文件夹名称和相对位置需要一起保留。本包已按 GitHub 项目网址的子目录方式检查路径，可用于任意仓库名称。

## 修改与更新

修改文字或样式后，把改动的文件上传到同一个 `main` 分支即可触发更新。主页面的文字位于 `index.html`，展开知识说明位于 `base/course.js`；样段的动态提示还涉及 `src/sight-graphics.js` 与 `src/lesson.js`。

## 常见情况

- **打开显示 README 而不是课件**：检查 Pages 是否选了 `main` 和 `/ (root)`，以及仓库根目录是否有 `index.html`。
- **文字显示，模型或图片不显示**：检查 `src`、`base`、`vendor`、`fonts`、`images` 是否完整上传，大小写是否保留。
- **页面是旧版本**：等待部署完成后刷新页面；可在仓库 Actions 页面查看部署结果。
- **不支持 WebGL2 的浏览器**：当前课程会使用兼容图解模式；仍可使用滚动、眼点比较和知识说明。完整三维阴影的表现取决于实际设备。

## 资料与许可

舞台尺寸、人物、队形和机构为教学示意。现场照片的来源保存在 `images` 的来源记录中。字体和第三方脚本的许可说明保留在对应目录。

## GitHub 官方说明

- [创建 GitHub Pages 网站](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [设置发布分支和文件夹](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [上传文件和文件夹](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

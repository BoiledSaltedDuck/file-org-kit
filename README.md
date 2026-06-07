# file-org-kit 文件智能分类整理工具

[![PyPI version](https://img.shields.io/pypi/v/file-org-kit)](https://pypi.org/project/file-org-kit/)
[![Downloads](https://img.shields.io/pypi/dm/file-org-kit)](https://pypi.org/project/file-org-kit/)
[![License](https://img.shields.io/pypi/l/file-org-kit)](https://github.com/BoiledSaltedDuck/file-org-kit/blob/main/LICENSE)

## 安装

```bash
pip install file-org-kit
```

## 用法

```bash
# 按文件类型分类
file-org ./下载/ type ./整理后/

# 按修改日期分类
file-org ./桌面/ date
```

## 按类型分类 (type)

自动识别以下文件类型并分类到对应目录：

| 类别 | 支持的扩展名 |
|------|------------|
| 图片 | jpg, png, gif, webp, svg, bmp, tiff... |
| 文档 | pdf, doc, xls, ppt, txt, md, csv... |
| 压缩包 | zip, rar, 7z, tar, gz, bz2... |
| 视频 | mp4, avi, mkv, mov, flv... |
| 音频 | mp3, wav, flac, aac, ogg... |
| 代码 | py, js, java, go, rs, cpp, rb... |
| 网页 | html, css, scss... |
| 配置 | json, xml, yaml, toml, ini... |
| 可执行 | exe, msi, apk, deb, rpm... |
| 字体 | ttf, otf, woff... |

## 按日期分类 (date)

按文件的最后修改时间，自动以 `年-月` 格式分目录归档。

## 特点

- 零配置，安装即用
- 自动处理重名文件（添加编号后缀）
- 安全移动，非复制
- 纯 Python，零依赖

## 支持

如果 file-org-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️

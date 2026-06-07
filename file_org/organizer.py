#!/usr/bin/env python3
"""
file-org-kit - 文件智能分类整理工具
功能：按扩展名/文件类型自动将文件分类到对应目录
用法：file-org [输入目录] [模式] [输出目录(可选)]
      file-org ./下载/ type ./整理后/
      file-org ./桌面/ date
"""
import sys
import shutil
from pathlib import Path
from datetime import datetime

# 文件类型分类规则
FILE_CATEGORIES = {
    "图片": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff', '.tif', '.psd', '.raw'],
    "文档": ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md', '.csv', '.odt', '.odp', '.ods'],
    "压缩包": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.zst', '.iso'],
    "视频": ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'],
    "音频": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
    "代码": ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.h', '.hpp', '.go', '.rs', '.rb', '.php', '.swift', '.kt', '.scala', '.sh', '.bash', '.zsh', '.sql', '.r', '.pl'],
    "网页": ['.html', '.htm', '.css', '.scss', '.less', '.jsx', '.tsx', '.vue', '.svelte'],
    "配置文件": ['.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf', '.env', '.properties'],
    "可执行文件": ['.exe', '.msi', '.appimage', '.deb', '.rpm', '.dmg', '.apk'],
    "字体": ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
}

def _get_category(ext):
    """根据扩展名返回文件类别"""
    ext = ext.lower()
    for category, exts in FILE_CATEGORIES.items():
        if ext in exts:
            return category
    return "其他"

def _get_month_dir(date_obj):
    """根据日期返回月份目录名，如 2026-06"""
    return date_obj.strftime("%Y-%m")

def org_by_type(input_dir, output_dir):
    """按类型分类"""
    src_path = Path(input_dir)
    dst_path = Path(output_dir)
    return _organize_files(src_path, dst_path, "type")

def org_by_date(input_dir, output_dir):
    """按日期分类"""
    src_path = Path(input_dir)
    dst_path = Path(output_dir)
    return _organize_files(src_path, dst_path, "date")

def _organize_files(src_path, dst_path, mode):
    if not src_path.exists():
        print(f"错误：目录 {src_path} 不存在")
        return False

    files = [f for f in src_path.iterdir() if f.is_file()]
    if not files:
        print(f"目录 {src_path} 中没有文件")
        return False

    print(f"找到 {len(files)} 个文件")
    moved = 0

    for f in sorted(files):
        try:
            if mode == "type":
                cat = _get_category(f.suffix)
                target_dir = dst_path / cat
            elif mode == "date":
                mtime = datetime.fromtimestamp(f.stat().st_mtime)
                target_dir = dst_path / _get_month_dir(mtime)
            else:
                return False

            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / f.name

            # 处理重名
            counter = 1
            while target_path.exists():
                stem = f.stem
                target_path = target_dir / f"{stem}_{counter}{f.suffix}"
                counter += 1

            shutil.move(str(f), str(target_path))
            print(f"  ✓ {f.name} → {target_dir.name}/")
            moved += 1

        except Exception as e:
            print(f"  ✗ {f.name} 移动失败: {e}")

    print(f"\n完成！成功整理 {moved}/{len(files)} 个文件到 {dst_path}")
    _show_promotion()
    return moved > 0

def _show_promotion():
    print("\n" + "=" * 55)
    print("  🔧 file-org-kit - 文件智能分类整理工具")
    print("  📦 pip install file-org-kit")
    print("  ☕ 如果帮到了您，欢迎打赏支持:")
    print("     USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("  ⭐ https://github.com/BoiledSaltedDuck/file-org-kit")
    print("=" * 55)

def main():
    if len(sys.argv) < 3:
        print("用法: file-org [输入目录] [模式] [输出目录(可选)]")
        print("模式:")
        print("  type   - 按文件类型分类（图片、文档、视频等）")
        print("  date   - 按修改日期分类（按年月分目录）")
        print("示例: file-org ./下载/ type ./整理后/")
        print("      file-org ./桌面/ date")
        sys.exit(1)

    input_dir = sys.argv[1]
    mode = sys.argv[2].lower()

    if mode not in ("type", "date"):
        print(f"错误：不支持的模式 '{mode}'，仅支持 type 和 date")
        sys.exit(1)

    output_dir = sys.argv[3] if len(sys.argv) > 3 else f"{input_dir.rstrip('/')}_整理后"

    if mode == "type":
        success = org_by_type(input_dir, output_dir)
    else:
        success = org_by_date(input_dir, output_dir)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

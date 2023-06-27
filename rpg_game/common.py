import sys
import os


def resource_path(filename: str) -> str:
    """リソースのパスを返す関数"""
    # sys._MEIPASSが存在する場合は、そのパスと渡されたファイル名を結合して返す
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)

    # そうでない場合は、現在のディレクトリのパスと渡されたファイル名を結合して返す
    return os.path.join(filename)

# 🧩 競技プログラミング用 Python 開発環境（Arch + uv + VS Code）

## 概要

この環境は、**Python 3.11 + uv + VS Code** を使った  
軽量・高速な競技プログラミング用セットアップです。

- `uv`: Rust 製の超高速パッケージマネージャ（pip の代替）
- `venv`: プロジェクトごとに自動生成される仮想環境
- `VS Code`: コード整形・即実行・自動保存対応

---

## セットアップ手順

### 1. Python 3.11 をインストール

```bash
yay -S python311
yay -S uv
```

### 実行

```bash
uv run main.py < input.txt
```

もしくは
`ctrl shift B`

### デバッガ

`f5`

### メモ

**GCD** : Greatest Common Divisor：最大公約数
**LCM** : Least Common Multiple：最小公倍数

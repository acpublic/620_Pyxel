# Pyxel
- https://github.com/kitao/pyxel/blob/main/docs/README.ja.md

## VScode
- https://qiita.com/kitao/items/04b6ab72d957de10f9a7

## インストール
```
sudo pip3 install -U pyxel
```
## 基本構成
- 初期化 (__init__): 画面サイズの設定 (pyxel.init)とupdate/drawの起動 (pyxel.run)
- 更新 (update): ゲームのロジックを実行
- 描画 (draw): グラフィックを表示
- デフォルトfps: 30
## リソースの作成方法
Pyxel Editorを使用して、Pyxelアプリケーションで使用する画像やサウンドを作成
```
pyxel edit Pyxelリソースファイル
```

## Pyxelアプリケーションファイル (.pyxapp) の作成
```
pyxel package pyxel ./pyxel/main.py
```
## PyxelアプリケーションファイルからHTMLファイルへの変換
```
mkdir web
cd web
pyxel app2html ../pyxel.pyxapp
```

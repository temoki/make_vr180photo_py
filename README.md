# make_vr180photo.py

左眼カメラ画像と右眼カメラ画像を結合して VR180 3D フォトを作成する Python スクリプト。

* [Cardboard Camera VR Photo Format](https://developers.google.com/vr/reference/cardboard-camera-vr-photo-format)
* [Photo Sphere XMP メタデータ](https://developers.google.com/streetview/spherical-metadata)

## 準備

### Python 2

[Python 2](https://www.python.org) が必要（Python 3 では動作しない）。macOS にはプリインストールされているはず。

### python-xmp-toolkit インストール

[XMP](https://www.adobe.com/products/xmp.html) の付与に [python-xmp-toolkit](https://github.com/python-xmp-toolkit/python-xmp-toolkit) を使うのでインストールが必要。ソースリポジトリに含まれるセットアップを実行すれば良い。

```sh
# リポジトリをクローン
git clone https://github.com/python-xmp-toolkit/python-xmp-toolkit.git

# リポジトリディレクトリへ移動
cd python-xmp-toolkit

# セットアップを実行
python setup.py install
```

参考: [Installation](http://python-xmp-toolkit.readthedocs.io/en/latest/installation.html#python-xmp-toolkit)

### Exempi インストール

python-xmp-toolkit は [Exepi](https://libopenraw.freedesktop.org/wiki/Exempi/) を使うのでインストールが必要。[Homebrew](https://brew.sh/index_ja) でインストールするのが手っ取り早い。

```sh
brew install exempi
```

## 使い方

* 左眼視点の画像と右目視点の画像をJPEG形式で用意する
* 両画像は同じサイズになっている必要がある
* 下記のようにしてスクリプトを実行すると左眼画像と同じ位置に結合されたVR180 3Dフォトファイルが作成される

```sh
# python make_vr180photo.py {左眼画像ファイルパス} {右目画像ファイルパス} {画像幅(ピクセル)} {画像高さ(ピクセル)}
python make_vr180photo.py left.jpg right.jpg 1280 1280
# -> left.vr.jpg
```

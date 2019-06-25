"""
    SVMアルゴリズムで手書き文字の判定を学習し、また結果を評価します.
"""
import os

if __name__ == "__main__":

    if not os.path.exists("result"):
        os.mkdir("result")

    """
        **** ここを実装します（基礎課題） ****
        `csv`フォルダからデータを読み込み、SVMアルゴリズムを用いた学習を行ってください。
        そして学習結果を`result`フォルダに`svm.pkl`という名前で保存してください。

        実装ステップ：
            ・トレーニングデータを読み込む
            ・SVGアルゴリズムによる学習を行う
            ・テストデータを読み込む
            ・精度とメトリクスによる性能評価を行う
            ・学習結果を`result/svm.pkl`ファイルとして保存する

        参考になる情報
            講義スライドや答えを適宜確認しながら実装してみてください。
            サンプルを見ながら手を動かしながら学ぶという感じがお勧めです。

        ここが一番大変なところです。
        ぜひぜひ頑張ってください！！
    """
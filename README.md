## 猫相談所


![test](https://github.com/ken222d/Homework1_robosys/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/github/license/ken222d/Homework1_robosys)


## コマンドの説明


このコマンドはあなたの現在の調子を聞いて, それに応じて猫が癒やしてくれるものです. 


## 使い方


```bash
$ git clone https://github.com/ken222d/Homework1_robosys
$ cd Homework1_robosys
$ echo 寂しい | ./Consult_cat   　　　　　　　　　　　　　　　　　　　　　　　　　　#実行その１（調子: 寂しい）
今日の調子は寂しい（例: 絶好調、疲れた、眠い、寂しいなど）
寂しい時ですね…。猫が膝の上でごろごろしながら『大丈夫だよ』と言って いるようです🌙🐈　#結果
$./Consult_cat                                                                      #実行その２
元気                               　　　　　　　　　　　　　　　　　　　　　　　　　　#あなたの調子を入力（調子: 元気）
今日の調子は元気（例: 絶好調、疲れた、眠い、寂しいなど）
にゃんにゃん！元気なんですね！猫も一緒にごろごろ嬉しい気分です✨😺　　　　　　　　　　#結果　
```


## 利用可能な言葉


猫に応えをもらうためには, 以下の言葉が含まれる文章を入力してください. （ひらがなでも可能）


* :幸せ、最高、絶好調、元気
* :辛い、悲しい、寂しい、しんどい
* :疲れた、だるい、眠い
* :普通、まあまあ、特に無し、特に無い


例: 今日はとても疲れた。

上記の言葉が含まれないとき, 猫がどんな気分か聞くようになっています. 


## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7 ~ 3.10  


## テスト環境
- Ubuntu 22.04.5 LTS


## 参考資料
* [ロボットシステム学 第3回: Linux環境でのPythonプログラミングⅡ](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson3.html)
* [ロボットシステム学 第5回: 著作権とライセンス](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson5.html)
* [ロボットシステム学 第6回: ソフトウェアのテスト](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson6.html)
* [ロボットシステム学 第7回: GitHubでのテスト](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson7.html)
* [GitHub License - Shields.io](https://shields.io/badges/git-hub-license)
* [ワークフロー状態バッジの追加](https://docs.github.com/ja/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge)


## ライセンスと著作権


- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- このパッケージのコードの一部は, 下記のスライド(CC-BY-SA 4.0 by ryuichi ueda)のものを本人の許可を得て自身の著作としたものです. 
  - [ryuichiueda/my_slides robosys_2024](http://github.com/ryuichiueda/slides_marp/tree/master/robosys2024) 
- © 2024 Kenta Ishizeki

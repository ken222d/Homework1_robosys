# Homework1_robosys
ロボットシステム学の課題1


![test](https://github.com/ken222d/Homework1_robosys/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/github/license/ken222d/Homework1_robosys)


## コマンドの説明


このコマンドは、あなたの現在の調子を聞いて、それに応じて猫が癒やしてくれるものです。


## 使い方


```bash
$ git clone https://github.com/ken222d/Homework1_robosys
$ cd Homework1_robosys
$ echo "調子" | ./Consult_cat.py
# または
# ./Consult_cat.py
# その後"調子"を入力
```


## 利用可能な言葉


猫に応えをもらうためには、以下の言葉が含まれる文章を入力しなければなりません。（ひらがなでも可能）


* :幸せ、最高、絶好調、元気
* :辛い、悲しい、寂しい、しんどい
* :疲れた、だるい、眠い
* :普通、まあまあ、特に無し、特に無い


例: 今日はとても疲れた。


## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7 ~ 3.10  


## テスト環境
- Ubuntu 22.04.5 LTS


## 参考資料
* [ロボットシステム学 第3回: Linux環境でのPythonプログラミングⅡ](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson3.html)
* [ロボットシステム学 第5回: 著作権とライセンス](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson5.html)
* [ロボットシステム学 第6回: ソフトウェアのテスト](https://github.com/shellgei/rusty_bash/blob/main/README.md)
* [ロボットシステム学 第7回: GitHubでのテスト](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson7.html)
* [GitHub License - Shields.io](https://shields.io/badges/git-hub-license)
* [ワークフロー状態バッジの追加](https://docs.github.com/ja/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge)


## ライセンスと著作権


- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます. 
- © 2024 Kenta Ishizeki

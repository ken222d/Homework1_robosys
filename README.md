# Homework1_robosys
ロボットシステム学の課題1


![test](https://github.com/ken222d/Homework1_robosys/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/github/license/ken222d/Homework1_robosys)


##コマンドの説明


このコマンドは、あなたの現在の調子を聞いて、それに応じて猫が癒やしてくれるものです。


## 使い方


```bash
$ git clone git@github.com:ken222d/Homework1_robosys.git
$ cd Homework1_robosys
$ echo "調子" | ./Consult_cat.py
# または
# ./Consult_cat.py
# その後"調子"を入力
```


##利用可能な言葉


猫に応えをもらうためには、以下の言葉が含まれる文章を入力しなければなりません。（ひらがなでも可能）


* :幸せ、最高、絶好調、元気
* :辛い、悲しい、寂しい、しんどい
* :疲れた、だるい、眠い
* :普通、まあまあ、特に無し、特に無い


例: 今日はとても疲れた。


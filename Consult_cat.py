#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Kenta ishizeki<a.w.g.d0201@icloud.com>
# SPDX-License-Identifier: BSD-3-Clause

import sys

for feeling in sys.stdin:

    print("今日の調子は" + feeling.strip() + "（例: 絶好調、疲れた、眠い、寂しいなど）")

    if "絶好調" in feeling or "最高" in feeling or "元気" in feeling or  "幸せ" in feeling or "ぜっこうちょう" in feeling or "さいこう" in feeling or "げんき" in feeling or "しあわせ" in feeling:
        print("にゃんにゃん！" + feeling.strip() + "なんですね！猫も一緒にごろごろ嬉しい気分です✨😺")
       # break
    elif "疲れた" in feeling or "だるい" in feeling or "眠い" in feeling or "つかれた" in feeling or "ねむい" in feeling:
        print("少し疲れてるみたいですね。猫がそっと寄り添いながら『にゃーん』と癒やしてくれます🍵😽")
      #  break
    elif "しんどい" in feeling or "辛い" in feeling or "悲しい" in feeling or "つらい" in feeling or "かなしい" in feeling or "寂しい" in feeling or "さみしい" in feeling:
        print(feeling.strip() + "時ですね…。猫が膝の上でごろごろしながら『大丈夫だよ』と言っているようです🌙🐈")
     #   break
    elif "普通" in feeling or "まあまあ" in feeling or "特にな" in feeling or "ふつう" in feeling or "とくにな" in feeling or "とくに無" in feeling or "特に無" in feeling:
        print("普通の日も大切にゃん。猫はそばでのんびり見守っていますよ🐾")
    else:
        print("にゃ？それはどんな気分かにゃ？猫も気になってそばにいます🐾")


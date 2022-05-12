# 2022年5月現在
from cocapi import CocApi

################################################################
TOKEN = 'YOUR TOKEN'
TIMEOUT = 1
PLAYER = "PLAYER ID"

api = CocApi(TOKEN,TIMEOUT)
player = api.players(PLAYER)

TH_level = player['townHallLevel'] # タウンホールレベルをintで保持
BH_level = player['builderHallLevel'] # ビルダーホールレベルをintで保持
heroes = player['heroes'] # ヒーロー情報を辞書で保持

################################################################
# 関数定義
# ヒーローに関する情報(ヒーロー名、必要な拠点レベル)
# バーバリアンキング TH7
# アーチャークイーン TH9
# グランドウォーデン TH11
# ロイヤルチャンピオン TH13
# バトルマシン BH5
################################################################


# バーバリアンキング関数
def BarbarianKing(heroes, TH_level):
    level = 0
    max_level = 0
    # heroesからバーバリアンキングのレベルを取得
    for i in heroes:
        if i['name'] == 'Barbarian King':
            level = i['level']

    # THレベルごとに最大レベルを制御
    if TH_level <= 6:
        print('まだバーバリアンキングを建築できません。')
    else:
        if TH_level == 7:
            max_level = 5
        elif TH_level == 8:
            max_level = 10
        elif TH_level == 9:
            max_level = 30
        elif TH_level == 10:
            max_level = 40
        elif TH_level == 11:
            max_level = 50
        elif TH_level == 12:
            max_level = 65
        elif TH_level == 13:
            max_level = 75
        elif TH_level == 14:
            max_level = 80
        print('あなたのバーバリアンキングのレベルは%dで%dまで成長させられます。' % (level, max_level)) 
    # print(heroes, TH_level, level, max_level)
    return(level, max_level)

# アーチャークイーン関数
def ArcherQueen(heroes, TH_level):
    level = 0
    max_level = 0
    # heroesからアーチャークイーンのレベルを取得
    for i in heroes:
        if i['name'] == 'Archer Queen':
            level = i['level']

    # THレベルごとに最大レベルを制御
    if TH_level <= 8:
        print('まだアーチャークイーンを建築できません。')
    else:
        if TH_level == 9:
            max_level = 30
        elif TH_level == 10:
            max_level = 40
        elif TH_level == 11:
            max_level = 50
        elif TH_level == 12:
            max_level = 65
        elif TH_level == 13:
            max_level = 75
        elif TH_level == 14:
            max_level = 80
        print('あなたのアーチャークイーンのレベルは%dで%dまで成長させられます。' % (level, max_level)) 
    return(level, max_level)

# グランドウォーデン関数
def GrandWarden(heroes, TH_level):
    level = 0
    max_level = 0
    # heroesからグランドウォーデンのレベルを取得
    for i in heroes:
        if i['name'] == 'Grand Warden':
            level = i['level']

    # THレベルごとに最大レベルを制御
    if TH_level <= 10:
        print('まだグランドウォーデンを建築できません。')
    else:
        if TH_level == 11:
            max_level = 20
        elif TH_level == 12:
            max_level = 40
        elif TH_level == 13:
            max_level = 50
        elif TH_level == 14:
            max_level = 55
        print('あなたのグランドウォーデンのレベルは%dで%dまで成長させられます。' % (level, max_level)) 
    return(level, max_level)

# ロイヤルチャンピオン関数
def RoyalChampion(heroes, TH_level):
    level = 0
    max_level = 0
    # heroesからロイヤルチャンピオンのレベルを取得
    for i in heroes:
        if i['name'] == 'Royal Champion':
            level = i['level']

    # THレベルごとに最大レベルを制御
    if TH_level <= 12:
        print('まだロイヤルチャンピオンを建築できません。')
    else:
        if TH_level == 13:
            max_level = 25
        elif TH_level == 14:
            max_level = 30
        print('あなたのロイヤルチャンピオンのレベルは%dで%dまで成長させられます。' % (level, max_level)) 
    return(level, max_level)

# バトルマシン関数
def BattleMachine(heroes, BH_level):
    level = 0
    max_level = 0
    # heroesからバトルマシンのレベルを取得
    for i in heroes:
        if i['name'] == 'Battle Machine':
            level = i['level']

    # BHレベルごとに最大レベルを制御
    if BH_level <= 4:
        print('まだバトルマシンを建築できません。')
    else:
        if BH_level == 5:
            max_level = 5
        elif BH_level == 6:
            max_level = 10
        elif BH_level == 7:
            max_level = 20
        elif BH_level == 8:
            max_level = 25
        elif BH_level == 9:
            max_level = 30
        print('あなたのバトルマシンのレベルは%dで%dまで成長させられます。' % (level, max_level)) 
    return(level, max_level)

# THヒーロー開発進度計算関数
def TH_HeroesProgressRate():
    BK = BarbarianKing(heroes, TH_level)
    AQ = ArcherQueen(heroes, TH_level)
    GW = GrandWarden(heroes, TH_level)
    RC = RoyalChampion(heroes, TH_level)
    rate = (BK[0] + AQ[0] + GW[0] + RC[0]) / (BK[1] + AQ[1] + GW[1] + RC[1])
    print('THのヒーローの開発進度は', int(rate * 100), '%です')
    return 0

# BHヒーロー開発進度計算関数
def BH_HeroesProgressRate():
    BM = BattleMachine(heroes, BH_level)
    rate = BM[0] / BM[1]
    print('BHのヒーローの開発進度は', int(rate * 100), '%です')
    return 0


# 各関数確認用
# BarbarianKing(heroes, TH_level)
# ArcherQueen(heroes, TH_level)
# GrandWarden(heroes, TH_level)
# RoyalChampion(heroes, TH_level)
# BattleMachine(heroes, BH_level)

TH_HeroesProgressRate()
BH_HeroesProgressRate()

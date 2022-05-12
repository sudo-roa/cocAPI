# 2022年5月現在
from cocapi import CocApi

TOKEN = 'YOUR TOKEN'
TIMEOUT = 1
CLANS = "CLAN ID"
PLAYER = "PLAYER ID"

api = CocApi(TOKEN,TIMEOUT)
player = api.players(PLAYER)

################################################################
# 呪文情報（呪文名 解放されるTHレベル）
# Lightning Spell TH5
# Healing Spell TH6
# Rage Spell TH7
# Jump Spell TH9
# Freeze Spell TH9
# Clone Spell TH10
# Invisibility Spell TH11

# Poison Spell TH8
# Earthquake Spell TH8
# Haste Spell TH9
# Skeleton Spell TH9
# Bat Spell TH10
################################################################


TH_level = player['townHallLevel']
spells = player['spells']

# 呪文名称総当たり
# for i in range(len(spells)):
#     print(spells[i]['name'])


################################################################
# 各呪文の関数定義
# ライトニング
def LightningSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Lightning Spell':
            level = spells[i]['level']
    if TH_level <= 4:
        return(level, max_level)
    else:
        if TH_level >= 5 and TH_level <= 7:
            max_level = 4
        elif TH_level == 8:
            max_level = 5
        elif TH_level == 9:
            max_level = 6
        elif TH_level == 10:
            max_level = 7
        elif TH_level == 11:
            max_level = 8
        elif TH_level >= 12:
            max_level = 9
    print(level, max_level)
    return(level, max_level)

# ヒーリング
def HealingSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Healing Spell':
            level = spells[i]['level']
    if TH_level <= 5:
        return(level, max_level)
    else:
        if TH_level == 6:
            max_level = 3 
        elif TH_level == 7:
            max_level = 4
        elif TH_level == 8:
            max_level = 5
        elif TH_level == 9:
            max_level = 6
        elif TH_level >= 10 and TH_level <=12:
            max_level = 7
        elif TH_level == 13:
            max_level = 8
    print(level, max_level)
    return(level, max_level)

# レイジ
def RageSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Rage Spell':
            level = spells[i]['level']
    if TH_level <= 6:
        return(level, max_level)
    else:
        if TH_level == 7:
            max_level = 4
        elif TH_level >= 8 and TH_level <= 11:
            max_level = 5
        elif TH_level >= 12:
            max_level = 6
    print(level, max_level)
    return(level, max_level)

# ジャンプ
def JumpSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Jump Spell':
            level = spells[i]['level']
    if TH_level <= 8:
        return(level, max_level)
    else:
        if TH_level == 9:
            max_level = 2
        elif TH_level >= 10 and TH_level <=12:
            max_level = 3
        elif TH_level >= 13:
            max_level = 4
    print(level, max_level)
    return(level, max_level)

# フリーズ
def FreezeSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Freeze Spell':
            level = spells[i]['level']
    if TH_level <= 8:
        return(level, max_level)
    else:
        if TH_level == 9:
            max_level = 2
        elif TH_level == 10:
            max_level = 5
        elif TH_level == 11:
            max_level = 6
        elif TH_level >= 12:
            max_level = 7
    print(level, max_level)
    return(level, max_level)

# クローン
def CloneSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Clone Spell':
            level = spells[i]['level']
    if TH_level <= 9:
        return(level, max_level)
    else:
        if TH_level >= 10:
            max_level = 3
        elif TH_level >= 11 and TH_level <= 12:
            max_level = 5
        elif TH_level == 13:
            max_level = 6
        elif TH_level == 14:
            max_level = 7
    print(level, max_level)
    return(level, max_level)

# インビジブル
def InvisibilitySpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Invisibility Spell':
            level = spells[i]['level']
    if TH_level <= 10:
        return(level, max_level)
    else:
        if TH_level == 11:
            max_level = 2
        elif TH_level == 12:
            max_level = 3
        elif TH_level >= 13:
            max_level = 4
    print(level, max_level)
    return(level, max_level)

# ポイズン
def PoisonSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Poison Spell':
            level = spells[i]['level']
    if TH_level <= 7:
        return(level, max_level)
    else:
        if TH_level == 8:
            max_level = 2
        elif TH_level == 9:
            max_level = 3
        elif TH_level == 10:
            max_level = 4
        elif TH_level == 11:
            max_level = 5
        elif TH_level == 12:
            max_level = 6
        elif TH_level >= 13:
            max_level = 7
        elif TH_level >= 14:
            max_level = 8
    print(level, max_level)
    return(level, max_level)

# アースクエイク
def EarthquakeSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Earthquake Spell':
            level = spells[i]['level']
    if TH_level <= 7:
        return(level, max_level)
    else:
        if TH_level == 8:
            max_level = 2
        elif TH_level == 9:
            max_level = 3
        elif TH_level == 10:
            max_level = 4
        elif TH_level >= 11:
            max_level = 5
    print(level, max_level)
    return(level, max_level)

# ヘイスト
def HasteSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Haste Spell':
            level = spells[i]['level']
    if TH_level <= 8:
        return(level, max_level)
    else:
        if TH_level == 9:
            max_level = 2
        elif TH_level == 10:
            max_level = 4
        elif TH_level >= 11:
            max_level = 5
    print(level, max_level)
    return(level, max_level)

# スケルトン
def SkeletonSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Skeleton Spell':
            level = spells[i]['level']
    if TH_level <= 8:
        return(level, max_level)
    else:
        if TH_level == 9:
            max_level = 1
        elif TH_level == 10:
            max_level = 3
        elif TH_level >= 11:
            max_level = 4
        elif TH_level == 12:
            max_level = 6
        elif TH_level >= 13:
            max_level = 7
    print(level, max_level)
    return(level, max_level)

# コウモリ
def BatSpell(spells, TH_level):
    level = 0
    max_level = 0
    for i in range(len(spells)):
        if spells[i]['name'] == 'Bat Spell':
            level = spells[i]['level']
    if TH_level <= 9:
        return(level, max_level)
    else:
        if TH_level == 10:
            max_level = 3
        elif TH_level == 11:
            max_level = 4
        elif TH_level >= 12:
            max_level = 5
    print(level, max_level)
    return(level, max_level)


################################################################
# 開発進度確認関数
def  spellsProgressRate():
    LS = LightningSpell(spells, TH_level)
    HeS = HealingSpell(spells, TH_level)
    RS = RageSpell(spells, TH_level)
    JS = JumpSpell(spells, TH_level)
    FS = FreezeSpell(spells, TH_level)
    CS = CloneSpell(spells, TH_level)
    IS = InvisibilitySpell(spells, TH_level)
    PS = PoisonSpell(spells, TH_level)
    ES = EarthquakeSpell(spells, TH_level)
    HaS = HasteSpell(spells, TH_level)
    SS = SkeletonSpell(spells, TH_level)
    BS = BatSpell(spells, TH_level)
    rate = (LS[0] + HeS[0] + RS[0] + JS[0] + FS[0] + CS[0] + IS[0] + PS[0] + ES[0] + HaS[0] + SS[0] + BS[0]) / (LS[1] + HeS[1] + RS[1] + JS[1] + FS[1] + CS[1] + IS[1] + PS[1] + ES[1] + HaS[1] + SS[1] + BS[1])
    print('呪文の開発進度は', int(rate * 100), '%です')
    return 0

# 各関数確認用
# LightningSpell(spells, TH_level)
# HealingSpell(spells, TH_level)
# RageSpell(spells, TH_level)
# JumpSpell(spells, TH_level)
# FreezeSpell(spells, TH_level)
# CloneSpell(spells, TH_level)
# InvisibilitySpell(spells, TH_level)
# PoisonSpell(spells, TH_level)
# EarthquakeSpell(spells, TH_level)
# HasteSpell(spells, TH_level)
# SkeletonSpell(spells, TH_level)
# BatSpell(spells, TH_level)

spellsProgressRate()
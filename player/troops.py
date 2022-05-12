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
troops = player['troops'] # 部隊情報を辞書で保持

# ベビドラはhomeとbuilderBaseで分けないといけない
elixar_troops_dict =[
    {
        "ID": 1,
        "name": "Barbarian",
        "limit_level": [0,1,1,2,2,3,3,4,5,6,7,8,9,9,10],
        "japanese": "バーバリアン"},
    {
        "ID": 2,
        "name": "Archer",         
        "limit_level": [0,1,1,2,2,3,3,4,5,6,7,8,9,9,10],
        "japanese": "アーチャー"},
    {
        "ID": 3,
        "name": "Giant",          
        "limit_level": [0,1,1,1,2,2,3,4,5,6,7,8,9,10,10],
        "japanese": "ジャイアント"},
    {
        "ID": 4,
        "name": "Goblin",         
        "limit_level": [0,0,1,2,2,3,3,4,5,6,7,7,8,8,8],
        "japanese": "ゴブリン"},
    {
        "ID": 5,
        "name": "Wall Breaker",
        "limit_level": [0,0,0,1,2,2,3,4,5,5,6,7,8,9,10],
        "japanese": "ウォールブレイカー",},
    {
        "ID": 6,
        "name": "Balloon",  
        "limit_level": [0,0,0,0,2,2,3,4,5,6,6,7,8,9,10],
        "japanese": "エアバルーン"},
    {
        "ID": 7,
        "name": "Wizard",       
        "limit_level": [0,0,0,0,0,2,3,4,5,6,7,8,9,10,10],
        "japanese": "ウィザード"},
    {
        "ID": 8,
        "name": "Healer",         
        "limit_level": [0,0,0,0,0,0,1,2,3,4,4,5,5,6,7],
        "japanese": "ヒーラー"},
    {
        "ID": 9,
        "name": "Dragon",         
        "limit_level": [0,0,0,0,0,0,0,2,3,4,5,6,7,8,9],
        "japanese": "ドラゴン"},
    {
        "ID": 10,
        "name": "P.E.K.K.A",      
        "limit_level": [0,0,0,0,0,0,0,0,3,4,6,7,8,9,9],
        "japanese": "P.E.K.K.A"},
    {
        "ID": 11,
        "name": "Baby Dragon",    
        "limit_level": [0,0,0,0,0,0,0,0,0,2,4,5,6,7,8],
        "japanese": "ベビードラゴン"},
    {
        "ID": 12,
        "name": "Miner",          
        "limit_level": [0,0,0,0,0,0,0,0,0,0,3,5,6,7,8],
        "japanese": "ディガー"},
    {
        "ID": 13,
        "name": "Electro Dragon", 
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,2,3,4,5],
        "japanese": "ライトニングドラゴン"},
    {
        "ID": 14,
        "name": "Yeti",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,2,3,4],
        "japanese": "イエティ"},
    {
        "ID": 15,
        "name": "Dragon Rider",
       "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,2,3],
       "japanese": "ドラゴンライダー"}
]

dark_elixar_troops_dict =[
    {
        "ID": 1,
        "name": "Minion",
        "limit_level": [0,0,0,0,0,0,0,2,4,5,6,7,8,9,10],
        "japanese": "ガーゴイル"},
    {
        "ID": 2,
        "name": "Hog Rider",      
        "limit_level": [0,0,0,0,0,0,0,2,4,5,6,7,9,10,11],
        "japanese": "ホグライダー"},
    {
        "ID": 3,
        "name": "Valkyrie",     
        "limit_level": [0,0,0,0,0,0,0,0,2,4,5,6,7,8,9],
        "japanese": "バルキリー"},
    {
        "ID": 4,
        "name": "Golem",     
        "limit_level": [0,0,0,0,0,0,0,0,2,4,5,7,9,10,11],
        "japanese": "ゴーレム"},
    {
        "ID": 5,
        "name": "Witch",
        "limit_level": [0,0,0,0,0,0,0,0,0,2,3,4,5,5,5],
        "japanese": "ネクロマンサー"},
    {
        "ID": 6,
        "name": "Lava Hound",     
        "limit_level": [0,0,0,0,0,0,0,0,0,2,3,4,5,6,6],
        "japanese": "ラヴァハウンド"},
    {
        "ID": 7,
        "name": "Bowler",    
        "limit_level": [0,0,0,0,0,0,0,0,0,0,2,3,4,5,6],
        "japanese": "ボウラー"},
    {
        "ID": 8,
        "name": "Ice Golem",      
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,3,5,5,6],
        "japanese": "アイスゴーレム"},
    {
        "ID": 9,
        "name": "Headhunter",     
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,2,3,3],
        "japanese": "ストライカー"},
]

super_troops_dict =[
    {
        "ID": 1,
        "name": "Super Barbarian",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,8,9,9,10],
        "japanese": "スーパーバーバリアン"},
    {
        "ID": 2,
        "name": "Super Archer",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,8,9,9,10],
        "japanese": "スーパーアーチャー"    
    },
    {
        "ID": 3,
        "name": "Super Giant",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,9,10,10],
        "japanese": "スーパージャイアント"    
    },
    {
        "ID": 4,
        "name": "Sneaky Goblin",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,7,8,8,8],
        "japanese": "スニークゴブリン"    
    },
    {
        "ID": 5,
        "name": "Super Wall Breaker",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,7,8,9,10],
        "japanese": "スーパーウォールブレイカー"    
    },
    {
        "ID": 6,
        "name": "Rocket Balloon",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,8,9,10],
        "japanese": "ロケットバルーン"    
    },
    {
        "ID": 7,
        "name": "Super Wizard",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,9,10,10],
        "japanese": "スーパーウィザード"    
    },
    {
        "ID": 8,
        "name": "Super Dragon",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,7,8,9],
        "japanese": "スーパードラゴン"    
    },
    {
        "ID": 9,
        "name": "Inferno Dragon",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,6,7,8],
        "japanese": "インフェルノドラゴン"    
    },
    {
        "ID": 10,
        "name": "Super Minion",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,8,9,10],
        "japanese": "スーパーガーゴイル"    
    },
    {
        "ID": 11,
        "name": "Super Valkyrie",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,7,8,9],
        "japanese": "スーパーバルキリー"    
    },
    {
        "ID": 12,
        "name": "Super Witch",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,5,5,5],
        "japanese": "スーパーネクロマンサー"    
    },
    {
        "ID": 13,
        "name": "Ice Hound",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,5,6,6],
        "japanese": "アイスハウンド"    
    },
    {
        "ID": 14,
        "name": "Super Bowler",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,4,5,6],
        "japanese": "スーパーボウラー"    
    }
]

builderbase_troops_dict = [
    {
        "ID": 1,
        "name": "Raged Barbarian",
        "limit_level": [0,2,4,6,8,10,12,14,16,18],
        "japanese": "レイジバーバリアン"
    },
    {
        "ID": 2,
        "name": "Sneaky Archer",
        "limit_level": [0,2,4,6,8,10,12,14,16,18],
        "japanese": "スニークアーチャー"
    },
    {
        "ID": 3,
        "name": "Boxer Giant",
        "limit_level": [0,0,0,4,8,10,12,14,16,18],
        "japanese": "ボクサージャイアント"
    },
    {
        "ID": 4,
        "name": "Beta Minion",
        "limit_level": [0,0,0,4,8,10,12,14,16,18],
        "japanese": "ベータガーゴイル"
    },
    {
        "ID": 5,
        "name": "Bomber",
        "limit_level": [0,0,0,0,8,10,12,14,16,18],
        "japanese": "ボンバー"
    },
    {
        "ID": 6,
        "name": "Baby Dragon",
        "limit_level": [0,0,0,0,8,10,12,14,16,18],
        "japanese": "ベビードラゴン"
    },
    {
        "ID": 7,
        "name": "Cannon Cart",
        "limit_level": [0,0,0,0,0,10,12,14,16,18],
        "japanese": "移動砲台"
    },
    {
        "ID": 8,
        "name": "Night Witch",
        "limit_level": [0,0,0,0,0,0,12,14,16,18],
        "japanese": "ダークネクロ"
    },
    {
        "ID": 9,
        "name": "Drop Ship",
        "limit_level": [0,0,0,0,0,0,0,14,16,18],
        "japanese": "降下船"
    },
    {
        "ID": 10,
        "name": "Super P.E.K.K.A",
        "limit_level": [0,0,0,0,0,0,0,0,16,18],
        "japanese": "スーパーP.E.K.K.A"
    },
    {
        "ID": 11,
        "name":  "Hog Glider",
        "limit_level": [0,0,0,0,0,0,0,0,0,18],
        "japanese": "ホググライダー"
    }
]

siege_machines_dict = [
    {
        "ID": 1,
        "name": "Wall Wrecker",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4],
        "japanese": "ウォールバスター"
    },
    {
        "ID": 2,
        "name": "Battle Blimp",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4],
        "japanese": "突撃艦"
    },
    {
        "ID": 3,
        "name": "Stone Slammer",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4],
        "japanese": "ロックボマー"
    },
    {
        "ID": 4,
        "name": "Siege Barracks",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4],
        "japanese": "投下兵舎"
    },
    {
        "ID": 5,
        "name": "Log Launcher",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4],
        "japanese": "ウッドランチャー"
    },
    {
        "ID": 6,
        "name": "Flame Flinger",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
        "japanese": "フレイムシューター"
    }
]

pets_dict =[
    {
        "ID": 1,
        "name": "L.A.S.S.I",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10],
        "japanese": "L.A.S.S.I"
    },
    {
        "ID": 2,
        "name": "Electro Owl",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10],
        "japanese": "エレクトロオウル"
    },
    {
        "ID": 3,
        "name": "Mighty Yak",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10],
        "japanese": "ヤク"
    },
    {
        "ID": 4,
        "name": "Unicorn",
        "limit_level": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10],
        "japanese": "ユニコーン"
    }

]



# Elixar troops
def ElixarTroops(TH_level):
    limit_sum = 0
    level_sum = 0
    for i in range(len(troops)):
        temp1 = troops[i]
        if temp1['name'] == "Baby Dragon" and temp1['village'] == "builderBase":
            continue
        for j in range(len(elixar_troops_dict)):
            temp2 = elixar_troops_dict[j]
            if temp1['name'] == temp2['name']:
                limit = temp2['limit_level'][TH_level]
                level = temp1['level']
                if limit == 0:
                    print('%s: まだ使用できません' % (temp2['japanese']))
                else:
                    limit_sum += limit
                    level_sum += level                    
                    print('%s: 現在%dレベルで%dまで強化できます。' % (temp2['japanese'], level, limit))
    rate = level_sum / limit_sum
    print (int(rate*100), '% 強化できています。')            
    return 0

# dark Elixar troops
def DarkEixarTroops(TH_level):
    limit_sum = 0
    level_sum = 0
    for i in range(len(troops)):
        temp1 = troops[i]
        for j in range(len(dark_elixar_troops_dict)):
            temp2 = dark_elixar_troops_dict[j]
            if temp1['name'] == temp2['name']:
                limit = temp2['limit_level'][TH_level]
                level = temp1['level']
                if limit == 0:
                    print('%s: まだ使用できません' % (temp2['japanese']))
                else:
                    limit_sum += limit
                    level_sum += level                    
                    print('%s: 現在%dレベルで%dまで強化できます。' % (temp2['japanese'], level, limit))
    rate = level_sum / limit_sum
    print (int(rate*100), '% 強化できています。')            
    return 0

# Super troops
def SuperTroops(TH_level):
    if TH_level <= 10:
        print('まだスーパーユニットを自身で作成できません')
        return 0
    else:
        print('スーパーユニットつかえます。')
    return 0

# BuilderBase troops
def BuilderBaseTroops(BH_level):
    limit_sum = 0
    level_sum = 0
    for i in range(len(troops)):
        temp1 = troops[i]
        if temp1['name'] == "Baby Dragon" and temp1['village'] == "home":
            continue
        for j in range(len(builderbase_troops_dict)):
            temp2 = builderbase_troops_dict[j]
            if temp1['name'] == temp2['name']:
                limit = temp2['limit_level'][BH_level]
                level = temp1['level']
                if limit == 0:
                    print('%s: まだ使用できません' % (temp2['japanese']))
                else:
                    limit_sum += limit
                    level_sum += level                    
                    print('%s: 現在%dレベルで%dまで強化できます。' % (temp2['japanese'], level, limit))
    rate = level_sum / limit_sum
    print (int(rate*100), '% 強化できています。')  
    return 0

# Eiege Machines
def SiegeMachines(TH_level):
    if TH_level <= 10:
        print('まだ突破兵器を自身で作成できません')
        return 0
    else:
        print('突破兵器つかえます。')
    return 0

# Pets
def Pets(TH_level):
    if TH_level <= 10:
        print('まだペットを使用できません')
        return 0
    else:
        print('ペット使えます。')
    return 0

ElixarTroops(TH_level)
DarkEixarTroops(TH_level)
SuperTroops(TH_level)
BuilderBaseTroops(BH_level)
SiegeMachines(TH_level)
Pets(TH_level)
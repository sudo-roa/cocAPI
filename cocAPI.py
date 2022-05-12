from cocapi import CocApi
import json

################################################################
# トークン等情報
TOKEN = 'YOUR TOKEN'
TIMEOUT = 1
CLANS = "CLAN ID"
PLAYER = "PLAYER ID"

# apiを利用するための準備
api = CocApi(TOKEN,TIMEOUT)
clan = api.clan_tag(CLANS)
clan_member = api.clan_members(CLANS)
player = api.players(PLAYER)


################################################################
# 全情報検索用スクリプト
print(json.dumps(clan, indent=2, ensure_ascii=False)) # 所属クラン情報全検索
print(json.dumps(clan_member, indent=2, ensure_ascii=False)) # クラン所属メンバー情報
print(json.dumps(player, indent=2)) # プレイヤー情報全検索
################################################################

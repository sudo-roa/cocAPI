# cocAPI
cocAPIを使ったアプリケーションの開発

トークンはこちらから取得 -> https://developer.clashofclans.com/

## インストール

> pip install cocapi

## 導入

cocAPIを利用するために、CocApiのインポートおよびTOKENが必要

```python
from cocapi import CocApi

token = 'YOUR_API_TOKEN'
timeout=1 #requests timeout

api=CocApi(token,timeout)
```

## 参考
- [Clash of Clans API](https://developer.clashofclans.com/)
- [ tonybenoy / cocAPI](https://github.com/tonybenoy/cocapi)
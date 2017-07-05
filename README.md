# AppEngine用ネイキッドドメインリダイレクトサービス

Google App Engineでネイキッドドメインへアクセスがあった場合に `www.example.com` などのサブドメインにリダイレクトするための簡単なソースです。

## 設定方法

### dispatch.yamlの設定

リダイレクトさせるパスをdispatch.yamlに設定します。

```
dispatch:
  - url: "freegufo.com/*"
    service: naked
```

もし、稼働させるアプリケーションにdispatch.yamlが存在している場合には、この設定を追加して下さい。

### app.yamlの設定

リダイレクト先のURLは、 `app.yaml` の `DOMEIN` に設定して下さい。

```
env_variables:
  DOMAIN: 'https://www.freegufo.com'
```

ここで設定したドメインにリダイレクトします。
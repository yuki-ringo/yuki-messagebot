# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjYyOTIwNTYzNTY3NzU1Mjgw.XsDFQg.mBa4sh0OOoDvlRHI2LBBaqU-5-A'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログイン成功なのだわ')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'はーぜちゃん':
        await message.channel.send('はーい！')

    if message.content == 'アルバハ':
        await message.channel.send('勝利を信じて')

    if message.content == 'ヒヒ':
        await message.channel.send('そんなの幻想よ！')

    if message.content == 'みるみる':
        await message.channel.send('教祖様')

    if message.content == 'いじわるきつね':
        await message.channel.send('そーよ！そーよ！')

    if message.content == '今川ガール':
        await message.channel.send('ちゅっ')

    if message.content == 'ゆきりんご':
        await message.channel.send('天使様')

    if message.content == 'らむらむ':
        await message.channel.send('グラブル㊙情報　らむさんは真姫ちゃんが好き')

    if message.content == 'まさぼのばかぁ！':
        await message.channel.send('私のこと嫌いなの？')

    if message.content == 'まきらむ':
        await message.channel.send('良きよね！')

    if message.content == 'ていたそ団長':
        await message.channel.send('よしよしなのだわ！')

    if message.content == 'はいせ姫様':
        await message.channel.send('しーずーまーりーたーまーえー')

    if message.content == 'いけちゃん':
        await message.channel.send('意外と真面目なのよね！びっくり！')

    if message.content == 'シナモンロール':
        await message.channel.send('世界一おいしい食べ物よ！')

    if message.content == 'Cinnabon':
        await message.channel.send('welcome　to Cinnabon!!')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

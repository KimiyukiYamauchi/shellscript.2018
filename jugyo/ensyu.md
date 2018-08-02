- 8/3演習
	- ログを記録する
	- 記事の選択機能をつける
	- パスを書き換える
	- 前後の日記記事に移動できるようにする
	- 記事の属性を埋め込む
	- 体裁を整える
	- ナビゲーション機能を強化する
		- 最新記事のリスト
		- カテゴリを押したときのリスト
		- 検索機能
		- ページビューカウンタ
	- プレビュー機能

- 7/27演習
	- 記事の表示
	- ログを記録する
	- 記事の選択機能をつける
	- パスを書き換える
	- 前後の日記記事に移動できるようにする
	- 記事の属性を埋め込む
	- 体裁を整える

- 7/20演習
	- CGIシェルスクリプトの動作確認
		- 動作確認用CGIスクリプト作成
		- Apacheの設定
		- 動作確認
			- 端末
			- ブラウザ
	- 記事の表示
	- ログを記録する
	- 記事の選択機能をつける
	- パスを書き換える
	
- 7/13演習
	- ディレクトリを作る
	- ファイルを置く
	- 記事の新規作成スクリプト
	- 記事のコミットスクリプト
	- 記事をリモートに送るスクリプト
	- gitの活用
	- リンク切れをチェックするスクリプト
	- 大きな画像を縮小するスクリプト
		- sudo apt install imagemagick

- 7/6演習
	- sysstatをインストール
		- sudo apt install sysstat
		- sudo vi /etc/defalt/sysstat
			- false -> true
		- sudo service sysstat start
		- sar
	- ポートの開閉を確認する
		- sudo apt install nmap
		- sudo nmap -sT -P0 -p 1-65535 192.168.33.10
	- ファイアウォールの設定
	- コマンド
		- bash
		- awk
		- sed
		- Open usp Tukubai
			- sudo apt install unzip
			- sudo apt install make
			- wget --no-check-certificate https://github.com/\  
			usp-engineers-community/Open-usp-Tukubai/archive/master.zip
			- unzip master.zip
			- cd Open-usp-Tukubai-master/
			- sudo make install
			- sudo apt install python
			- self
		- tree
		- curl
		- nkf
	- Apache(Webサーバ)のインストール
		- sudo apt install apache2


- 6/29演習
	- personal_infomation.csvから男女それぞれの人数を表示する
	- personal_infomation.csvから男女それぞれの割合を表示する
	- personal_infomation.csvから住所の都道府県の多い上位の５件を表示する
	- ホームディレクトリ以下をアーカイブしてバックアップする

- 6/22演習
	- drink2.txtからBeerを削除、この時削除された行のみ表示。  
	行番号も表示

- 6/15演習
	- date、test([)
	- 夏休みまでの日数
	- 西暦年からうるう年かどうかを判定
	- 誕生日までの日数

- 6/8演習
	- find、wc、sort
	- ディレクトリ内のファイル数・ディレクトリ数を調べる(演習1)
	- 2つのディレクトリ内を比較し、どちらか片方だけに存在するファイルを表示する(演習2)
	- du、xargs
	- あるディレクトリの中で容量を食っているサブディレクトリを調べる(演習3)

- 5/25演習
	- ホームディレクトリの中にworkディレクトリを作成
	    - pwd
	    - cd /home/vagrant
	    - cd
	    - mkdir work
	    - cd work
    - dir1の中にdir2を作って、さらにその中にdir3を作成
    - file2をコピーして、file3を作成
    - file3をdir1に移動
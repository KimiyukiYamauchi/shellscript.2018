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
2012/07/14 m3-suzuki eclipseでpythonを使う人向けの補助ツール

指定フォルダ以下すべてのテンプレートファイルのテキストファイル・エンコードモードを
強制的にUTF-8にします。
詳しくは※1参照


■使用方法
eclipseTemplate2Utf8.bat を実行するだけでOK
もしパス構成が異なる場合はbat内を一度書き換える必要があります。
(.prefsファイルの場所と、templatesフォルダの場所を引数で指定する)

python .\src\eclipseTemplate2Utf8.py ..\..\..\gameroot\.settings\org.eclipse.core.resources.prefs ..\..\..\gameroot\templates

元のprefsファイルは、コンバート前にバックアップされます。
このbat実行後、eclipseを起動すればOKです。
(eclipse起動中なら、再起動すればOK)


※1
eclipseが初期オープン時にs-jisと判定してしまうケース向け。
(他人が記述したHTMLを開く際に、内容から判別されるとshift_jis扱いにされてしまい、
 いちいちUTF-8に設定しなおしているケース)
↑この設定を行うと、.settings\org.eclipse.core.resources.prefs 内に
 記載されるが、それを全部自動でやってしまうツールになります。


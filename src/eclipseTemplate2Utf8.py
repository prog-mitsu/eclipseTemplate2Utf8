#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#===============================================================================
#
# Created on 2012/07/13
# @author: m3-suzuki
# 
#
# note
# eclipseのプロジェクト管理下にある全てのテンプレートHTMLファイルのエンコーディングを
# 強制的にUTF-8化する
# (eclipseのorg.eclipse.core.resources.prefsファイルを書き換える)
#
#===============================================================================
'''
import os
import sys                  # モジュール属性 argv を取得するため
import textFileOpen
import shutil
import getDirFileNameList


#==================================================================
# TEST
#==================================================================

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 設定ファイルをバックアップする(別名でコピーしておく)
# param   設定ファイル名
# param   バックアップファイル名
# retval  none
# note    既にバックアップファイルが存在するときは何もしない
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def _backupFile( srcFileName, backupFileName ):
    # 書き換える前に、バックアップをとっておく(別名でコピーする)
    src = open( srcFileName,    "r" )
    
    if not os.path.isfile( backupFileName ):    # まだファイルがなかったら
        dst = open( backupFileName, "w" )
        shutil.copyfileobj( src, dst )
    
    
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# パスから末端のテンプレートフォルダ名だけ抽出する
# param   指定パス
# retval  テンプレートフォルダ名
# note    例 RD_proj\branch\ver-1.0.0\gameroot\templates から、「templates」だけ抽出
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def _getTemplateFolderName( templatePath ):
    findIndex    = templatePath.rindex( '\\' )
    templateName = templatePath[findIndex+1:]    # +1 -> 「\」一文字ぶんシフト
    
    return templateName
    
    
    
#==================================================================
# TEST & RUN
#==================================================================
EXT_STR   = '\\.html$'
if __name__ == '__main__':
    
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数
    if (argc != 3):   # 引数が足りない場合は、その旨を表示
        print 'Usage: # python %s settingFileName, templatePath' % argvs[0]
        quit()
    
    srcFileName    = argvs[1]                   # eclipse prefsファイル名
    templatePath   = argvs[2]                   # チェックするtemplatesパス名
    
    # パスから、末端のテンプレートフォルダ名だけ抽出する
    templateName = _getTemplateFolderName( templatePath )
    
    # 書き換える前に、バックアップをとっておく(別名でコピーする)
    backupFileName = srcFileName + '.bak'
    _backupFile( srcFileName, backupFileName )
    
    # テキストファイルを読み込む
    readBufferList = []
    readBufferList = textFileOpen.textFileOpen( srcFileName, readBufferList )
    
    # 書き込む情報を収集する
    writeBufferList = []
    for _str in readBufferList:
        if -1 == _str.find( templateName ):    # templateを含む行は書き込み対象から外す
            writeBufferList.append( _str )
    
    # 指定テンプレートパス以下のhtmlファイルをフルパスで列挙する(再帰)
    dirFileNameList = []
    dirFileNameList = getDirFileNameList.getDirFileNameList( templatePath, EXT_STR, dirFileNameList )
    
    # 列挙したテンプレートファイルを、出力形式に置き換える
    # 例 → encoding//templates/base/battleHistoryInformation.html=UTF-8\n
    for _fileName in dirFileNameList:
        _idx  = _fileName.rindex( templateName )
        _str  = _fileName[ _idx: ]
        _str  = _str.replace( '\\', '/' )
        _str  = 'encoding//' + _str + '=UTF-8\n'    # 出力形式に置き換え
        writeBufferList.append( _str )
    
    # ファイル出力
    f = open( srcFileName, 'w' ) # 書き込みモードで開く
    for _str in writeBufferList:
        print _str
        f.write( _str )
    f.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#===============================================================================
#
# Created on 2012/07/13
# @author: m3-suzuki
#
# テキストファイルを読み込む
#
# note
# Pythonでファイルを読み込むスマートなやり方
# http://tech.lampetty.net/tech/index.php/archives/418
#
#from __future__ import with_statement
# 
#with open('/tmp/test.txt') as f:
#    for line in f:
#        print line
# 
# http://www.python.jp/doc/release/library/stdtypes.html#bltin-file-objects
# Python 2.5 から with 文を使えばcloseメソッドを直接呼び出す必要はなくなりました。
# 
#===============================================================================
'''

from __future__ import with_statement # これは Python 2.6 では不要です

#==================================================================
# テキストファイルを読み込んでバッファに格納する
# param   ファイル名
# param   出力先のリスト(一行ずつの文字列リストになります)
# retval  
# note    closeは不要( withを抜けたら勝手に閉じる )
#
#==================================================================
def textFileOpen( fileName, dstList ):
    with open( fileName ) as f:
        for line in f:
            dstList.append( line )
    
    return dstList



#==================================================================
# TEST
#==================================================================

if __name__ == '__main__':
    FILE_NAME = 'C:\\Users\\m3-suzuki\\Dropbox\\prog\\my_script\\python\\data\\org.eclipse.core.resources.prefs'
    
    readBufferList = []
    
    # テキストファイルを読み込んでバッファリストに出力
    readBufferList = textFileOpen( FILE_NAME, readBufferList )
    
    # 読み込んだテキストを一行ずつ表示
    for _str in readBufferList:
        print _str
    
    
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#===============================================================================
#
# Created on 2012/07/13
# @author: m3-suzuki
#
# 指定パス以下の、指定拡張子のファイルをフルパスで列挙する(再帰する)
# 
# note
# Python で os.walk 関数を使ってディレクトリを再帰的に操作してみる - 集中力なら売り切れたよ : 
# http://d.hatena.ne.jp/r_ikeda/20111122/pythonoswork
# 
#===============================================================================
'''
import os
import re

#==================================================================
# 指定パス以下の、指定拡張子のファイルをフルパスで列挙する(再帰する)
# param   指定パス
# param   拡張子名指定(正規表現で指定)
# param   出力先のリスト(マッチしたファイル名がフルパスで格納されます)
# retval  
# note    拡張子指定例 '\\.html$'
#
#==================================================================
def getDirFileNameList( path, extStr, dstList ):
    for root, dirs, files in os.walk( path ):
        for f in files:
            f = unicode(f, 'cp932')
            if not re.search( extStr, f ):
                continue
            
            fullpath = os.path.join( root, f )
            dstList.append( fullpath )
    
    return dstList



#==================================================================
# TEST
#==================================================================

if __name__ == '__main__':
    PATH_STR  = 'C:\\work\\RD_proj\\branch\\ver-1.0.0\\gameroot\\templates\\'
    EXT_STR   = '\\.html$'
    
    readBufferList = []
    readBufferList = getDirFileNameList( PATH_STR, EXT_STR, readBufferList )
    
    # 読み込んだテキストを一行ずつ表示
    for _str in readBufferList:
        print _str
    
    
    
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from xbmcswift import Plugin, download_page, xbmc, xbmcgui
from xbmcswift.ext.playlist import playlist


PLUGIN_NAME = 'GermanTV'
PLUGIN_ID = 'plugin.video.XBMC-Television'


plugin = Plugin(PLUGIN_NAME, PLUGIN_ID, __file__)
plugin.register_module(playlist, url_prefix='/_playlist')


@plugin.route('/', default=True)
def show_homepage():
    items = [
        # ARD
        {'label': 'ARD',
         'url': plugin.url_for('ard')},
        # ZDF
        {'label': 'ZDF',
         'url': plugin.url_for('zdf')},
        # RTL
        {'label': 'RTL',
         'url': plugin.url_for('rtl')},
        # SAT1
        {'label': 'SAT1',
         'url': plugin.url_for('sat1')},                  
        # PRO7
        {'label': 'PRO7',
         'url': plugin.url_for('pro7')},                           
        # RTL2
        {'label': 'RTL2',
         'url': plugin.url_for('rtl2')},
        # VOX
        {'label': 'VOX',
         'url': plugin.url_for('vox')},
        # 
        {'label': 'Super RTL',
         'url': plugin.url_for('superrtl')},
        # 3sat
        {'label': '3Sat',
         'url': plugin.url_for('3sat')},                  
        # ARTE
        {'label': 'ARTE',
         'url': plugin.url_for('arte')},                  
        # VIVA
        {'label': 'VIVA',
         'url': plugin.url_for('viva')}
    ]
    return plugin.add_items(items)


@plugin.route('/ard/')
def ard():
    url = 'http://webtv-aarh-9.stofa.dk:80/179_01.m3u8'
    li = xbmcgui.ListItem('ARD')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/zdf/')
def zdf():
    url = 'http://webtv-aarh-9.stofa.dk:80/184_01.m3u8'
    li = xbmcgui.ListItem('ZDF')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/rtl/')
def rtl():
    url = 'http://webtv-aarh-8.stofa.dk:80/187_01.m3u8'
    li = xbmcgui.ListItem('RTL')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/sat1/')
def sat1():
    url = 'http://webtv-aarh-8.stofa.dk:80/193_01.m3u8'
    li = xbmcgui.ListItem('SAT1')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/pro7/')
def pro7():
    url = 'http://webtv-aarh-8.stofa.dk:80/193_01.m3u8'
    li = xbmcgui.ListItem('PRO7')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/rtl2/')
def rtl2():
    url = 'http://webtv-aarh-8.stofa.dk:80/188_01.m3u8'
    li = xbmcgui.ListItem('RTL2')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []                

@plugin.route('/vox/')
def vox():
    url = 'http://webtv-aarh-8.stofa.dk:80/190_01.m3u8'
    li = xbmcgui.ListItem('VOX')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/super rtl/')
def superrtl():
    url = 'http://webtv-aarh-9.stofa.dk:80/189_01.m3u8'
    li = xbmcgui.ListItem('Super RTL')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/3sat/')
def 3sat():
    url = 'http://webtv-aarh-8.stofa.dk:80/182_01.m3u8'
    li = xbmcgui.ListItem('3Sat')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/arte/')
def arte():
    url = 'http://webtv-aarh-8.stofa.dk:80/180_01.m3u'
    li = xbmcgui.ListItem('ARTE')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

@plugin.route('/viva/')
def viva():
    url = 'http://webtv-aarh-9.stofa.dk:80/195_01.m3u8'
    li = xbmcgui.ListItem('VIVA')
    xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, li)
    return []

if __name__ == '__main__':
    plugin.run()
    

# -*- coding: utf-8 -*-

from module.plugins.internal.DeadHoster import DeadHoster, create_getInfo


class MegavideoCom(DeadHoster):
    __name__    = "MegavideoCom"
    __type__    = "hoster"
    __version__ = "0.24"
    __status__  = "stable"

    __pattern__ = r'http://(?:www\.)?megavideo\.com/\?.*&?(d|v)=\w+'
    __config__  = []  #@TODO: Remove in 0.4.10

    __description__ = """Megavideo.com hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("jeix", "jeix@hasnomail.de"),
                       ("mkaay", "mkaay@mkaay.de")]


getInfo = create_getInfo(MegavideoCom)

# coding: UTF-8
from __future__ import print_function

import re
import random

choice = random.choice


"""
26 12 99         added support for 'article' in tags:
            'this_demonstrates_articles':    ['<#article, demo_fruit#>'],
            'demo_fruit':    ['pear', 'apple', 'olive']
            #a pear
            #an apple
            #a pear
            #an olive

30 12 99         fixed replacecode - now it will interpret identical tags in one line individually

4 jan 99        added support for inline style references
            <#!bold, company#>    will label this for bold, it depends on the styledict
                                how it is formatted in the end
            <#!bold, !uppercase, company#> - multiple styles should be possible as well, no?
            in theory yes, but somehow netscape doesn't draw the uppercase - odd?
            - tag = name of an entry from the Content module
            - formatdict is a dictionary in which style
                commands that are used in Content are mapped
                to any arbitrary outside defined stylename.
                This is to prevent pollution from outside formatting stuff
                in the content module.
                For instance, a content tag can say <#!bold, company#>
                the formatdict can look like this: {'bold':    'CSS_my_specific_bold'}
                If the style cmd from the tag can be found in the provided formatdict
                format func is used to format the final resulting text. 
                    def formatfunc(text, tagname)
                This means that Writer and Content should also be able to be used
                to make RTF, or any other kind of formatted text without making
                the modules specific to any kind of format, or platform.


3.0            added support for the Content package, added some UI
17 1 2000    

3.1            Writer can now handle nested tags, opening a whole world of metaprogramming
evb    

3.2            messed with the caching mechanism
evb

3.3            now the write() method also accepts tagged entries, simpler code, more flexible
evb            w.write('<#name#>') and w.write('name') have the same results
    
3.4            added simpler support for initial capitals. Write '<#^,word#> for a capital of the first letter
evb

4.0             Removed string module import. Added some tests.
"""

__version__ = '4.0'

opentag = u'<#'
closetag = u'#>'

DEBUG = 0

# filter tabs, newline, returns, double spaces, but leave single spaces.
FILTERWHITESPACE = 1

randint = random.randint
vowels = u'aeiuoAEIUO'

class BlurbWriter(object):

    '''A very unspecific recursive compiler and randomizer for text.
    '''

    def __init__(self, content, debug=False):
        self.DEBUG = debug
        self.data = {}
        self._cache = {}
        self.formatdict = None
        self.formatfunc = None
        self.lasttag = 'no last tag'    # last processed tag, useful when debugging loops
        self.choicetree = []
        p = '\<#(?P<tagname>.*)#\>'
        #p = '\<#(?P<tagname>.*?)#\>'
        self.tag = re.compile(p, re.IGNORECASE)
        p = '\<-(?P<tagname>.*?)-\>'
        self.pstatement = re.compile(p, re.IGNORECASE)
        self.allkeys = self.keys()

        self.importcontent(content)
    
    def importcontent(self, contentdict):
        self.data.update(contentdict)
        dk = self.data.keys()
        dk.sort()
        self.keywords = dk
    
    def keyindex(self, key):
        if key in self.allkeys:
            return self.allkeys.index(key)
        else:
            return -1
        
    def keys(self):
        k = self.data.keys()
        k.sort()
        return self.data.keys()

    def has_key(self, key):
        if self._cache.has_key(key):
            return 1
        if self.data.has_key(key):
            return 1
        return 0
    
    def alternatives(self, key):
        return self[key]
        
    def choice(self, cached, key):
        if self.has_key(cached):
            return 1, self[cached][0]
        items = self[key]
        if len(items)>0:
            i = randint(0, len(items)-1)
            self.choicetree.append((self.keyindex(key), i))
            return i, items[i]
        else:
            self.choicetree.append((-1, -1))
            return -1, ''

    def getvalue(self, key):
        return self[key]
        
    def __getitem__(self, key):
        if self._cache.has_key(key):
            return self._cache[key]
        if self.data.has_key(key):
            return self.data[key]
        return u'__' + key + '__'
        
    def define(self, key, value):
        if DEBUG:
            print('hard define', key, value)
        self._cache[key] = [value]
        
    def softdefine(self, key, value):
        if DEBUG:
            print('soft define', key, value)
        if not self._cache.has_key(key):
            self._cache[key] = [value]
        
    def clearcache(self, key=None):
        if not key:
            self._cache = {}
        else:
            if self._cache.has_key(key):
                del self._cache[key]
        
    def parsetag(self, tag):
        hard=0
        # check for styles
        parts = tag.split(',')
        if len(parts)>1:
            name = parts[-1].strip()
            cmd = parts[0:-1]
            variable = None
            return name, cmd, variable, hard
        # check for hard definition
        parts = tag.split('=')
        if len(parts)>1:
            hard = 1
            name = parts[-1].strip()
            cmd = []
            variable = u"".join(parts[0:-1])
            return name, cmd, variable, hard
        # check for soft definition
        parts = tag.split(':')
        if len(parts)>1:
            hard=0
            name = parts[-1].strip()
            cmd = []
            variable = u''.join(parts[0:-1])
            return name, cmd, variable, hard
        # rest
        else:
            hard=0
            name = tag
            cmd = []
            variable = None
            return name, cmd, variable, hard
    
    def write(self, tag, formatdict=None, formatfunc=None):
        '''this assumes tag to be a direct entry in content'''
        return self.writetag(opentag+tag+closetag,formatdict ,formatfunc)
        
    def writetag(self, tag, formatdict=None, formatfunc=None):
        '''this will evaluate tag directly, use writetag if you want to more tags in one line to be processed.
        this is the main interface to the writer class'''
        self.allkeys = self.keys()
        self.choicetree = []
        if not formatdict:
            self.formatdict = {}
        else:
            self.formatdict = formatdict
        self.formatfunc = formatfunc
        _, item = self.replacetag(0, tag) # ok, item
        _, item = self.replacecode(item) # ok, item
        if FILTERWHITESPACE:
            return ' '.join(item.split())
        return item
    
    def replacecode(self, text):
        m = 1
        pend= 0
        while m != None:
            m = self.pstatement.search(text, pend)
            if m == None:
                return 0, text
            tag = m.group('tagname')
            if len(tag) == 0:
                raise 'Error in blurb code' # Better make it crash to show the error
                return 0, '__empty tag__'
            try:
                result = eval(tag)
            except:
                result = '__error('+tag+')__'
            if not isinstance(result, basestring):
                result = str(result)
            parts = text.split('<-' + tag + '->')
            text = parts[0] + result + ('<-' + tag + '->').join(parts[1:])
        return 1, text
        
    def capsentence(self, s):
        ss = s.split('. ')
        new = [] 
        for i in ss:
            new.append(i[0].upper() + i[1:])
        return new.join('. ')
    
    def nextopen(self, pos, text):
        return text.find(opentag, pos)
        
    def nextclosed(self, pos, text):
        return text.find(closetag, pos)
    
    def nexttag(self, pos, text):
        start = self.nextopen(pos, text)
        stop = self.nextclosed(pos, text)
        if start == -1:
            if stop == -1:
                return -1, -1
            return 0, stop
        if start < stop and start != -1:
            return 1, start
        else:
            return 0, stop
                    
    def findtag(self, text):
        p = -1
        last = None,None
        while 1:
            kind, p = self.nexttag(p+1, text)
            if last[0]==1 and kind==0:
                if self.DEBUG:
                    print(text[last[1]+len(opentag): p])
                return last[1]+len(opentag), p
            if (kind, p) == (-1, -1):
                break
            last=kind, p
        return None, None
        
    def replacetag(self, level, text):
        level = level + 1
        if level > 100:
            raise 'recursion error? too many nested instructions!', self.lasttag
        #pend = 0
        m = 1
        while m != None:
            start, stop = self.findtag(text)
            if start == None:
                return 0, text
            tag = text[start:stop]
            if len(tag) == 0:
                raise 'Error in blurb code' # Better make it crash to show the error
                return 0, '__empty tag__'

            # do the meta-recursive tag-tagging thing here
            metatext = text
            metatag = tag
            while tag.find(opentag) != -1:
                _, metatag = self.replacetag(level, tag) # ok, metalog
                parts = metatext.split(tag)
                if len(parts) > 1:
                    tag = parts.join(metatag)
                else:
                    tag = metatag
                return self.replacetag(level, tag)
                
            tagname, cmd, variable, hard = self.parsetag(tag)
            # process in-tag commands, if any
            cachethis = 0    # whether results should be cached
            setarticle = 0    # prepare an article ( 'a' or 'an' )
            uppered = 0    # make first character uppercase
            formatcmds = []
            for i in cmd:
                si = i.strip()
                if not si:
                    continue
                if si=='article':
                    setarticle = 1
                elif si[0] == '!':        # it's a format command!
                    formatcmds.append(si[1:])
                elif si[0] == '^':        # make first character uppercase
                    uppered = 1

            parts = text.split(opentag + tag + closetag)
            if self.has_key(tagname):
                _, selection = self.choice(variable, tagname) # ci, selection
                _, c = self.replacetag(level, selection) # ok, c
            else:
                _, c = self.replacetag(level, '__' + tagname + '__') # ok, c 
            self.lasttag = c

            # take care of the article command
            art = ''
            if setarticle:
                if c[0] in vowels:
                    art = 'an '
                else:
                    art = 'a '
            if uppered and c:
                c = c[0].upper()+c[1:]

            # format the line if necessary
            if len(formatcmds) > 0 and self.formatfunc:
                for fc in formatcmds:
                    if DEBUG:
                        print('writerformatting before:', fc, c)
                    if not self.formatdict.has_key(fc):
                        continue
                    c = self.formatfunc(c, self.formatdict[fc])
                    if DEBUG:
                        print('writerformatting after:', fc, c)

            # build the new line
            vardef = c
            if variable:
                c = ''
            try:
                text = parts[0] + art + c + (opentag + tag + closetag).join(parts[1:])
            except:
                print('Hm, a problem occurred. Nested quite deep, I think should just stop. Sorry!')
                return 0, text
            # store the result in the cache
            # note: it is storing the stylised version
            if variable or cachethis:
                if variable:
                    tg = variable
                else:
                    tg = tagname
                if hard:
                    self.define(tg, vardef)
                else:
                    self.softdefine(tg, vardef)
        return 0, text

# maybe time to write some tests
if __name__ == "__main__":

    def test():
        u"""
        >>> # replace a single tag
        >>> content = { 'pattern1': ['a']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern1')
        u'a'
        
        >>> # replace a tag
        >>> content = { 'pattern2': ['a'], 'pattern1': ['<#pattern2#>']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern2')
        u'a'
        >>> bw.write('pattern1')
        u'a'

        >>> # prefix an / a article for a result based on consonant / vowel
        >>> content = { 'pattern2': ['a'], 'pattern1': ['<#article, pattern2#>'],  'pattern4': ['b'], 'pattern3': ['<#article, pattern4#>']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern1')
        u'an a'
        >>> bw.write('pattern3')
        u'a b'

        >>> # replace a nested tag
        >>> content = { 'pattern2': ['pattern'], 'pattern1': ['<#<#pattern2#>3#>'], 'pattern3': ['b']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern1')
        u'b'

        >>> # capitalisation of first character
        >>> content = { 'pattern1': ['<#^,pattern2#>'], 'pattern2': [u'aa aa']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern1')
        u'Aa aa'

        >>> # unicode content
        >>> content = { 'pattern1': [u'üößé']}
        >>> bw = BlurbWriter(content)
        >>> bw.write('pattern1')
        u'\\xfc\\xf6\\xdf\\xe9'
        # not sure if that is the right way

        >>> # replace a tag
        >>> content = { 'pattern2': ['a'], 'pattern1': ['<#pattern2#>']}
        >>> bw = BlurbWriter(content, debug=True)
        >>> bw.write('pattern2')
        pattern2
        u'a'
        >>> bw.write('pattern1')
        pattern1
        pattern2
        u'a'
        """

    def _test():
        import doctest
        doctest.testmod()

    _test()

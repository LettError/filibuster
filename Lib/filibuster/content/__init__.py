# -*- coding: UTF-8 -*-
#
"""
        history
        This is the init code for the Content package.
        No user servicable parts inside.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
3.0.0    - split all the content into babycontents
evb        - note: only one dictionary named 'contexnt' allowed per module
        this limitation is to speed up loading
4.0    - changes due to the fact that Content is now a submodule of the
        new ContentWriter package. (jvr)
4.0     2016 public release
"""

__version__ = '4.0'



import glob
import os, string
import importlib
#import filibuster

contentPath = os.path.dirname(__file__) #@NoEffect
print('contentPath', contentPath)


DEBUG=1

_contentCache = None


def clearCache():
    global _contentCache
    _contentCache = None


def old_content():
    """Return one dictionary that contains all dictionaries of the
    module. By making a function rather than part of the namespace,
    the content can be updated dynamically. Should not make any
    difference in speed for normal use."""
    
    global _contentCache
    
    if _contentCache is not None:
        return _contentCache
    
    # import each time by looking at the files
    mods = glob.glob1(contentPath, '*.py')
    print(mods)
    _contentCache = content = {}
    
    for m in mods:
        if m[:2] == '__':
            continue
        modname = __name__ + '.' + m[:-3]
        path = 'filibuster.content.' + modname.split('.')[1]
        print("aa modname", modname)
        print('aa path', path)
        module = importlib.import_module(path)
        # find the deepest submodule
        for modname in path[1:]:
            module = getattr(module, modname)
        if hasattr(module, 'content'):
            content.update(module.content)
            continue
        else:
            if DEBUG:
                print(__name__, 'submodule ', module, 'misses a content dictionary.')
    return content


def index(tagname):
    """Return the name of the submodule that tagname is defined in,
    as well as a list of modules and keys in which this tagname is used."""
    mods = glob.glob1(contentPath[0], '*.py')
    keys = []
    usedin = {}
    
    for m in mods:
        if m[:2] == '__':
            continue
        modname = __name__ + '.' + m[:-3]
        path = string.split(modname, '.')
        module = importlib.import_module(modname)
        # find the deepest submodule
        for modname in path[1:]:
            module = getattr(module, modname)
        if hasattr(module, 'content'):
            c = module.content
            for k in c.keys():
                if k == tagname:
                    keys.append(m)
                for item in c[k]:
                    if string.find(item, tagname) !=  -1:
                        usedin[(m, k)] = 1
    return keys, usedin.keys()


def filibusterContent():
    """Return one dictionary that contains all dictionaries of the
    module. By making a function rather than part of the namespace,
    the content can be updated dynamically. Should not make any
    difference in speed for normal use."""
    import filibuster
    print('filibuster', filibuster.__file__)
    
    global _contentCache
    
    if _contentCache:
        return _contentCache
    
    # import each time by looking at the files
    print('assuming contentPath', contentPath)
    mods = glob.glob1(contentPath, '*.py')
    #print(mods)
    _contentCache = content = {}
    for name in mods:
        n = name[:-3]
        #print('name', name[:-3])
        #print('filibuster', filibuster)
        fullModulePath = 'filibuster.content.%s' % (n)
        module = None
        try:
            module = importlib.import_module(fullModulePath)
        except ImportError:
            print('failed to load module', n)
            continue
        if hasattr(module, 'content'):
            for k, v in module.content.items():
                content[k] = v
            #if not n in content:
            #    content[n] = {}
            #for k, v in module.content.items():
            #   content[n][k] = v
    _contentCache = content
    return content


if __name__ == "__main__":
    import filibuster
    #m = importlib.import_module('filibuster')
    #m = importlib.import_module('filibuster.content')
    #m = importlib.import_module('legal', filibuster)
    #print('xx', m)
    print(filibusterContent())
    




import os, sys
import xpub as imp_xpub
import DefinedAssets

class SimplePublisher:
    def publishStyleframes(self, publishPath, passInfo={}):
        '''
        publish styleframes
        '''





import DefinedAssets
da = DefinedAssets.DefinedAssets('testing', '_default')

#print da.assets()
print da.getAsset('styleframes')
#styleframes image dir dir images/ltm "Directory of style frames"



'''



import DefinedAssets

da = DefinedAssets.DefinedAssets('tinman', 'TM101_012_030')

print da.getAsset('CAM_chan')

DefinedAssets.asset()

asset_name = da.assets()

asset_name.setAll('CAM_chan',
                  'camera_chan',
                  'chan',
                  'houdini/chan',
                  "Chan define to go with maya camera")

da.makeDefine(asset_name)

# Publish distortion.
xpub.publish(show_name,
             shot_name,
             'define',
             'pathToDefine',
             1,
             quiet=True,
             comment_file="Quietly published from 3DE"
                          "by %s" % os.getenv("USERNAME"))





print xpub.publish.__doc__

Publish an asset.

params:
        show            - (string) short show name
        shot            - (string) shot name
        asset_name      - (string) define name
        publish         - (string) path to publish
        do_copy         - (int)  operation type - 0 (move), 1 (copy), 2 (symlink)
        quiet           - (bool) verbose or not
        comment_file    - (string) comment or a path to text file containing comment
        force_version   - (int) force to supplied version
        proxy           - (bool) generate proxies for seq publish
        deps            - (string/id list) list of items to link as dependencies
        parents         - (string/id list) list of items to link as parents
        suppress_mail   - (bool) set to not send notification mail
        category        - (string) category of define to use for auto-define creation

returns:
        id              - (int) unique id of new publish



styleframes image dir dir images/ltm "Directory of style frames"
'addDefine', 
'assets', 
'collections',
 'findAssets', 
 'get', 
 'getAsset',
  'getAssetByCollection',
   'getAssetByPath', 
   'getCollection', 
   'getLastVersion', 
   'getLastVersionFS', 
   'getPublishDirectory', 
   'getPublishFile', 
   'getPublishMasterFile', 
   'initByPath', 
   'isDefined', 
   'pad3Ver', 
   'removeDefine', 
   'shot', 
   'show', 
   'updateDefine', 
   'validateCollection', 
'writeDefineFile'

'''
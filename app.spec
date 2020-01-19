# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['microstatistics\\app.py'],
             pathex=['C:\\yp\\microstatistics'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.neighbors.typedefs', 'sklearn.utils._cython_blas', 'sklearn.neighbors.quad_tree', 'sklearn.tree', 'sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='microstatistics',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='microstatistics\\gui\\img\\micro.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')

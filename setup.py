import setuptools

setuptools.setup(name='memobird',
                 version='1.0',
                 packages=['memobird',
                           'memobird.libs',
                           'memobird.apps'],
                 install_requires=['requests==2.31.0',
                                   # 'Pillow==3.2.0', # enable when image printing is needed
                                  ],
                 scripts=['memobird/apps/mb-qod',
                          'memobird/apps/mb-umbrella'],
)
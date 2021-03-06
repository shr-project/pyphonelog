# -*- coding: utf-8 -*-
from distutils.core import setup
import glob
    
setup(name='pyphonelog',
        version='0.17.0',
	description='A phonelog gui that connects to the shr daemon/a custom daemon',
        author='Tom Hacohen',
        author_email='tom@stosb.com',
        url='http://wiki.openmoko.org/wiki/PyPhonelog',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: X11 Applications',
            'Intended Audience :: End Users/Phone UI',
            'License :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: System',
            ],
	scripts = ['src/phonelog'],
	data_files= [
		('applications', ['data/applications/phonelog.desktop']),
		('pixmaps', ['data/pixmaps/phonelog.png']),
		('locale/de/LC_MESSAGES', ['data/po/de/phonelog.mo']),
                ('locale/fr/LC_MESSAGES', ['data/po/fr/phonelog.mo']),
                ('locale/es/LC_MESSAGES', ['data/po/es/phonelog.mo']),
                ('locale/gl/LC_MESSAGES', ['data/po/gl/phonelog.mo']),
                ('locale/eo/LC_MESSAGES', ['data/po/eo/phonelog.mo']),
                ('locale/sv/LC_MESSAGES', ['data/po/sv/phonelog.mo']),
		('phonelog/skeleton', ['data/config/phonelog.conf']),
		('phonelog/icons', ['data/pixmaps/ui/missed.png',\
				    'data/pixmaps/ui/received.png',\
				    'data/pixmaps/ui/made.png',\
				    'data/pixmaps/ui/general.png'])
	]
        
     )

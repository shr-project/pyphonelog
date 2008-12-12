from distutils.core import setup
import glob
    
setup(name='pyphonelog',
        version='0.13.0',
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
        package_dir= {'phonelog':'./'},
        packages=['phonelog'],
        data_files=[('share/applications', ['data/applications/phonelog.desktop'])
                    ],
        scripts = ['src/phonelog']
     )

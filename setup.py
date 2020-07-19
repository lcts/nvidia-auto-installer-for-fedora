import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(name='nvautoinstall',
      version='0.4.0',
      description='Auto-installer for proprietary NVidia drivers on Fedora',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: Utilities',
      ],
      keywords='',
      url='https://github.com/t0xic0der/nvidia-auto-installer-for-fedora',
      author='Akashdeep Dhar',
      author_email='nobody@example.com',
      license='GPLv3',
      packages=setuptools.find_packages(),
      install_requires=[
          'click',
          'colorama',
          'distro',
      ],
      entry_points={
          'console_scripts': ['nvautoinstall=nvautoinstall:main'],
      },
      )

from setuptools import setup

# python setup.py sdist
# twine upload dist/*

setup(name='CrypticCreations',
      version='0.2.1',
      description='Create ciphers or random strings for DnD players to try and read aloud for the group.',
      url='https://github.com/ClutchTech/CrypticCreations',
      keywords='dnd ciphers random CrypticCreations',
      author='Clutch_Reboot',
      author_email='clutchshadow26@gmail.com',
      license='GNU General Public License v2.0',
      packages=['CrypticCreations'],
      zip_safe=False,
      long_description=open('README.md', 'rt').read(),
      long_description_content_type='text/markdown'
      )

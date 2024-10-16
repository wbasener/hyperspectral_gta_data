from distutils.core import setup
setup(
  name = 'hyperspectral_gta_data',         # How you named your package folder (MyLib)
  packages = ['hyperspectral_gta_data'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Module for downloading hyperspectral imagery and libraries',   # Give a short description about your library
  author = 'Bill Basener',                   # Type in your name
  author_email = 'wb8by@virginia.edu',      # Type in your E-Mail
  url = 'https://github.com/wbasener/hyperspectral_gta_data',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/wbasener/hyperspectral_gta_data/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['HYPERSPECTRAL', 'IMAGES', 'LIBRARIES'],   # Keywords that define your package best
  install_requires=[            
          'gdown',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)

# To build:
#  > python -m build
#  > python -m twine upload dist/*
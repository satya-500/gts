from setuptools import setup

setup(
  name='appscale-hermes',
  version='0.1.2',
  description='AppScale module which takes care of periodical backup and '
              'restore tasks and provides statistics API.',
  author='AppScale Systems, Inc.',
  url='https://github.com/AppScale/appscale',
  license='Apache License 2.0',
  keywords='appscale google-app-engine python',
  platforms='Posix',
  install_requires=[
    'appscale-common',
    'kazoo',
    'tornado',
    'psutil==5.6.3',
    'attrs>=18.1.0,<19.2.0',  # 19.2.0 removed "convert" attribute.
    'mock',
  ],
  test_suite='appscale.hermes',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2.7'
  ],
  namespace_packages=['appscale'],
  packages=['appscale',
            'appscale.hermes',
            'appscale.hermes.producers'],
  entry_points={'console_scripts': [
    'appscale-hermes=appscale.hermes.hermes_server:main'
  ]}
)

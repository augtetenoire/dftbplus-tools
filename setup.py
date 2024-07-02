from setuptools import setup

setup(name='dftbplus-tools',
      version='1.0',
      description='Package that contain tools for DFTB+ software',
      url='https://github.com/augtetenoire/dftbplus-tools',
      author='Auguste TETENOIRE',
      author_email='auguste.tetenoire.pro@gmail.com',
      license='CNRS',
      packages=['electron_dynamics', 'extra_tools', 'vibrational_modes'],
      zip_safe=False)

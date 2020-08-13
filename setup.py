from pathlib import Path
from setuptools import setup, find_packages
from setuptools.extension import Extension


def gen_long_description():
    with Path('./README.md').open(encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(name='rlogger',
      version='3.0',
      packages=find_packages(),
      description='An Python logger',
      long_description=gen_long_description(),
      long_description_content_type='text/markdown',
      url='',
      author='rivergold',
      author_email='jinghe.rivergold@gmail.com',
      license='MIT',
      zip_safe=False)

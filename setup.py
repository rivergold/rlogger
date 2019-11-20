from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(name='rlogger',
      version='1.0',
      platforms=['any'],
      packages=find_packages(),
      description='An Python logger',
      url='',
      author='rivergold',
      author_email='rivergold@qiyi.com',
      license='MIT',
      zip_safe=False)

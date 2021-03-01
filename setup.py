from setuptools import setup, find_packages

setup(name='personal-finance',
      description='A personal finance helper',
      long_description='This is just a education loan service profiler',
      packages=find_packages(exclude=["*tests*"]),
      version='1.0.0',
      install_requires=[
          'fastapi',
          'uvicorn[standard]',
          'sqlalchemy'
      ],
      extras_require={
          'dev': [
             
          ],
      }
      ) 

from setuptools import setup, find_packages
import sortable

setup(name='twentytab-sortable',
      version=sortable.__version__,
      description='A django model and admin to create sortable items in django admin with jqueryui sortable method',
      author='20tab S.r.l.',
      author_email='info@20tab.com',
      url='https://github.com/20tab/twentytab-sortable',
      license='MIT License',
      install_requires=[
          'Django >=1.6',
          'django-appconf>=0.6',
      ],
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
      }
)

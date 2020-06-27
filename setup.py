from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='django-admin-menu',
      version=__import__('admin_menu').__version__,
      description='A Django admin theme with a horizontal, tabbed navigation bar',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='http://github.com/cdrx/django-admin-menu',
      author='Chris Rose',
      license='MIT',
      packages=['admin_menu'],
      install_requires=[
          'libsass>=0.20,<0.21'
      ],
      zip_safe=False,
      keywords=['django', 'admin', 'theme', 'interface', 'menu', 'navigation'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
      )

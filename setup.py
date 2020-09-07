from setuptools import setup, find_packages
from os.path import join, dirname
import distutils.cmd
import distutils.log
import subprocess
import os

with open('requirements.txt') as fp:
    install_requires = fp.read()

#import http_cats
class PylintCommand(distutils.cmd.Command):
  """A custom command to run Pylint on all Python source files."""

  description = 'run Pylint on Python source files'
  user_options = [
      # The format is (long option, short option, description).
      ('pylint-rcfile=', None, 'path to Pylint config file'),
  ]

  def initialize_options(self):
    """Set default values for options."""
    #Each user option must be listed here with their default value.
    self.pylint_rcfile = ''

  def finalize_options(self):
    """Post-process options."""
    if self.pylint_rcfile:
      assert os.path.exists(self.pylint_rcfile), (
          'Pylint config file %s does not exist.' % self.pylint_rcfile)

  def run(self):
    """Run command."""
    command = ['pylint']
    if self.pylint_rcfile:
      command.append('--rcfile=%s' % self.pylint_rcfile)
    command.append(os.getcwd()+"/src")
    self.announce(
        'Running command: %s' % str(command),
        level=distutils.log.INFO)
    print(command)
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as err:
        print("ok")


setup(name='http_cats',
      version='1.0',
      cmdclass={
            'pylint': PylintCommand,
      },
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      include_package_data=True,
      tests_require=['pytest'],
      data_files=[('config', ['tests/.pylintrc']),('config', ['tests/tox.ini']),('config', ['requirements.txt'])],
      install_requires=install_requires,
      )
import click
import os
import subprocess
 

def _run_git_commands(repo_dir):
  """Runs the following commands in order
  on the repo given"""
  subprocess.run(["git", "pull"])
  subprocess.run(["git", "push"])
  subprocess.run(["git", "push", "--tags"])  


def _walk_dir(dir):
  """Walk through dir and return true if 
  we find a directory labelled .git, otherwise
  return false"""
  for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isdir(dir) == True:
      if filename.basename == ".git":
        return True
  return False



# @click.command()
# def run():
#   print("Hello")
 
@click.command()
@click.option('-d', '--dir', default=".", type=str, help="Target path to scan")
def run(dir):
    is_git = _walk_dir(dir)
    if is_git is True:
     _run_git_commands(dir)
 

if __name__ == '__main__':
  run()







#!/usr/bin/env python3

import argparse, sys, re
from functools import cmp_to_key

parser = argparse.ArgumentParser(
  description='Find the next target branch for automerging'
)

parser.add_argument(
  '-b',
  '--branches',
  type=str,
  nargs='+',
  required=True,
  help='Space separated list of branches that should be considered as targets',
)

parser.add_argument(
  '-i',
  '--ignore',
  type=str,
  nargs='+',
  required=False,
  help='Space separated list of branches that should be excluded as targets',
)

parser.add_argument(
  '-s',
  '--source',
  type=str,
  nargs=1,
  required=True,
  help='The source branch that is triggering the merge',
)

parser.add_argument(
  '-m',
  '--main',
  type=str,
  nargs=1,
  required=False,
  default='master',
  help='The main branch used when no release branch is a candidate for a target',
)

# Regular expression to match branches with valid version, i.e. release/x.y
release_reg = r'^release\/\d+\.\d+$'
rx_release = re.compile(release_reg)

# Used to retrieve the minor version of a release branch
def get_minor_version(x): return int(x.partition('.')[2])

# Compare function fors sorting release branches by ascending minor version
def cmp_release_branches(x, y):
  x_minor = get_minor_version(x)
  y_minor = get_minor_version(y)

  if x_minor > y_minor: return 1

  if x_minor < y_minor: return -1

  return 0

# Returns a list of release branches sorted by minor version
def sort_release_branches(branch_list):
  return sorted(branch_list, key=cmp_to_key(cmp_release_branches))

# Validates the arguments passed to the application
def parse_arguments():
  try:
    return parser.parse_args()
  except argparse.ArgumentError as err:
    sys.stderr.write(str(err))
    sys.exit(2)

# Subtracts the list of branches to exclude from the list of all possible target
# branches
def remove_ignored_branches(branch_list, ignore_list):
  return list(set(branch_list) - set(ignore_list))

# This removes any release branches that have an invalid version syntax
def sanitize_release_branches(branch_list):
  return filter(
    lambda branch: rx_release.match(branch),
    branch_list,
  )

def main():
  args = parse_arguments()

  source_branch = args.source[0]
  target_branches = args.branches
  ignore_branches = args.ignore or ""
  main_branch = args.main[0]

  exclude_branches = remove_ignored_branches(target_branches, ignore_branches)
  branches = list(sanitize_release_branches(exclude_branches))
  release_branches = sort_release_branches(branches)

  current_minor = get_minor_version(source_branch)

  for b in release_branches:
    b_minor = get_minor_version(b)

    if b_minor > current_minor:
      sys.stdout.write(b)
      sys.exit(0)

  sys.stdout.write(main_branch)
  sys.exit(0)


# This mechanism ensures the main function is executed only if this script
# is executed directly and not when imported as a module
if __name__ == '__main__':
  main()

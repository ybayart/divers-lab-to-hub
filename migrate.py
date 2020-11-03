#! /usr/bin/python3

import requests, json, gitlab, github, os
from subprocess import call, check_call

gl = gitlab.Gitlab('https://git.hexanyn.fr', private_token=os.environ.get('GITLAB_TOKEN'))
gh = github.Github(os.environ.get('GITHUB_TOKEN'))

projects = gl.projects.list(all=True)
call('mkdir -p repo', shell=True)
for project in projects:
	print(project.name_with_namespace)
	try:
		check_call('git -C repo/{} pull > /dev/null 2>&1'.format(project.path_with_namespace), shell=True)
	except:
		call('git clone {} repo/{} > /dev/null 2>&1'.format(project.ssh_url_to_repo, project.path_with_namespace), shell=True)
	try:
		gh_project = gh.get_user().get_repo(name=project.path_with_namespace.replace('/', '-'))
	except:
		gh_project = gh.get_user().create_repo(name=project.path_with_namespace, private=project.visibility!='public')
	call('git -C repo/{} remote add github {} > /dev/null 2>&1'.format(project.path_with_namespace, gh_project.ssh_url), shell=True)
	call('git -C repo/{} push github master'.format(project.path_with_namespace), shell=True)
	print('')

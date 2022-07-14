from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from .index_tree import tree

import json


views = Blueprint('views', __name__)

@views.route('/')
def home():
	tree.current_node = tree.root_node
	return render_template("home.html", user=current_user, index_tree=tree)

@views.route('/info')
def info():
    return render_template("info.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user, index_tree=tree)


@views.route('/lectures', methods=['GET', 'POST'])
def render_lectures():
	if request.method == 'POST':
		print(request.data)
		node_id = json.loads(request.data)['node_id']
		print("\n\n\n", node_id, "\n\n\n")
		for node in tree.current_node.children_nodes + [tree.current_node.parent_node]:
			if node_id == node.id:
				print('Hurray!')
				tree.current_node = node
				break
	return render_template("lectures.html", user=current_user, index_tree=tree)



# @views.route('/info/<pep>')
# def info_pep(pep):
#     print("\n\n\n", pep, "\n\n\n")
#     return render_template("info.html")
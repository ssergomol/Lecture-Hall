from flask import Blueprint, render_template
from flask_login import login_required, current_user

from .index_tree import tree

import json


views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("home.html", user=current_user, index_tree=tree)

@views.route('/info')
def info():
    return render_template("info.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user, index_tree=tree)


@views.route('/lectures', methods=['POST'])
def render_lectures():
	child_node_id = json.loads(request.data)
	for child_node in tree.current_node.children_nodes:
		if child_node_id == child_node.id:
			tree.current_node = child_node
			break
	return render_template("lectures.html", user=current_user, index_tree=tree)



# @views.route('/info/<pep>')
# def info_pep(pep):
#     print("\n\n\n", pep, "\n\n\n")
#     return render_template("info.html")
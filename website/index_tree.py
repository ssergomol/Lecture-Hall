# from .models import Publication

gen_index = 0
def generate_new_id():
	global gen_index
	gen_index += 1
	return gen_index



defalut_sections = {
	"name": "Лекции",
	"children": [
		{
			"name": "Механика",
			"children": [
				{
					"name": "Кинематика",
					"children": [
						{
							"name": "Механическое движение и его виды",
							"children": []
						},
						{
							"name": "Относительность механического движения",
							"children": []
						},
						{
							"name": "Правило сложения перемещений",
							"children": []
						},
						{
							"name": "Скорость",
							"children": []
						},
						{
							"name": "Ускорение",
							"children": []
						},
						{
							"name": "Равномерное движение",
							"children": []
						},
						{
							"name": "Прямолинейное равноускоренное движение",
							"children": []
						},
						{
							"name": "Свободное падение",
							"children": [
								{
									"name": "Движение тела по вертикали",
									"children": []
								},
								{
									"name": "Движение тела, брошенного горизонтально",
									"children": []
								},
								{
									"name": "Движение тела, брошенного под углом к горизонту",
									"children": []
								}
							]
						},
						{
							"name": "Движение по окружности с постоянной по модулю скоростью",
							"children": []
						},
						{
							"name": "Гармонические колебания",
							"children": []
						}
					]
				},
				{
					"name": "Динамика",
					"children": []
				},
				{
					"name": "Статика",
					"children": []
				}
			]
		},
		{
			"name": "Термодинамика",
			"children": []
		},
		{
			"name": "Электричество",
			"children": []
		},
		{
			"name": "Оптика",
			"children": []
		},
		{
			"name": "Квантовая физика",
			"children": []
		}
	]
}



class Node():
	def __init__(self, name, id, parent_node, children_nodes):
		self.name = name
		self.id = id
		self.parent_node = parent_node
		self.children_nodes = children_nodes


class IndexTree():
	def __init__(self, root_name='Лекции', root_id=0, root_parent_node=None, root_children_nodes=[]):
		self.root_node = Node(root_name, root_id, root_parent_node, root_children_nodes)
		self.current_node = self.root_node

	def add_defalut_sections(self, sections=defalut_sections):
		dfs(self.root_node, defalut_sections)

	def __repr__(self):
		res = dict()
		repr_dfs(self.root_node, res)
		return res


	def add_db_info(delf, db):
		pass

	def set_current(self):
		pass


def dfs(node, defalut_sections):
	for child in defalut_sections["children"]:
		new_node = Node(child["name"], generate_new_id(), node, [])
		node.children_nodes.append(new_node)
		dfs(new_node, child)

def repr_dfs(node, res):
	res["name"] = node.name
	res["id"] = node.id
	res["children"] = []
	for child_node in node.children_nodes:
		res["children"].append({"name": "", "id": -1, "children": []})
		repr_dfs(child_node, res["children"][-1])





if __name__ == '__main__':
	tree = IndexTree()
	tree.add_defalut_sections()
	print(tree.__repr__())

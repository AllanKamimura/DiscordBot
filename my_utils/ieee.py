import os
import re

def get_post_images(capitulo):
	"""
	Helper Function to Main Funcion get_post()
	
	input : String
		Society Chapter Name lower cased [.lower()]
	output : Tuple(String, List)
		chapter folder name and list of files in the folder
	"""
	
	base_folder = "./my_utils/ieee_utils"
	image_folder = os.path.join(base_folder, capitulo)
	image_list = os.listdir(image_folder)
	image_list.sort
	return image_folder, image_list
	
def get_post(mensagem):
	"""
	Function to spam the chat with Marketing related post from Instagram
	input : String
		unidecoded lowercased message
	output : Tuple(String, List)
		resposta: bot answer
		image_list: list with the path to the images
	"""
	
	if "cs" in mensagem:
		image_folder, image_list = get_post_images("cs")
		resposta = "para conhecer mais sobre os nossos projetos da Computer Society,\n converse com os nossos membros"
	elif "pes" in mensagem:
		image_folder, image_list = get_post_images("pes")
		resposta = "para conhecer mais sobre os nossos projetos da Power & Energy Society,\n converse com os nossos membros"
	elif "ras" in mensagem:
		image_folder, image_list = get_post_images("ras")
		resposta = "para conhecer mais sobre os nossos projetos da Robotics and Automation Society,\n converse com os nossos membros"
	elif "event" in mensagem: 
		image_folder, image_list = get_post_images("eventos")
		resposta = "para conhecer mais sobre os nossos eventos,\n converse com os nossos membros"
	else:
		image_folder, image_list = get_post_images("ieee")
		resposta = "pergunte pra loli sobre os nossos capitulos,\n IEEE-CS, IEEE-RAS, IEEE-PES e sobre os eventos que participamos"

	return resposta, image_folder, image_list
	
def get_role(message, mensagem, member_name):
	"""
	Funcion que pega uma mensagem enviada 
	"""
	capitulos = re.findall("quero entrar n[oa] ([\w -,]{2,})", mensagem)
	print(capitulos)
	
	roles_entrou = []
	capitulos_entrou = ""
	for capitulo in capitulos[0].split(","):
		print(capitulo)
		if capitulo in ["presid"] or any(name in capitulo for name in ["presid"]):
			resposta = "Golpe no <@374687177411526656>"
			return resposta, roles_entrou
	
		elif capitulo in ["cs", "comput"] or any(name in capitulo for name in ["cs", "comput"]):
			roles_entrou.append(695298595838230612)
			roles_entrou.append(882066954389700663)
			capitulos_entrou += " CS,"
			
		elif capitulo in ["pes", "poten", "energ"] or any(name in capitulo for name in ["pes", "poten", "energ"]):
			roles_entrou.append(695298637613367307)
			roles_entrou.append(882066954389700662)
			capitulos_entrou += " PES,"

		elif capitulo in ["ras", "robo"] or any(name in capitulo for name in ["ras", "robot"]):
			roles_entrou.append(695298686204248115)
			roles_entrou.append(882066954389700661)
			capitulos_entrou += " RAS,"

		elif capitulo in ["mkt", "marketing", "mark"] or any(name in capitulo for name in ["mkt", "marketing", "mark"]):
			roles_entrou.append(695298154299654205)
			roles_entrou.append(882066954389700665)
			capitulos_entrou += " Marketing,"

		elif capitulo in ["rh", "recursos", "human"] or any(name in capitulo for name in ["rh", "recurso", "human"]):
			roles_entrou.append(695298234096025724)
			roles_entrou.append(882066954389700664)
			capitulos_entrou += " Recursos Humanos,"
	confirm_text = capitulos_entrou[:-1]
	print(confirm_text)
	
	if len(confirm_text) > 1:
		resposta = "Parabains {}, você entrou no".format(member_name) + confirm_text
		
	else:
		resposta = "escolha entre: CS, PES, RAS, MKT e RH".format(member_name) + confirm_text
		
	return resposta, roles_entrou
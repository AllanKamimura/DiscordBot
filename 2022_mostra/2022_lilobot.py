import os
import discord
import unidecode
from wit import Wit

# bot intents
client = discord.Client(intents = discord.Intents.all())

# connect to wit.ai
wit_client = Wit(os.getenv('WIT_TOKEN'))

# roles color category
roles_cat = {"#9b59b6": 947268383672533022,
			 "#e74c3c": 947267479506403328,
			 "#3498db": 947267508224794635,
			 "#c27c0e": 947267482400469032,
			 "#ad1457": 947267506609995849,
			 "#f1c40f": 947267476595568721,
			 "#2ecc71": 947267461487689789
			}

#roles = {}
#cat_dict = {}
with open("./channels.txt", mode = "r", encoding = "utf-8-sig") as f:
	exec("cat_dict=" + f.read())

@client.event
async def on_ready():
	global main_guild
	
	print('We have logged in as {0.user}'.format(client))
	print(client.user)
	
	
	main_guild = client.get_guild(943990826881650759)
	filter_channel = main_guild.get_channel(947268761642233877)
	role_model = main_guild.get_role(946095884591071253)

## alphabetical order
#	for i, category_name in enumerate(list(cat_dict.keys())):
#		category = main_guild.get_channel(cat_dict[category_name]["category"])
#		await category.edit(position = i + 1)
		
#	for role in main_guild.roles:
#		roles[role.name] = role.id
#		
##		print('"{:<44}": {},'.format(role.name, role.id))
#		if role.name in ["@everyone", "LiLo-bot", "novo cargo", "Organizadores"]:
#			pass
#		else:
#			await role.edit(permissions = role_model.permissions, mentionable = True)
#		if role.name in cat_dict.keys():
#			print(role.name)
#			big_role = roles_cat[str(role.colour)]
#			
#			channel = main_guild.get_channel(cat_dict[role.name]["sobre"])
#			await channel.set_permissions(
#				target = main_guild.get_role(big_role),
#				overwrite = discord.PermissionOverwrite(
#					read_messages = True
#				)
#			)
#			
#			channel = main_guild.get_channel(cat_dict[role.name]["text"])
#			await channel.set_permissions(
#				target = main_guild.get_role(big_role),
#				overwrite = discord.PermissionOverwrite(
#					read_messages = True
#				)
#			)
#			
#			channel = main_guild.get_channel(cat_dict[role.name]["voice"])
#			await channel.set_permissions(
#				target = main_guild.get_role(big_role),
#				overwrite = discord.PermissionOverwrite(
#					read_messages = True
#				)
#			)
#			
#	for category in main_guild.categories:
#		cat_dict[category.name] = category.id
##		if category.name not in roles.keys():
##			print(category.name)
##			
##		else:
##			print(category.position)
##			
##			await category.set_permissions(
##				target = main_guild.get_role(947204544201363487),
##				overwrite = discord.PermissionOverwrite(
##					read_messages = False
##				)
##			)
##
##			await category.set_permissions(
##				target = main_guild.get_role(roles[category.name]),
##				overwrite = discord.PermissionOverwrite(
##					read_messages = True,
##					manage_channels = True,
##					manage_messages = True,
##					manage_webhooks = True,
##					deafen_members = True,
##					mute_members = True,
##					move_members = True,
##					view_audit_log = True,
##					view_guild_insights = True,
##					send_tts_messages = True,
##					use_slash_commands = True,
##				)
##			)
##			
##			await category.set_permissions(
##				target = main_guild.get_role(roles["@everyone"]),
##				overwrite = discord.PermissionOverwrite(
##				)
##			)
##
##
##			if len(category.channels) < 4:
##				channel_names = [channel.name for channel in category.channels]
##				if "backstage" not in channel_names:
##					await category.create_text_channel(name = "backstage")
##				if "sobre" not in channel_names:
##					await category.create_text_channel(name = "sobre")
##				if "text" not in channel_names:
##					await category.create_text_channel(name = "text")
##				if "voz" not in channel_names:
##					await category.create_voice_channel(name = "voz")
##		
##			channel_dict = {}
##
##			for channel in category.channels:
##				await channel.set_permissions(
##					target = main_guild.get_role(947204544201363487),
##					overwrite = discord.PermissionOverwrite(
##						read_messages = False
##					)
##				)
##				
##				if str(channel.type) == "text":
##					if channel.name == "sobre":
##						channel_dict["sobre"] = channel.id
##						await channel.edit(
##							topic = "Espaço reservado para apresentação da extra, descreva as atividades do grupo e informações adicionais. Podendo incluir imagens e links para redes sociais. Todos podem visualizar esse canal, mas apenas pessoas com a cargo da extra podem escrever aqui")
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles["Organizadores"]),
##							overwrite = discord.PermissionOverwrite(
##							)
##						)
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles[category.name]),
##							overwrite = discord.PermissionOverwrite(
##								read_messages = True,
##								send_messages = True,
##							)
##						)
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles["@everyone"]),
##							overwrite = discord.PermissionOverwrite(
##								send_messages = False,
##							)
##						)
##
##					elif channel.name == "backstage":
##						channel_dict["backstage"] = channel.id
##
##						await channel.edit(
##							topic = "Canal privado, apenas os membros da sua extra e a organização podem ver esse canal, pode ser usado para organização interna e conversas paralelas.")
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles["Organizadores"]),
##							overwrite = discord.PermissionOverwrite(
##							)
##						)
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles[category.name]),
##							overwrite = discord.PermissionOverwrite(
##								view_channel = True,
##							)
##						)
##	
##						await channel.set_permissions(
##							target = main_guild.get_role(roles["@everyone"]),
##							overwrite = discord.PermissionOverwrite(
##								view_channel = False,
##							)
##						)
##
##					elif channel.name == "text":
##						await channel.set_permissions(
##							target = main_guild.get_role(roles[category.name]),
##							overwrite = discord.PermissionOverwrite(
##								read_messages = True,
##								send_messages = True,
##							)
##						)
##						channel_dict["text"] = channel.id
##
##				elif str(channel.type) == "voice":
##					await channel.set_permissions(
##						target = main_guild.get_role(roles[category.name]),
##						overwrite = discord.PermissionOverwrite(
##							read_messages = True,
##						)
##					)
##					channel_dict["voice"] = channel.id
##
##					await channel.edit(name = "voz")
##
##			cat_dict[category.name] = channel_dict
##		
##				
##			


#	title = "Filtro Preto"
#	description = "Apenas o canal da sua extra ficara visivel para voce\n" 
#
#	embed = discord.Embed(title = title, description = description, color = 0xffffff)
#	embed.set_author(name = main_guild.get_member(828816674567618600).nick, 
#							 icon_url = main_guild.get_member(828816674567618600).avatar_url)
#	embed.add_field(name = "Reaja com o emoji: :white_check_mark:", value = "↓ ↓ ↓ ↓ ↓ ↓ ↓ <@&947204544201363487>", inline = False)
#	
#	message = await filter_channel.send(embed = embed)
#	await message.add_reaction("✅")
#	
#	title = "Filtros Coloridos"
#	description = "Visualizar extras por categoria\nAntes de utilizar os filtros coloridos, pegue o filtro preto acima\nPara remover o filtro, basta remover o reaction na mensagem" 	
#	embed = discord.Embed(title = title, description = description, color = 0xaaaaaa)
#	embed.set_author(name = main_guild.get_member(828816674567618600).nick, 
#							 icon_url = main_guild.get_member(828816674567618600).avatar_url)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:chart_with_upwards_trend: ", value = "<@&947267461487689789>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:computer:  ", value = "<@&947267508224794635>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:race_car:  ", value = "<@&947267476595568721>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:united_nations:  ", value = "<@&947267479506403328>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:steam_locomotive:  ", value = "<@&947267506609995849>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:satellite_orbital:  ", value = "<@&947267482400469032>", inline = True)
#	embed.add_field(name = "⠀⠀⠀⠀⠀:compression:  ", value = "<@&947268383672533022>", inline = True)
#	message = await filter_channel.send(embed = embed)
#	await message.add_reaction("📈")
#	await message.add_reaction("💻")
#	await message.add_reaction("🏎️")
#	await message.add_reaction("🇺🇳")
#	await message.add_reaction("🚂")
#	await message.add_reaction("🛰️")
#	await message.add_reaction("🗜️")
	
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return message
	
	# login message filter
	elif len(message.content) < 2:
		return message
	
	# 947621007517184060: main_channel, 943990829079470092: test_channel
	elif (message.channel == main_guild.get_channel(947621007517184060)) or (message.channel == main_guild.get_channel(943990829079470092)):
		resp = wit_client.message(message.content)
		if len(resp["intents"]) > 0:
#			await message.channel.trigger_typing()

			intent = resp["intents"][0]["name"]
			intent_score = resp["intents"][0]["confidence"]

			if intent == "cadastro":
				try:
					entities = resp["entities"]["name:name"]
					if len(entities) > 0:
						for ent in entities:
							extra_name = ent["value"]
							extra_score = ent["confidence"]

							if extra_name in cat_dict.keys():

								extra_channel = cat_dict[extra_name]["sobre"]
								await message.channel.send(
									"**Cadastrar** em **{}**\n**Clique aqui**: :arrow_right: <#{}>, Para acessar o canal da sua extra\n\n[intent confidence: {}] [capture confidence: {}]".format(
										extra_name, extra_channel, intent_score, extra_score),
									reference = message
								)

								await message.author.add_roles(
									main_guild.get_role(
										cat_dict[extra_name]["role"]
									)
								)
				except:
					print(message)
					print(message.content)
					print(resp)




			elif intent == "procurar":
				try:
					entities = resp["entities"]["name:name"]
					if len(entities) > 0:
						for ent in entities:

							extra_name = ent["value"]
							extra_score = ent["confidence"]
							if extra_name in cat_dict.keys():
								extra_channel = cat_dict[extra_name]["sobre"]
								await message.channel.send(
									"**Procurar** por **{}**\n**Clique aqui**: :arrow_right: <#{}>, Para acessar o canal da sua extra\n\n[intent confidence: {}] [capture confidence: {}]".format(
										extra_name, extra_channel, intent_score, extra_score),
									reference = message
								)
				except:
					print(message)
					print(message.content)					
					print(resp)

			elif intent == "ajuda":
				await message.channel.send(
					"Envie `oi, sou da extra tal` para **pegar o cargo** da sua extra\nou `oi, onde ta o canal da extra tal?` para **encontrar** a sua extra",
					reference = message)
			
	elif str(message.channel.type) == "private":
		print(message)
		print(message.content)	
		
	else:
		pass
	
	if ("nitro" in unidecode.unidecode(message.content.lower())) or ("crypto" in unidecode.unidecode(message.content.lower())) or ("give away" in unidecode.unidecode(message.content.lower())) or ("nft" in unidecode.unidecode(message.content.lower())) or ("gift" in unidecode.unidecode(message.content.lower())):
		await message.channel.send("**Palavras proibidas** nesse servidor: :face_with_symbols_over_mouth: \n`nitro`, `crypto` `give away`, `NFT`, `gift`\nSe vc realmente quer falar isso, escreve tipo `ni-tro` kkkkkk", reference = message)
		print(message)
		print(message.content)

		await message.delete()
		
		
@client.event
async def on_raw_reaction_add(payload):
	if payload.message_id in [947341703440904232, 947341705420623872]:
		if str(payload.emoji) == "✅":
			await payload.member.add_roles(main_guild.get_role(947204544201363487))
		if str(payload.emoji) == "📈":
			await payload.member.add_roles(main_guild.get_role(947267461487689789))
		if str(payload.emoji) == "💻":
			await payload.member.add_roles(main_guild.get_role(947267508224794635))
		if str(payload.emoji) == "🏎️":
			await payload.member.add_roles(main_guild.get_role(947267476595568721))
		if str(payload.emoji) == "🇺🇳":
			await payload.member.add_roles(main_guild.get_role(947267479506403328))
		if str(payload.emoji) == "🚂":
			await payload.member.add_roles(main_guild.get_role(947267506609995849))
		if str(payload.emoji) == "🛰️":
			await payload.member.add_roles(main_guild.get_role(947267482400469032))
		if str(payload.emoji) == "🗜️":
			await payload.member.add_roles(main_guild.get_role(947268383672533022))

@client.event
async def on_raw_reaction_remove(payload):
	if payload.message_id in [947341703440904232, 947341705420623872]:
		member = main_guild.get_member(payload.user_id)
		
		if str(payload.emoji) == "✅":
			role = main_guild.get_role(947204544201363487)
		if str(payload.emoji) == "📈":
			role = main_guild.get_role(947267461487689789)
		if str(payload.emoji) == "💻":
			role = main_guild.get_role(947267508224794635)
		if str(payload.emoji) == "🏎️":
			role = main_guild.get_role(947267476595568721)
		if str(payload.emoji) == "🇺🇳":
			role = main_guild.get_role(947267479506403328)
		if str(payload.emoji) == "🚂":
			role = main_guild.get_role(947267506609995849)
		if str(payload.emoji) == "🛰️":
			role = main_guild.get_role(947267482400469032)
		if str(payload.emoji) == "🗜️":
			role = main_guild.get_role(947268383672533022)
			
		await member.remove_roles(role)
			
			
@client.event
async def on_guild_role_create(role):
	if role.guild == main_guild:
		dummy_dict = {"role": role.id}
		extra_name = role.name
		category = await main_guild.create_category_channel(name = extra_name)
		dummy_dict["category"] = category.id

		await category.set_permissions(
			target = role,
			overwrite = discord.PermissionOverwrite(
				read_messages = True,
				manage_channels = True,
				manage_messages = True,
				manage_webhooks = True,
				deafen_members = True,
				mute_members = True,
				move_members = True,
				view_audit_log = True,
				view_guild_insights = True,
				send_tts_messages = True,
				use_slash_commands = True,
			)


		)

		channel = await category.create_text_channel(name = "backstage")
		await channel.set_permissions(
			target = role,
			overwrite = discord.PermissionOverwrite(
				view_channel = True,
			)
		)

		await channel.set_permissions(
			target = main_guild.get_role(943990826881650759), #everyone
			overwrite = discord.PermissionOverwrite(
				view_channel = False,
			)
		)
		dummy_dict["backstage"] = channel.id

		channel = await category.create_text_channel(name = "sobre")
		await channel.set_permissions(
			target = role,
			overwrite = discord.PermissionOverwrite(
				read_messages = True,
				send_messages = True,
			)
		)
		await channel.set_permissions(
			target = main_guild.get_role(947204544201363487),
			overwrite = discord.PermissionOverwrite(
				view_channel = False,
			)
		)
		await channel.set_permissions(
			target = main_guild.get_role(943990826881650759),#everyone
			overwrite = discord.PermissionOverwrite(
				send_messages = False,
			)
		)
		dummy_dict["sobre"] = channel.id

		channel = await category.create_text_channel(name = "text")
		await channel.set_permissions(
			target = main_guild.get_role(947204544201363487),
			overwrite = discord.PermissionOverwrite(
				view_channel = False,
			)
		)
		dummy_dict["text"] = channel.id

		channel = await category.create_voice_channel(name = "voz")
		await channel.set_permissions(
			target = main_guild.get_role(947204544201363487),
			overwrite = discord.PermissionOverwrite(
				view_channel = False,
			)
		)
		dummy_dict["voz"] = channel.id
		print(dummy_dict)
		cat_dict[extra_name] = dummy_dict
	
client.run(os.getenv('DISCORD_TOKEN'))
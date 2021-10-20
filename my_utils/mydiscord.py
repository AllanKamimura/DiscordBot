import os
import re
import pandas as pd

letrinhas_list = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"]
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"

def rollcall(message):   
    #text channel -> voice channel
    channel_dict = {
        696752807922892870: 695297816708251819, #diretoria
        700096324791566358: 695298381660028989, #marketing
        697914527433490462: 695298447607201833, #RH
        701859610482442360: 695299755848499230, #RP
        701506758082035742: 695299092779368529, #PES
        702933954315026503: 695299139659104328, #RAS
        698292835924967525: 695299043571662869, #CS
        713806379097522207: 713806323359285366, # nas escolas
        695294625665253428: 702936628670234736 #geral
    }
    text_channel = message.channel.id
    
    if text_channel in channel_dict.keys():
        voice_channel = message.guild.get_channel(channel_dict[text_channel])
       
        members = voice_channel.members
        member_list = []
        
        for member in members:
            member_name = member.nick
            if member_name is None:
                print("sem nick")
                member_name = member.name
            member_list.append(member_name)
    
    resposta = "\n".join(member_list)
    return resposta

def read_alternativas(message):
    if '"' in message.content:
        alternativas = re.findall('"([\w\n\d ?!@#$%¨&*\(\)]{1,})"', message.content)
    elif "\n" in message.content:
        alternativas = message.content.split("\n")[1:]
    else:
        alternativas = ""
        
    print(alternativas)
    return alternativas
    
def open_poll(alternativas, translate, embed, member_name, icon_url):    
    if len(alternativas) == 1:
        translate = {}

        embed.set_author(name = member_name, icon_url = icon_url)
        embed.add_field(name = ":white_check_mark:", value = "sim")
        embed.add_field(name = ":x:", value = "não")
        
        translate["✅"] = "SIM"
        translate["❌"] = "NÃO"
        poll_question = True
        
    elif len(alternativas) > 1:
        translate = {}

        embed.set_author(name = member_name, icon_url = icon_url)
        for alternativa, letter in zip(alternativas[1:], ascii_lowercase):
            embed.add_field(
                name = ":regional_indicator_{}: Alternativa {}".format(letter, letter.upper()), 
                value = alternativa,
                inline = False)
        for alternativa, letter in zip(alternativas[1:], letrinhas_list):
            translate[letter] = alternativa
        poll_question = True
        
    else:
        poll_question = False
        print("poll help")
        
    return embed, translate, poll_question

def add_alternativas(translate):
    alternativas = list(translate.keys())
    if "🇦" in alternativas :
        emojis = letrinhas_list[:len(alternativas)]
        
    elif "✅" in alternativas:
        emojis = ["✅", "❌"]
        
    return alternativas, emojis  
        
async def close_poll(poll_message, translate):
    reactions = poll_message.reactions
    reactions_list = []
    people_list = []
    
    for reaction in reactions:
        if reaction.emoji in letrinhas_list + ["✅", "❌"]:
            reactions_list.append(translate[reaction.emoji])
            reaction_people_list = await reaction.users().flatten()
            name_list = [user.nick if user.nick is not None else user.name for user in reaction_people_list]
            people_list.append(name_list)
        else:
            continue

    df = pd.DataFrame(data = [reactions_list, people_list])
    
    out_folder = os.path.join(".", "my_utils", "mydiscord", "poll_resposta.csv")  
    try:
        df.transpose().to_csv(out_folder, index = False, encoding = 'latin1', header = False)
    except:
        df.transpose().to_csv(out_folder, index = False, encoding = 'utf8', header = False)
        
    return out_folder
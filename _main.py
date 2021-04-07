# Importation de librairies
import discord
from discord.ext import commands

import asyncio

import random

import datetime

from datetime import datetime

from async_timeout import timeout

# création d'une instance de bot (préfixe + description)
bot = commands.Bot(command_prefix = "p!", description = "Pépute!")
bot.remove_command("help")
bot.remove_command("warn")


# On crée un event qui sera une fonction appelée par la librairie discord quand le bot est prêt et qui sera envoyée dans la console python.
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="p!commands"))
	print(str(datetime.now()))
	print("Ready!")

#Commande à faire pour s'assurer que le bot fonctionne.
@bot.command()
@commands.has_role("Modérateur")
async def helloworld(ctx):
	await ctx.send("Chef oui Chef!")

@bot.command()
async def say(ctx, *, question):
	if ctx.message.author.id == 328480752561815553:
		await ctx.message.delete()
		await ctx.send(f'{question}')
	elif ctx.message.author.id == 518780406422700032:
		await ctx.send("Bon par contre ça fonctionne pas à chaque fois\nDonc chuuut mais je te nem donc ça passe na? :p")
	else:
		await ctx.message.delete()
		await ctx.send("T'as po l'droit toa! è-é")

#Commande Liste commandes
@bot.command()
async def commands(ctx):
	await ctx.send("lulu\ntaumate\nmiemie\nsachou\ntatarn\nfraisou\nhanae")

@bot.command()
async def lulu(ctx):
	n = random.randint(1, 51)
	if n==1:
		await ctx.send("Cherche des dickpics!")
	if n==2:
		await ctx.send("Nous manipule à l'aide de ses doubles comptes!")
	if n==3:
		await ctx.send("Apprend qu'y a eu une réforme du BAC!")
	if n==4:
		await ctx.send("Vient d'apprendre que le covid existe!")
	if n==5:
		await ctx.send("Vient de se réveiller... À 15 heures")
	if n==6:
		await ctx.send("Chope un doigt de sirène!")
	if n==7:
		await ctx.send("A une arme dans son dos!")
	if n==8:
		await ctx.send("Défonce, heu valide une fiche!")
	if n==9:
		await ctx.send("Envoie une photo de bite pour calmer quelqu'un.")
	if n==10:
		await ctx.send("Se cache des péputes!")
	if n==11:
		await ctx.send("Se demande si masser c'est tromper!")
	if n==12:
		await ctx.send("Écoute Sachouille quand il dort! é-è")
	if n==13:
		await ctx.send("Arrive pas à poser un Portoloin!")
	if n==14:
		await ctx.send("Fait des gâteaux!")
	if n==15:
		await ctx.send("Mange son petit dej au milieu de l'aprem!")
	if n==16:
		await ctx.send("Voit des allusions sexuelles partout autour d'elle!")
	if n==17:
		await ctx.send("Va trop loin dans un ERP INRP et vient en MP!")
	if n==18:
		await ctx.send("Enseigne le Sortilège du Feudeymon à ceux qui le lui demandent!")
	if n==19:
		await ctx.send("A défragmenté son SSD puis passe onze heures à trouver une solution à ses bêtises! è-é")
	if n==20:
		await ctx.send("Tapine!")
	if n==21:
		await ctx.send("Mange la poussière!")
	if n==22:
		await ctx.send("Pense que dire Mage Noir c'est raciste!")
	if n==23:
		await ctx.send("« C'est grand? Ça c'est grand ça? C'est un bonnet C à tout casser! »")
	if n==24:
		await ctx.send("*Apparition de boobs aléatoires*")
	if n==25:
		await ctx.send("*Arrive dans le jeu, court et se prend une porte pour essayer*")
	if n==26:
		await ctx.send("Voit rouge ! Ou magenta ? Nan c'est du rouge... Heu help?")
	if n==27:
		await ctx.send("À poil lo! è-é")
	if n==28:
		await ctx.send("« Ben si on a pas de scénario ben... voilà. »")
	if n==29:
		await ctx.send("**2035** pas 2025 banane!")
	if n==30:
		await ctx.send("Luciana, Directeur et Harceleur depuis 1936.")
	if n==31:
		await ctx.send("« Pas encore une pépute »")
	if n==32:
		await ctx.send("Tout le monde: *parle d'un sujet random*\nLuciana: *Ramène ça aux boobs*")
	if n==33:
		await ctx.send("Nouveau triple A: Need for sex")
	if n==34:
		ctx.sebd("Lulu quand elle voit un salon de validation en blanc:")
		ctx;send("https://cdn.discordapp.com/attachments/741233431870177291/808993951163744297/unknown.png")
	if n==35:
		await ctx.send("Eliott se tortionnaire xD")
	if n==36:
		await ctx.send("Eliott: We are going to Disneyland!\nÉlèves:")
		await ctx.send("https://cdn.discordapp.com/attachments/741233431870177291/808995465285992468/unknown.png")
	if n==37:
		await ctx.send("https://cdn.discordapp.com/attachments/741233431870177291/809003000806375435/unknown.png")
	if n==38:
		await ctx.send("Agrou! è-é")
	if n==39:
		await ctx.send("Lulu et le romantisme... une belle histoire d'am-\nLuciana: À poil lo! è-é")
	if n==40:
		await ctx.send("Si lulu jouait à gta V:")
		await ctx.send("https://cdn.weeb.sh/images/B1qosktwb.gif")
	if n==41:
		await ctx.send("Est punie!")
	if n==42:
		await ctx.send("#teamgrincheux! è-é")
	if n==43:
		await ctx.send("Bullyeuse en chef!")
	if n==44:
		await ctx.send("Mama de la mafiaaaaaa!")
	if n==45:
		await ctx.send("On veut plus de vidéos lo! èoé")
	if n==46:
		await ctx.send("Owen le démon démoniaque débarque!")
	if n==47:
		await ctx.send("Galère avec les bots!")
	if n==48:
		await ctx.send("Alors c'est Vesuvia, Edmond et Claire qui étudient l'arithmancie...")
	if n==49:
		await ctx.send("« Oh je peux zoomer? » *Zoom vers un décolté* « Oh il est très joli votre haut madame »")
	if n==50:
		await ctx.send("*Arrive dans des toilettes au milieu de gens et se mets à sauter de façon random*")
	if n==51:
		await ctx.send("*Voit une plante extraterrestre/du future*\n« Oh c'est une grosse bite c'est ça? »")
		await ctx.send("https://cdn.discordapp.com/attachments/741233431870177291/810206719812304966/unknown.png")

@bot.command()
async def taumate(ctx):
	n = random.randint(1, 18)
	if n==1:
		await ctx.send("Se fait bully par un bot !")
	if n==2:
		await ctx.send("S'appelle en réalité Goblet !")
	if n==3:
		await ctx.send("Touche un portoloin et se désintègre !")
	if n==4:
		await ctx.send("Son égo surdimensionné n'a d'égal que ses gros pieds ! ")
	if n==5:
		await ctx.send("A la folie des grandeurs dans ses fiches personnages !")
	if n==6:
		await ctx.send("Stalk ses copains derrière des buissons !")
	if n==7:
		await ctx.send("Est la biatch de RaidProtect !")
	if n==8:
		await ctx.send("A son frère irl dont le second perso joue le frère inrp de son second perso ! Compris ?")
	if n==9:
		await ctx.send("Vend carte du maraudeur lo! Bon marché lo! Etvia amazon lo hin!")
	if n==10:
		await ctx.send("Anal Walker restera dans nos cœurs.")
	if n==11:
		await ctx.send("Verge\n*Nom féminin*\nBaguette (pour frapper, battre les enfants).\n« C'est officiel, la langue française a plein de double sens... Mais celui-ci est vraiment obvious... Perso, j'adore frapper les enfants avec ma verge... :smirk: :smirk: :smirk: »")
	if n==12:
		await ctx.send("Les règles de fight club sont simples...")
	if n==13:
		await ctx.send("**Sacha Baranovich Armiansky réalise son premier feudeymon, one shot. Thomas l'observe, admiratif.\n\n- Woah, t'es hyper chaud en fait !!!\n\nSacha répond sans aucune modestie.\n\n- Ben ouais, dans le milieu on m'appelle Sachalumeau, parce que je vais tous vous allumer...**")
	if n==14:
		await ctx.send("Et sa légendaire autorité!")
	if n==15:
		await ctx.send("Une énergie particulirèment... énergique")
	if n==16:
		await ctx.send("Thomas: *Poste une fiche de demi-dieu*\n Lulu et Sacha:")
		await ctx.send("https://tenor.com/view/fight-guns-gun-get-ready-gif-11837029")
	if n==17:
		await ctx.send("Est jaloux des beaux cheveux longs noirs, et soyeux de Vrusvrus! (Et il brillent à cause de la mana! è-é")
		await ctx.send("https://tenor.com/view/severus-snape-harry-potter-sassy-hair-flip-because-im-worth-it-gif-13910317")
	if n==18:
		await ctx.send("TG!")


@bot.command()
async def miemie(ctx):
	n = random.randint(1, 3)
	if n==1:
		await ctx.send("Se fait bully par Discordo via les salons nsf!")
	if n==2:
		await ctx.send("Graou! è-é")
	if n==3:
		await ctx.send("Écris kitchen au lieu de bitch!\nLuciana: LA PLACE DE LA FEMME C'EST À LA KOUIZINE!!!")

@bot.command()
async def sachou(ctx):
	n = random.randint(1, 27)
	f = random.randint(1, 200)
	if n==1:
		await ctx.send("« J'vais t'faire un anilagus! »")
	if n==2:
		await ctx.send("Essaie de mute un modo mais ils sont tous contre lui les bots lo! è-é")
	if f==19:
		await ctx.send("-Sachouille\n-Sachatouille\n-Sachatte\n-Sachiale\n-Sachier\n-Sachut\n-Sachute\n-Sashit\n-Sachiotte\n-Sachateau\n-Sachapeau\n-Sachapelet\n-Sachard'assaut\n-Sachariot\n-Sachlinge\n-Sachameau\n-Sacharlot\n-Sacharlotte aux fraises\n-Sacheveux\n-Sachauffe\n-Sachalet\n-Sachauve\n-Sachat\n-Sachille\n-Sachien\n-Savachier\n-Sachimi\n-Sachambre\n-Sacaille\n-Sachlingue\n-Sachocolat\n-Sacatain\n-Sacataing\n-Sachouilla\n-Sachouine\n-Sachabichou\n-Sachafouin\n-Sachagasse\n-Sachagriné\n-Sachahut\n-Sachoupinette\n-Sachou\n-Sachakra\n-Sachoukie\n-Sachaleur\n-Sachaloupe\n-Sachaman\n-Sachamaille\n-Sachamboulé")
	if n==3:
		await ctx.send("Encore une autre fiche de lulu c-c")
	if n==4:
		await ctx.send("Crois que Taumate demande en mariage Lulu!")
	if n==5:
		await ctx.send("Le verre d'eau * - *")
	if n==6:
		await ctx.send("« Ma grosse argumentation est ma force! ...\n ||Ma bouteille de thé!|| »")
	if n==7:
		await ctx.send("Se fait bully par les dés T-T")
	if n==8:
		await ctx.send("nianianiania scrogneugneuh!")
	if n==9:
		await ctx.send("Agrou! è-é")
	if n==10:
		await ctx.send("*Sacha est en train d'écrire*")
		await ctx.send("https://cdn.discordapp.com/emojis/296327525309612032.png?v=1")
	if n==11:
		await ctx.send("Sacha qui arrive après que Lulu ait donné son avis sur une fiche:")
		await ctx.send("https://tenor.com/view/damage-thats-a-lot-of-damage-jon-tron-gif-13054497")
	if n==12:
		await ctx.send("Sacha quand un joueur va trop loin INRP:")
		await ctx.send("https://tenor.com/view/now-thats-a-lot-of-pings-now-thats-a-lot-of-damage-gif-19591578")
	if n==13:
		await ctx.send("« Ouah! Il rp super bien! il doit faire des jets de malade! »\n Sacha avec des dés de 90: 2")
	if n==14:
		await ctx.send("Parti boire son thé")
	if n==15:
		await ctx.send("Tape son nouveau bot!")
	if n==16:
		await ctx.send("Ne voit pas le bout de la fiche d'alexei! :oula1:")
	if n==17:
		await ctx.send("Pense au suicide après qu'une énième fois de plus un membre ait envoyé un message en valdiation alors qu'il devrait pas")
	if n==18:
		await ctx.send("Se frappe la tête contre son bureau car bloqué depuis un mois sur le même problème quand il code des bots è-é")
	if n==19:
		await ctx.send("Rêve de boire un Sbitten")
	if n==20:
		await ctx.send("Pense au suicide lorsqu'un énième erreur Python se pointe dans le Terminal")
	if n==21:
		await ctx.send("A rage quit! èoé")
	if n==22:
		await ctx.send("Apparait inrp!... Ah bah non en fait")
	if n==23:
		await ctx.send("Se demande si coder ce bot a une grande utilité")
	if n==24:
		await ctx.send("Rage")
		await ctx.send("https://cdn.discordapp.com/attachments/741233431870177291/809942041798639636/unknown.png")
	if n==25:
		await ctx.send("Ding ding la clochette a sonné, il est temps d'arrêter de taper au clavier le temps que le démon passe!")
	if n==26:
		await ctx.send("Sachou, ce rebelle! è-é")
	if n==27:
		await ctx.send("LE WIKO")

@bot.command()
async def hanae(ctx):
	n = random.randint(1, 3)
	if n==1:
		await ctx.send("https://tenor.com/view/girl-rage-hairbrush-gif-9806845")
	if n==2:
		await ctx.send("La reine des gifs!")
	if n==3:
		await ctx.send("#teambonnehumeur !")

@bot.command()
async def fraisou(ctx):
	n = random.randint(1, 5)
	if n==1:
		await ctx.send("(Désolé je pouvais que renvoyer cette image xDDDD)")
		await ctx.send("https://cdn.discordapp.com/attachments/729078474517643294/796769721650905088/Sans_titre.png")
	if n==2:
		await ctx.send("Se fait bully par Owen!")
	if n==3:
		await ctx.send("À poil lo! è-é")
	if n==4:
		await ctx.send("Notre petit soleil à nous! :p")
	if n==5:
		await ctx.send("Rage sur sa taille et désire que Sachou s'étouffe avec son thé! é-è")

@bot.command()
async def tatarn(ctx):
	n = random.randint(1,4)
	if n==1:
		await ctx.send("Tarte Tatarn!")
	if n==2:
		await ctx.send("À poil lo! è-é")
	if n==3:
		await ctx.send("Continue la fiche de Taré!")
	if n==4:
		await ctx.send("Woof woof!")


bot.run("ODA5MDEyMTYyNDQxNTEwOTEy.YCO5Sg.EJwctcjUphDp5wAMxsLjLbBVibE")

#set up connection to machine learning model 
import azureml
from azureml.core import Workspace
# Check core SDK version number
import json
import league_api

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
def get_players_attributes(champion_name,role,team,summoner_name,champions):
	league = league_api.LeagueAPI()
	league.set_key("RGAPI-d186c4b8-e781-4639-ad3e-f1eb49014cff")
	print("got leage")
	(summonerName,summonerId,accountId) = league.get_player_name(summoner_name)
	player_match_hist = league.get_player_match_hist(accountId)[:3]
	player_stats = {}
	player_stats['{}_{}_avg(gold_earned)'.format(team,role)] = 0
	player_stats['{}_{}_avg(kills)'.format(team,role)] = 0
	player_stats['{}_{}_avg(assists)'.format(team,role)] = 0
	player_stats['{}_{}_avg(deaths)'.format(team,role)] = 0
	player_stats['{}_{}_avg(visionScore)'.format(team,role)] = 0
	player_stats['{}_{}_avg(totalDamageDealt)'.format(team,role)] = 0
	player_stats['{}_{}_avg(totalDamageTaken)'.format(team,role)] = 0
	player_stats['{}_{}_avg(totalMinionsKilled)'.format(team,role)] = 0
	player_stats['{}_{}_avg(totalTimeCrowdControlDealt)'.format(team,role)] = 0   
	for match in player_match_hist:
		game_stats = league.get_game_stats(match)
		for player in game_stats['participantIdentities']: #find the player stats for that match
			if player['player']['accountId'] == accountId:
				player_num = player['participantId']   
		gameDuration = game_stats['gameDuration']/60
		for player in game_stats['participants']:
			if player['participantId'] == player_num:
				#get features for this player in this game
				stats = player['stats']
				player_stats['{}_{}_avg(gold_earned)'.format(team,role)] += stats['goldEarned']/gameDuration
				player_stats['{}_{}_avg(kills)'.format(team,role)] += stats['kills']/gameDuration
				player_stats['{}_{}_avg(assists)'.format(team,role)] += stats['assists']/gameDuration
				player_stats['{}_{}_avg(deaths)'.format(team,role)] += stats['deaths']/gameDuration
				player_stats['{}_{}_avg(visionScore)'.format(team,role)] += stats['visionScore']/gameDuration
				player_stats['{}_{}_avg(totalDamageDealt)'.format(team,role)] += stats['totalDamageDealt']/gameDuration
				player_stats['{}_{}_avg(totalDamageTaken)'.format(team,role)] += stats['totalDamageTaken']/gameDuration
				player_stats['{}_{}_avg(totalMinionsKilled)'.format(team,role)] += stats['totalMinionsKilled']/gameDuration
				player_stats['{}_{}_avg(totalTimeCrowdControlDealt)'.format(team,role)] += stats['totalTimeCrowdControlDealt']/gameDuration
	for i in player_stats:
		player_stats[i] /= 3 #average stats
		
	#get champion_stats
	attributes = ['attackrange','armorperlevel','attackspeed',
					'attackdamageperlevel','hpperlevel','spellblockperlevel']
	champ = champions[champion_name]['stats']
	for att in attributes:
			player_stats["{}_{}_{}".format(team,role,att)] = champ[att]
	return player_stats

def feature_row_dict(players,champions):
	all_players_feature = {}
	for player in players:
		role = player[0]
		team = player[1]
		print("process {}_{}".format(role,team))
		champion_name = player[2]
		summoner_name = player[3]
		player_stats = get_players_attributes(champion_name,role,team,summoner_name,champions)
		all_players_feature=Merge(all_players_feature,player_stats)
	return all_players_feature

def create_feature_row(players,champions):
    all_players_feature = feature_row_dict(players,champions)
    features = ['100_CARRY_armorperlevel','100_CARRY_attackdamageperlevel','100_CARRY_attackrange',
 '100_CARRY_attackspeed','100_CARRY_avg(assists)','100_CARRY_avg(deaths)','100_CARRY_avg(gold_earned)',
 '100_CARRY_avg(kills)','100_CARRY_avg(totalDamageDealt)','100_CARRY_avg(totalDamageTaken)',
 '100_CARRY_avg(totalMinionsKilled)',
 '100_CARRY_avg(totalTimeCrowdControlDealt)',
 '100_CARRY_avg(visionScore)',
 '100_CARRY_hpperlevel',
 '100_CARRY_spellblockperlevel',
 '100_JUNGLE_armorperlevel',
 '100_JUNGLE_attackdamageperlevel',
 '100_JUNGLE_attackrange',
 '100_JUNGLE_attackspeed',
 '100_JUNGLE_avg(assists)',
 '100_JUNGLE_avg(deaths)',
 '100_JUNGLE_avg(gold_earned)',
 '100_JUNGLE_avg(kills)',
 '100_JUNGLE_avg(totalDamageDealt)',
 '100_JUNGLE_avg(totalDamageTaken)',
 '100_JUNGLE_avg(totalMinionsKilled)',
 '100_JUNGLE_avg(totalTimeCrowdControlDealt)',
 '100_JUNGLE_avg(visionScore)',
 '100_JUNGLE_hpperlevel',
 '100_JUNGLE_spellblockperlevel',
 '100_MIDDLE_armorperlevel',
 '100_MIDDLE_attackdamageperlevel',
 '100_MIDDLE_attackrange',
 '100_MIDDLE_attackspeed',
 '100_MIDDLE_avg(assists)',
 '100_MIDDLE_avg(deaths)',
 '100_MIDDLE_avg(gold_earned)',
 '100_MIDDLE_avg(kills)',
 '100_MIDDLE_avg(totalDamageDealt)',
 '100_MIDDLE_avg(totalDamageTaken)',
 '100_MIDDLE_avg(totalMinionsKilled)',
 '100_MIDDLE_avg(totalTimeCrowdControlDealt)',
 '100_MIDDLE_avg(visionScore)',
 '100_MIDDLE_hpperlevel',
 '100_MIDDLE_spellblockperlevel',
 '100_SUPPORT_armorperlevel',
 '100_SUPPORT_attackdamageperlevel',
 '100_SUPPORT_attackrange',
 '100_SUPPORT_attackspeed',
 '100_SUPPORT_avg(assists)',
 '100_SUPPORT_avg(deaths)',
 '100_SUPPORT_avg(gold_earned)',
 '100_SUPPORT_avg(kills)',
 '100_SUPPORT_avg(totalDamageDealt)',
 '100_SUPPORT_avg(totalDamageTaken)',
 '100_SUPPORT_avg(totalMinionsKilled)',
 '100_SUPPORT_avg(totalTimeCrowdControlDealt)',
 '100_SUPPORT_avg(visionScore)',
 '100_SUPPORT_hpperlevel',
 '100_SUPPORT_spellblockperlevel',
 '100_TOP_armorperlevel',
 '100_TOP_attackdamageperlevel',
 '100_TOP_attackrange',
 '100_TOP_attackspeed',
 '100_TOP_avg(assists)',
 '100_TOP_avg(deaths)',
 '100_TOP_avg(gold_earned)',
 '100_TOP_avg(kills)',
 '100_TOP_avg(totalDamageDealt)',
 '100_TOP_avg(totalDamageTaken)',
 '100_TOP_avg(totalMinionsKilled)',
 '100_TOP_avg(totalTimeCrowdControlDealt)',
 '100_TOP_avg(visionScore)',
 '100_TOP_hpperlevel',
 '100_TOP_spellblockperlevel',
 '200_CARRY_armorperlevel',
 '200_CARRY_attackdamageperlevel',
 '200_CARRY_attackrange',
 '200_CARRY_attackspeed',
 '200_CARRY_avg(assists)',
 '200_CARRY_avg(deaths)',
 '200_CARRY_avg(gold_earned)',
 '200_CARRY_avg(kills)',
 '200_CARRY_avg(totalDamageDealt)',
 '200_CARRY_avg(totalDamageTaken)',
 '200_CARRY_avg(totalMinionsKilled)',
 '200_CARRY_avg(totalTimeCrowdControlDealt)',
 '200_CARRY_avg(visionScore)',
 '200_CARRY_hpperlevel',
 '200_CARRY_spellblockperlevel',
 '200_JUNGLE_armorperlevel',
 '200_JUNGLE_attackdamageperlevel',
 '200_JUNGLE_attackrange',
 '200_JUNGLE_attackspeed',
 '200_JUNGLE_avg(assists)',
 '200_JUNGLE_avg(deaths)',
 '200_JUNGLE_avg(gold_earned)',
 '200_JUNGLE_avg(kills)',
 '200_JUNGLE_avg(totalDamageDealt)',
 '200_JUNGLE_avg(totalDamageTaken)',
 '200_JUNGLE_avg(totalMinionsKilled)',
 '200_JUNGLE_avg(totalTimeCrowdControlDealt)',
 '200_JUNGLE_avg(visionScore)',
 '200_JUNGLE_hpperlevel',
 '200_JUNGLE_spellblockperlevel',
 '200_MIDDLE_armorperlevel',
 '200_MIDDLE_attackdamageperlevel',
 '200_MIDDLE_attackrange',
 '200_MIDDLE_attackspeed',
 '200_MIDDLE_avg(assists)',
 '200_MIDDLE_avg(deaths)',
 '200_MIDDLE_avg(gold_earned)',
 '200_MIDDLE_avg(kills)',
 '200_MIDDLE_avg(totalDamageDealt)',
 '200_MIDDLE_avg(totalDamageTaken)',
 '200_MIDDLE_avg(totalMinionsKilled)',
 '200_MIDDLE_avg(totalTimeCrowdControlDealt)',
 '200_MIDDLE_avg(visionScore)',
 '200_MIDDLE_hpperlevel',
 '200_MIDDLE_spellblockperlevel',
 '200_SUPPORT_armorperlevel',
 '200_SUPPORT_attackdamageperlevel',
 '200_SUPPORT_attackrange',
 '200_SUPPORT_attackspeed',
 '200_SUPPORT_avg(assists)',
 '200_SUPPORT_avg(deaths)',
 '200_SUPPORT_avg(gold_earned)',
 '200_SUPPORT_avg(kills)',
 '200_SUPPORT_avg(totalDamageDealt)',
 '200_SUPPORT_avg(totalDamageTaken)',
 '200_SUPPORT_avg(totalMinionsKilled)',
 '200_SUPPORT_avg(totalTimeCrowdControlDealt)',
 '200_SUPPORT_avg(visionScore)',
 '200_SUPPORT_hpperlevel',
 '200_SUPPORT_spellblockperlevel',
 '200_TOP_armorperlevel',
 '200_TOP_attackdamageperlevel',
 '200_TOP_attackrange',
 '200_TOP_attackspeed',
 '200_TOP_avg(assists)',
 '200_TOP_avg(deaths)',
 '200_TOP_avg(gold_earned)',
 '200_TOP_avg(kills)',
 '200_TOP_avg(totalDamageDealt)',
 '200_TOP_avg(totalDamageTaken)',
 '200_TOP_avg(totalMinionsKilled)',
 '200_TOP_avg(totalTimeCrowdControlDealt)',
 '200_TOP_avg(visionScore)',
 '200_TOP_hpperlevel',
 '200_TOP_spellblockperlevel']
    final_row = []
    for feat in features:
        final_row.append(all_players_feature[feat])
    return final_row

def get_result(players):
	import os
	import azureml
	from azureml.core import Workspace
	from azureml.core.webservice import Webservice
	from azureml.core.authentication import ServicePrincipalAuthentication

	print("getting results")
	filename = os.path.join(app.static_folder, 'champion.json')
	with open(filename) as json_file:
			champions = json.load(json_file)['data']
	X = [create_feature_row(players,champions)]

	# Check core SDK version number
	print("SDK version:", azureml.core.VERSION)
	workspace="league-ws-deploy"
	subscription_id="79451499-b2c0-4513-8dea-ef7f37173fbb"
	resource_grp="league"


	svc_pr = ServicePrincipalAuthentication(
    tenant_id="1f0113ce-bee6-43b0-9e26-61617eced2e4",
    service_principal_id="4c9cfeac-dda9-4298-af3c-d51003c7438b",
    service_principal_password="646QyrNg7SiBvLNvjqZ-x:OdScv[uAs?")
 
	ws = Workspace(workspace_name = workspace,
				subscription_id = subscription_id,
				resource_group = resource_grp,
				auth=svc_pr)

	ws.get_details()

	print('Workspace name: ' + ws.name, 
		'Azure region: ' + ws.location, 
		'Subscription id: ' + ws.subscription_id, 
		'Resource group: ' + ws.resource_group, sep = '\n')

	print("Send to server to predict")
	sample = json.dumps({"data": X})
	sample = bytes(sample, encoding='utf8')
	service = Webservice(workspace=ws, name='lrmpredictfinal6')
	# predict using the deployed model
	result = service.run(input_data=sample)
	return result[0][1]


#routes.py
from flask import render_template, flash, redirect
from app import app
from app.forms import TeamForm

@app.route('/')
@app.route('/index')

def index():
	return("hello world")
	
@app.route('/predict', methods=['GET','POST'])
def predict():
	form=TeamForm()
	bplayers=[form.blueplayer1.data, form.blueplayer2.data, form.blueplayer3.data, form.blueplayer4.data, form.blueplayer5.data]
	bchamps=[form.bluechamp1.data, form.bluechamp2.data, form.bluechamp3.data, form.bluechamp4.data, form.bluechamp5.data]
	broles=[form.bluerole1.data, form.bluerole2.data, form.bluerole3.data, form.bluerole4.data, form.bluerole5.data]
	
	rplayers=[form.redplayer1.data, form.redplayer2.data, form.redplayer3.data, form.redplayer4.data, form.redplayer5.data]
	rchamps=[form.redchamp1.data, form.redchamp2.data, form.redchamp3.data, form.redchamp4.data, form.redchamp5.data]
	rroles=[form.redrole1.data, form.redrole2.data, form.redrole3.data, form.redrole4.data, form.redrole5.data]
	
	bpch=[[broles[i], "100", bchamps[i], bplayers[i]] for i in range(len(bplayers))]
	rpch=[[rroles[i], "200", rchamps[i], rplayers[i]] for i in range(len(rplayers))]
	pch=[]
	pch += bpch
	pch += rpch
	if form.validate_on_submit():
		result = get_result(pch)
		flash('The chance Blue team win is {}'.format(result))
		return redirect('/predict') #send input to model as list of tuples
	return render_template('team.html', form=form)
	
	
import os
import codecs
import json

print("Extracting data from pokemon replays")

win_weight = 2
lose_weight = 1

directory = os.listdir()
results = []
pkmn_weights_dict = {}

for replay_name in directory:
    if '.html' in replay_name:
        f = codecs.open(replay_name, 'r')
        data = f.read()
        f.close()
        
        ind1 = data.find("|poke|p1")
        ind2 =  data.find('|',data.rfind("|poke|p2|")+9)
        
        team_data = data[ind1:ind2].split('\n')
        p1_team = []
        p2_team = []
        for entry in team_data:
            if 'p1' in entry:
                if ',' in entry:
                    p_name = entry[entry.find('p1')+3:entry.find(',')]
                else:
                    p_name = entry[entry.find('p1')+3:]
                    
                p_name = p_name.replace("|item", "")
                p_name = p_name.replace("|", "")
                p_name = p_name.replace("-*", "")
                p1_team.append(p_name)
                
            elif 'p2' in entry:
                if ',' in entry:
                    p_name = entry[entry.find('p2')+3:entry.find(',')]
                else:
                    p_name = entry[entry.find('p2')+3:]
                    
                p_name = p_name.replace("|item", "")
                p_name = p_name.replace("|", "")
                p_name = p_name.replace("-*", "")
                p2_team.append(p_name)
                
        won_ind = data.find('won the battle')
        ind3 = data[:won_ind].rfind('<strong>')
        ind4 = data[:won_ind].rfind('</strong>')
        
        winner_name = data[ind3+8:ind4]
        
        ind5 = data.find('|',data.find('player|p1')+8)
        p1_name = data[ind5+1:data.find('|', ind5+1)]
        
        ind6 = data.find('|', data.find('player|p2')+8)
        p2_name = data[ind6+1:data.find('|', ind6+1)]
        
        if p1_name == winner_name:
            winner = 'p1'
            for pkmn in p1_team:
                if pkmn not in pkmn_weights_dict:
                    pkmn_weights_dict[pkmn] = win_weight
                else:
                    pkmn_weights_dict[pkmn] += win_weight
                    
            for pkmn in p2_team:
                if pkmn not in pkmn_weights_dict:
                    pkmn_weights_dict[pkmn] = lose_weight
                else:
                    pkmn_weights_dict[pkmn] += lose_weight
        else:
            winner = 'p2'
            for pkmn in p2_team:
                if pkmn not in pkmn_weights_dict:
                    pkmn_weights_dict[pkmn] = win_weight
                else:
                    pkmn_weights_dict[pkmn] += win_weight
                    
            for pkmn in p1_team:
                if pkmn not in pkmn_weights_dict:
                    pkmn_weights_dict[pkmn] = lose_weight
                else:
                    pkmn_weights_dict[pkmn] += lose_weight
            
        battle_data = {}
        battle_data['p1_team'] = p1_team
        battle_data['p2_team'] = p2_team
        battle_data['winner'] = winner
        
        results.append(battle_data)
        
        
            
    
with open('rp_file.json', 'w') as fout:
    json.dump(results, fout)
    
with open('pkmn_weights.json', 'w') as fout1:
    json.dump(pkmn_weights_dict, fout1)
    
print("Finished extracting data")
            
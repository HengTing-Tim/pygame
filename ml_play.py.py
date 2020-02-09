import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)
import pickle
import numpy as np

def ml_loop():
	filename = 'C:\\Users\\user\\Desktop\\Day02教材\\Day02教材\\04-磚塊怎麼打\\MLGame-master\\MLGame-master\\games\\arkanoid\\ml\\KNN_example.sav'
	model= pickle.load(open(filename,'rb'))
	comm.ml_ready()

	while True :
		scene_info = comm.get_scene_info()
		intp_temp =np.array([scene_info.ball[0],scene_info.ball[1],scene_info.platform[0]])
		input=intp_temp[np.newaxis,:]
		
		if scene_info.status == GameStatus.GAME_OVER or \
			scene_info.status == GameStatus.GAME_PASS:
			scene_info = comm.get_scene_info()
			
		move=model.predict(input)
		
		if move > 0:
			comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
		elif move < 0:
			comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
		else:
			comm.send_instruction(scene_info.frame, PlatformAction.NONE)
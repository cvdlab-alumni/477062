function makeExternalTexture(wallTesture){
	//external wall
      var textureWall = "brick-wall.jpg";
      //front wall texture
      wall = [[-1240/2,0],[1240/2,0],[1240/2,420],[-1240/2,420],[-1240/2,0]];
      holesDoor = [[20,20],[20,305.5],[165,305.5],[165,20],[20,20]];
      holesWindowsLeft = [[-488,198],[-310,198],[-310,375],[-488,375],[-488,198]];
      holesWindowsRight = [[290,120],[475,120],[475,320],[290,320],[290,120]];
      holes = [holesDoor, holesWindowsLeft, holesWindowsRight];
      var front_wall = buildWall(wall,holes,textureWall);
      front_wall.material.map.repeat.set(10,10);
      front_wall.rotation.x = Math.PI/2;
      front_wall.position.set(0,-.1,0);
      front_wall.scale.set(2000, 2000, 2000);
      wallTesture.add(front_wall);

      //base wall texture
      wall = [[-1240/2,0],[1240/2,0],[1240/2,860],[-1240/2,860],[-1240/2,0]];
      holes = [[0,0]]
      var down_wall = buildWall(wall,holes,textureWall);
      down_wall.material.map.repeat.set(10,10);
      down_wall.position.set(0,0,-.1);
      down_wall.scale.set(2000, 2000, 2000);
      wallTesture.add(down_wall);

      //behind wall texture
      wall = [[-1240/2,0],[1240/2,0],[1240/2,420],[-1240/2,420],[-1240/2,0]];
      holes = [[0,0]]
      var behind_wall = buildWall(wall,holes,textureWall);
      behind_wall.material.map.repeat.set(10,10);
      behind_wall.position.set(0,860.1,0);
      behind_wall.rotation.x = Math.PI/2;
      behind_wall.scale.set(2000, 2000, 2000);
      wallTesture.add(behind_wall);

      //left wall texture
      wall = [[-860/2,0],[860/2,0],[860/2,420],[-860/2,420],[-860/2,0]];
      holes = [[0,0]]
      var left_wall = buildWall(wall,holes,textureWall);
      left_wall.material.map.repeat.set(10,10);
      left_wall.position.set(-(1240/2)-.1,430,0);
      left_wall.rotation.y = Math.PI/2;
      left_wall.rotation.x = Math.PI/2;
      left_wall.scale.set(2000, 2000, 2000);
      wallTesture.add(left_wall);

      //right wall texture
      wall = [[-860/2,0],[860/2,0],[860/2,420],[-860/2,420],[-860/2,0]];
      holesWindowsRight = [[260,170],[355,170],[355,370],[260,370],[260,170]];
      holes = [holesWindowsRight];
      var right_wall = buildWall(wall,holes,textureWall);
      right_wall.material.map.repeat.set(10,10);
      right_wall.position.set((1240/2)+.1,430,0);
      right_wall.rotation.x = Math.PI/2;
      right_wall.rotation.y = Math.PI/2;      
      right_wall.scale.set(2000, 2000, 2000);
      wallTesture.add(right_wall);
}
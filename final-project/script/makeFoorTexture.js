 function makeFoorTexture(model,textureLandRooms,textureBathroom){
 	//rooms land texture
	var floorTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureLandRooms);
	floorTexture.wrapS = floorTexture.wrapT = THREE.RepeatWrapping; 
	floorTexture.repeat.set(6,3);
	var floorMaterial = new THREE.MeshPhongMaterial( { map: floorTexture, side: THREE.DoubleSide});
	var floorGeometry = new THREE.PlaneGeometry(1240, 523);
	var floor = new THREE.Mesh(floorGeometry, floorMaterial);
	floor.position.set(0,261.5,20.1);
	floor.receiveShadow = true;
	model.add(floor);

	//kitchen land texture
	var floorTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureLandRooms);
	floorTexture.wrapS = floorTexture.wrapT = THREE.RepeatWrapping; 
	floorTexture.repeat.set(4,2);
	var floorMaterial = new THREE.MeshPhongMaterial( { map: floorTexture, side: THREE.DoubleSide});
	var floorGeometry = new THREE.PlaneGeometry(682, 330);
	var floor = new THREE.Mesh(floorGeometry, floorMaterial);
	floor.position.set(-259,685,20.1);
	floor.receiveShadow = true;
	model.add(floor);

	//bathroom land texture
	var floorTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	floorTexture.wrapS = floorTexture.wrapT = THREE.RepeatWrapping; 
	floorTexture.repeat.set(5,5);
	var floorMaterial = new THREE.MeshPhongMaterial( { map: floorTexture, side: THREE.DoubleSide});
	var floorGeometry = new THREE.PlaneGeometry(520, 330);
	var floor = new THREE.Mesh(floorGeometry, floorMaterial);
	floor.position.set(340,688,20.1);
	floor.receiveShadow = true;
	model.add(floor);

	//bathroom wall texture left
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(4,4);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(280, 320);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(105.2,700,330/2-5);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//bathroom wall texture behind door
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(1,4);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(51, 280);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(130,540.2,330/2-5);
	wall.rotation.x = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//bathroom wall texture down
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(3,3);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(295, 280);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(450,540.2,330/2-5);
	wall.rotation.x = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//bathroom wall texture between window
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(2,1);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(280, 60);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(599.8,819,330/2-5);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(3,3);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(280, 170);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(599.8,605,330/2-5);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(2,1);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(148, 99);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(599.8,739,330/2-68);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//bathroom wall texture up and kitchen up
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(13,5);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(1200, 280);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(0,839.8,330/2-5);
	wall.rotation.x = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//kitchen wall texture left
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(4,4);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(280, 320);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(-1240/2+20.2,700,330/2-5);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//kitchen wall texture right
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(5,4);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(280, 330);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(80,690,330/2-5);
	wall.rotation.y = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);

	//kitchen down
	var wallTexture = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureBathroom);
	wallTexture.wrapS = wallTexture.wrapT = THREE.RepeatWrapping; 
	wallTexture.repeat.set(10,4);
	var wallMaterial = new THREE.MeshPhongMaterial( { map: wallTexture, side: THREE.DoubleSide});
	var wallGeometry = new THREE.PlaneGeometry(556, 280);
	var wall = new THREE.Mesh(wallGeometry, wallMaterial);
	wall.position.set(-330,540.7,330/2-5);
	wall.rotation.x = Math.PI/2;
	wall.receiveShadow = true;
	model.add(wall);
}
function makeLight(lightScene){
	//left right
      var spotLight = new THREE.SpotLight(0xffffff);
      spotLight.position.set(-2000, 1200, 600);
      spotLight.angle = Math.PI/9;
      spotLight.intensity = 1;
      // var spotLightHelper0 = new THREE.SpotLightHelper(spotLight);
      // spotLight.add(spotLightHelper0);

      //right light
      var spotLight1 = new THREE.SpotLight(0xffffff);
      spotLight1.position.set(2000, 500, 600);
      spotLight1.angle = Math.PI/6;
      spotLight1.intensity = 1;
      // var spotLightHelper1 = new THREE.SpotLightHelper(spotLight1);
      // spotLight1.add(spotLightHelper1);

      //front light
      var spotLight2 = new THREE.SpotLight(0xffffff);
      spotLight2.position.set(0, -2000, 1000);
      spotLight2.angle = Math.PI/2;
      spotLight2.intensity = 1.5;
      // var spotLightHelper2 = new THREE.SpotLightHelper(spotLight2);
      // spotLight2.add(spotLightHelper2);
     
      //behind light
      var spotLight3 = new THREE.SpotLight(0xffffff);
      spotLight3.position.set(0, 2000,200);
      spotLight3.angle = Math.PI/4;
      spotLight3.intensity = 1;
      // var spotLightHelper3 = new THREE.SpotLightHelper(spotLight3);
      // spotLight3.add(spotLightHelper3);
     
      //down light
      var spotLight4 = new THREE.SpotLight(0xffffff);
      spotLight4.position.set(0, 1500,-1000);
      spotLight4.angle = Math.PI/4;
      spotLight4.intensity = 1;
      // var spotLightHelper4 = new THREE.SpotLightHelper(spotLight4);
      // spotLight4.add(spotLightHelper4);

      //up light
      var spotLight5 = new THREE.SpotLight(0xffffff);
      spotLight5.position.set(0, 500,1500);
      spotLight5.angle = Math.PI/3;
      spotLight5.intensity = 1;
      spotLight5.castShadow = true;
      spotLight5.shadowMapHeight = 1024;
      spotLight5.shadowMapWidth = 1024;
      // var spotLightHelper5 = new THREE.SpotLightHelper(spotLight5);
      // spotLight5.add(spotLightHelper5);
     
      //entry light
      //make carpetEntry here for take target light
      carpetEntry = getCarpet(200, 250, "carpetEntry.jpg");
      carpetEntry.position.set(95,-120,15.1);
      lightScene.add(carpetEntry);
      var entrylight = new THREE.SpotLight(0xffffff);
      entrylight.castShadow = true;
      entrylight.angle = Math.PI/6;
      entrylight.shadowCameraNear = 2;
      entrylight.shadowCameraFar = 500;
      entrylight.shadowCameraLeft = 500;
      entrylight.shadowCameraRight = 500;
      entrylight.shadowDarkness = .5;
      entrylight.shadowCameraTop = 500;
      entrylight.shadowCameraBottom = 500;
      entrylight.intensity = .5;
      entrylight.shadowMapHeight = 2000;
      entrylight.shadowMapWidth = 2000;
      entrylight.target = carpetEntry;
      entrylight.position.set(0,120,300);
      // var entrylightHelper = new THREE.SpotLightHelper(entrylight);
      // entrylight.add(entrylightHelper);

      //carpetEntry.add(entrylight);
      //lightScene.add(spotLight);
      //lightScene.add(spotLight1);
      lightScene.add(spotLight2);
      //lightScene.add(spotLight3);
      //lightScene.add(spotLight4);
      lightScene.add(spotLight5);

}
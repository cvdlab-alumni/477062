function getSphereLamp(radius){
  var sphereGeometry = new THREE.SphereGeometry(radius, 20, 20);
  var sphereMaterial = new THREE.MeshPhongMaterial({color: 0x6C5CE4,
    metal:true,shininess: 100,specular: 0xffffff});
  var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
  sphere.position.set(0, 0, 0);
  sphere.castShadow = true;
  return sphere;
}

function mkJoint (radius, height) {
  var joint = new THREE.Object3D();
  var sphereGeometry = new THREE.SphereGeometry(radius, 20, 20);
  var sphereMaterial = new THREE.MeshPhongMaterial({color: 0x6C5CE4,
    metal:true,specular: 0xffffff,shininess: 100});
  var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
  sphere.position.set(0, 0, 0);
  sphere.castShadow=true;
  joint.add(sphere);

  var cylinderGeometry = new THREE.CylinderGeometry(radius, radius, height, 20, 20);
  var cylinderMaterial = new THREE.MeshPhongMaterial({color: 0x3A3636,
    metal:true,shininess: 100,specular: 0xffffff});
  var cylinder = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
  cylinder.position.set(0, height / 2 + radius, 0);
  cylinder.castShadow=true;
  sphere.add(cylinder);

  var hook = new THREE.Object3D();
  hook.position.set(0, height/2+radius, 0);
  cylinder.add(hook);

  joint.sphere = sphere;
  joint.cylinder = cylinder;
  joint.hook = hook;
  return joint;
}
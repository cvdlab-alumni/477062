function getBox(lung,larg,spessore,colorBox){
    var GeometriaPiano = new THREE.BoxGeometry(lung,larg,spessore);
    var MaterialePiano = new THREE.MeshPhongMaterial({color: colorBox,
    	side: THREE.DoubleSide,transparent: true, opacity: 1});
    var box = new THREE.Mesh(GeometriaPiano,MaterialePiano);
    return box;
}

function getBoxFrameObject(lung,larg,spessore,colorBox){
    var GeometriaPiano = new THREE.BoxGeometry(lung,larg,spessore);
    var MaterialePiano = new THREE.MeshPhongMaterial({color: colorBox,
        side: THREE.DoubleSide,transparent: true, opacity: 1});
    var box = new THREE.Mesh(GeometriaPiano,MaterialePiano);
    return box;
}

function getRoofBox(lung,larg,spessore,colorBox){
    var GeometriaPiano = new THREE.BoxGeometry(lung,larg,spessore);
    var MaterialePiano = new THREE.MeshBasicMaterial({color: colorBox,
    	side: THREE.DoubleSide,transparent: true, opacity: .5});
    var box = new THREE.Mesh(GeometriaPiano,MaterialePiano);
    return box;
}

 function getCylinder(x1,x2,x3,x4,colorCylinder){
    var Geometriaclilindro = new THREE.CylinderGeometry(x1,x2,x3,x4);
    var MaterialeCilindro = new THREE.MeshLambertMaterial({color: colorCylinder});
    var getCylinder = new THREE.Mesh(Geometriaclilindro,MaterialeCilindro);
    getCylinder.position.set(0,5,0);
    return getCylinder;
}

function getSphere(r,div1,div2,colorSphere){
    var sphereGeometry = new THREE.SphereGeometry(r,div1,div2);
    var sphereMaterial = new THREE.MeshPhongMaterial({color: colorSphere,
        side: THREE.DoubleSide,transparent: true, opacity: 1});
    var sphere = new THREE.Mesh(sphereGeometry,sphereMaterial);
    return sphere;
}
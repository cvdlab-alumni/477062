/*create shape wall with any hole and make a mesh*/
function buildWall(wall,hole,textureWall){
    var wallshape = new THREE.ShapeGeometry(createWallShape(wall,hole));
    meshWall = getMeshWall(wallshape,textureWall);
    return meshWall;
}
/*create mesh wall*/
function getMeshWall(wallshape,textureWall){
    var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+textureWall);
    image.wrapS = THREE.RepeateWrapping;
    image.wrapT = THREE.RepeateWrapping;
    var text = new THREE.MeshLambertMaterial({map: image, side: THREE.DoubleSide});
    var wall = new THREE.Mesh(wallshape,text);
    return wall;
}
/*create shape wall with any hole*/
function createWallShape(wall,holes) {
    var i,j;
    var shape = new THREE.Shape();
    for(i=0; i<wall.length; i++){
        wall[i][0] = wall[i][0]/2000;
        wall[i][1] = wall[i][1]/2000;
        }
    for(j=0; j<holes.length; j++)
        for(i=0; i<holes[j].length; i++){
            holes[j][i][0] = holes[j][i][0]/2000;
            holes[j][i][1] = holes[j][i][1]/2000;
            }
    shape.moveTo(wall[0][0], wall[0][1]);
    for(i=1; i<wall.length; i++)
            shape.lineTo(wall[i][0], wall[i][1]);

    for(j=0; j<holes.length; j++){
      var doorhole = new THREE.Path();
      doorhole.moveTo(holes[j][0][0], holes[j][0][1])
      for(i=1;i<holes[j].length;i++)
              doorhole.lineTo(holes[j][i][0], holes[j][i][1]);
    shape.holes.push(doorhole); 
    }
    return shape;
}
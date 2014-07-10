function moreAnimation(nodeAnimation){
	ball = "ball.jpg";
	var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+ball);
    image.wrapS = image.wrapT = THREE.RepeatWrapping; 
    image.repeat.set(2,2);

    var ballMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
    var ballGeometry = new THREE.SphereGeometry(20,20,20);
    var ball = new THREE.Mesh(ballGeometry, ballMaterial);
   	ball.position.set(-100,-200,30);
   	ball.interact = function (){
   		initAnimator();
	    animator.start();
	}
   	nodeAnimation.add(ball);

    var ballMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
    var ballGeometry = new THREE.SphereGeometry(20,20,20);
    var ball1 = new THREE.Mesh(ballGeometry, ballMaterial);
   	ball1.position.set(140,-430,30);
   	ball1.interact = function (){
   		initAnimator1();
	    animator1.start();
	}
   	nodeAnimation.add(ball1);

	//animation
    var animator = null;
    var duration = 1;
    var loopAnimation = false;
   	function initAnimator() {
        animator = new KF.KeyFrameAnimator;
        animator.init({ 
        interps:
        [
            { 
            keys:[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,.1], 
            values:[
                { y:-150 ,z : 40 },
                { y:-100 ,z : 50 },
                { y:-50 ,z : 60 },
                { y:-40 ,z : 70  },
                { y:-0 ,z : 75 },
                { y:-40 ,z : 70 },
                { y:- 50,z : 60 },
                { y: -100,z : 50 },
                { y: -150,z : 40 },
                { y: -200,z : 30 },
                ],
                target:ball.position
                },
            ],
        loop: loopAnimation,
        duration: duration * 1000
        });
        }


	//animation
    var animator1 = null;
    var duration1 = 1;
    var loopAnimation1 = true;

    function initAnimator1() {
        animator1 = new KF.KeyFrameAnimator;
        animator1.init({ 
        interps:
        [
            { 
            keys:[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,.1], 
             values:[
                {y:-420 ,z : 100 },
                {y:-410 , z : 110 },
                {y:-400 , z : 120 },
                {y:-400 ,z : 130  },
                {y:-400 , z : 140 },
                {y:-400 , z : 130 },
                {y:-400 , z : 120 },
                {y:-400 , z : 110 },
                {y:-400 , z : 100 },
                {y:-400 ,z :85 },
                ],
                target:ball1.position
                },
            ],
        loop: loopAnimation1,
        duration: duration1 * 1000
        });
        }
    var element = [ball,ball1];
    return element;
}


